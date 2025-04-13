from django.urls import path
from .views import RegisterPage, TaskList, TaskDetail , TaskCreate , TaskUpdate , TaskDelete , CustomLoginView, logoutUser


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    
]

