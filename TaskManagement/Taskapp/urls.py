from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Taskapp import views

urlpatterns = [
    # Admin Users
    path('api/projects/', views.AdminProjectListView.as_view(), name='admin-project-list'),
    path('api/projects/<int:pk>/', views.AdminProjectDetailView.as_view(), name='admin-project-detail'),
    # Project Manager
    path('api/projects/manager/', views.ProjectManagerProjectListView.as_view(), name='project-manager-project-list'),
    path('api/projects/manager/<int:pk>/', views.ProjectManagerProjectDetailView.as_view(), name='project-manager-project-detail'),
    # Team Lead
    path('api/tasks/lead/', views.TeamLeadTaskListView.as_view(), name='team-lead-task-list'),
    path('api/tasks/lead/<int:pk>/', views.TeamLeadTaskDetailView.as_view(), name='team-lead-task-detail'),
    # Team Members
    path('api/tasks/member/', views.TeamMemberTaskListView.as_view(), name='team-member-task-list'),
    path('api/tasks/member/<int:pk>/', views.TeamMemberTaskDetailView.as_view(), name='team-member-task-detail'),
    # All Users
    path('api/comments/', views.CommentCreateView.as_view(), name='comment-create'),
    path('api/comments/<int:pk>/', views.CommentDeleteView.as_view(), name='comment-delete'),
    
    
    
    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
