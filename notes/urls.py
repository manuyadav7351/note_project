from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.note_list, name='note-list'),
    path('notes/create/', views.note_create, name='note-create'),
    path('notes/delete/<int:pk>/', views.note_delete, name='note-delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
    path('notes/', views.note_list, name='note_list'),
]
