from django.urls import path
from . import views

urlpatterns = [
    path("report/", views.CreateBugView.as_view(), name='report'),
    path("create_project/", views.create_project, name="create_project"),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>', views.project_detail, name='project_detail'),
    path('projects/all/', views.project_table, name='projects'),
    path('projects/<int:project_pk>/bugs/', views.project_bugs, name='project_bugs'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('bugs/<int:pk>/', views.bug_detail, name='bug_detail'),
    path('bugs/edit/<int:pk>/', views.bug_edit, name='bug_edit'),
    path('bugs/delete/<int:pk>/', views.bug_delete, name='bug_delete'),

]