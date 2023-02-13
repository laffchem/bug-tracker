from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .forms import BugForm, ProjectForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Bug, Project
from .serializers import ProjectSerializer, BugSerializer
from django.http import JsonResponse


@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@api_view(['GET'])
def bug_list(request):
    bugs = Bug.objects.all()
    serializer = BugSerializer(bugs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def bug_detail(request, pk, status=None):
    try:
        bug = Bug.objects.get(pk=pk)
    except Bug.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BugSerializer(bug)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BugSerializer(bug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        bug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# This is the actually site pages
class CreateBugView(FormView):
    template_name = 'api/report.html'
    form_class = BugForm
    success_url = 'bug_list'

    def form_valid(self, form):
        bug = form.save(commit=False)
        bug.reporter = self.request.user
        bug.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'api/create_project.html', {'form': form})


def bug_edit(request, pk):
    bug = Bug.objects.get(id=pk)
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Bug updated successfully'})
        else:
            return JsonResponse({'message': 'Failed to update bug'})
    else:
        form = BugForm(instance=bug)
    return render(request, 'api/bug_edit.html', {'form': form, 'bug': bug})


def bug_delete(request, pk):
    bug = Bug.objects.get(id=pk)
    bug.delete()
    return JsonResponse({'message': 'Bug deleted successfully'})


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@login_required()
def project_bugs(request, project_pk):
    bugs = Bug.objects.filter(project__pk=project_pk)
    projects = Project.objects.filter(pk=project_pk)
    project_name = projects[0].name if projects else None
    serializer = BugSerializer(bugs, many=True)
    return render(request, 'api/bugs.html', {'bugs': serializer.data, 'project_name': project_name})



def project_table(request):
    projects = Project.objects.all()
    return render(request, 'api/projects.html', {'projects': projects})
