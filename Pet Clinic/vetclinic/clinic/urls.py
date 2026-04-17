from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('owners/add/', views.owner_create, name='owner_create'),
    path('pets/delete/<int:id>/', views.pet_delete, name='pet_delete'),
    path('pets/edit/<int:id>/', views.pet_edit, name='pet_edit'),
    path('vets/', views.vets, name='vets'),
    path('appointments/add/', views.appointment_create, name='appointment_create'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/add/', views.appointment_create, name='appointment_create'),
    path('records/', views.records, name='records'),
    path('medications/', views.medications, name='medications'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('records/add/<int:appointment_id>/', views.record_from_appointment, name='record_from_appointment'),
    path('prescriptions/add/<int:record_id>/', views.add_prescription, name='add_prescription'),
    path('owners/', views.owners, name='owners'),
    path('pets/', views.pets, name='pets'),
    path('appointments/', views.appointments, name='appointments'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]