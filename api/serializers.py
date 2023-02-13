from rest_framework import serializers
from .models import Bug, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description')


class BugSerializer(serializers.ModelSerializer):
    reporter = serializers.StringRelatedField()
    assignee = serializers.StringRelatedField(allow_null=True)

    class Meta:
        model = Bug
        fields = ('id', 'title', 'description', 'project', 'reporter', 'assignee', 'status')
