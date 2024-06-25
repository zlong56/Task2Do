from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, UserLogin, SignupPage
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('signup/', SignupPage.as_view(), name="signup"),
    
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task"),
    path('create-task/', CreateTask.as_view(), name="create-task"),
    path('update-task/<int:pk>', UpdateTask.as_view(), name="update-task"),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name="delete-task"),
    
    path('updateStatus/<int:pk>', views.updateStatus, name="update-status"),
    path('profile/<int:pk>', views.userProfile, name="user-profile"),
    path('update-user', views.updateProfile, name="update-user"),
]
