from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/vote/', views.ProjectVoteView.as_view(), name='project_vote'),
    path('<int:pk>/result/', views.ProjectResultView.as_view(), name='project_result'),
]
