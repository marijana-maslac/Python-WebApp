"""
URL configuration for Projekt2023PNI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home , name='home'),
    path('register/', views.register , name='register'),
    path('subjects/', views.svi_predmeti, name='subjects'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('login_by_user/',views.login_by_user, name='login_by_user'),
    path('login_by_user/admin/', views.admin_view),
    path('login_by_user/profesor/', views.profesor_view),
    path('login_by_user/student/', views.student_view),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('delete_subject/<int:subject_id>', views.delete_subject),
    path('subject/<int:id>', views.get_subject_details, name='details_subject'),    
    path('edit_subject/<int:id>', views.edit_subject, name='edit_subject'),
    path('profesors_admin_navigation/', views.svi_profesori, name='profesors_admin_navigation'),
    path('add_profesor/', views.add_profesor, name='add_profesor'),
    path('delete_profesor/<int:profesor_id>', views.delete_profesor, name='delete_profesor'),
    path('check_prof_delete/<int:profesor_id>', views.check_prof, name='check_prof_delete'),
    path('edit_profesor/<int:id>', views.edit_profesor, name='edit_profesor'),
    path('students_admin_navigation/',views.svi_studenti, name='students_admin_navigation'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:id>', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>', views.delete_student, name='delete_student'),
    path('check_stu_delete/<int:student_id>', views.check_stu, name='check_stu_delete'),
    path('student_admin_subjects/<int:subject_id>', views.studenti_po_predmetu, name='student_admin_subjects'),
    path('student_profesor_subjects/<int:subject_id>', views.studenti_po_predmetu, name='student_profesor_subjects'),
    path('change_student_status_prof/<int:upis_id>/', views.change_student_status_prof, name='change_student_status_prof'),
    path('upisni_list/', views.upisni_list, name='upisni_list'),
    path('upis_ili_ispis/<int:predmet_id>/', views.upis_ili_ispis, name='upis_ili_ispis'),
    path('student_upisni_list/<int:student_id>/', views.student_upisni_list, name='student_upisni_list'),
    path('upis_ili_ispis_admin/<int:student_id>/<int:predmet_id>/', views.upis_ili_ispis_admin, name='upis_ili_ispis_admin'),
    path('studenti_predmet_upisani/<int:subject_id>/', views.studenti_predmet_upisani, name='studenti_predmet_upisani'),
    path('studenti_predmet_polozili/<int:subject_id>/', views.studenti_predmet_polozili, name='studenti_predmet_polozili'),
    path('studenti_predmet_pali/<int:subject_id>/', views.studenti_predmet_pali, name='studenti_predmet_pali'),
    path('zadatak1/',views.svi_studenti_admin, name='zadatak1'),
    path('detalji/<int:student_id>/', views.prikazi_detalje, name='prikazi_detalje'),
]