from django.shortcuts import render, redirect, get_object_or_404
from django.http import *
from .models import Predmeti, Korisnici, Upisi
from .forms import UserForm, SubjectForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def svi_predmeti(request):
    if str(request.user.uloga) == "ADMIN":
        predmeti = Predmeti.objects.all()
        return render(request, 'subjects.html', {'data': predmeti})
    elif str(request.user.uloga) == "PROF":
        predmeti = Predmeti.objects.filter(nositelj=request.user)
        return render(request, 'subjects.html', { 'data': predmeti})

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('password'))
            form.save()
            return redirect('login')
        else:
            return redirect('home')
    else:
        form = UserForm()
        return render(request, 'register.html', {'form': form})

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login_by_user')
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def login_by_user(request):
    if str(request.user.uloga) == 'ADMIN':
        url = 'admin/'
    elif str(request.user.uloga) == 'PROF':
        url = 'profesor/'
    elif str(request.user.uloga) == 'STU':
        url = 'student/'
    else:
        url='login/'
    return redirect(url)

@login_required
@user_passes_test(lambda u: u.uloga == "PROF")
def profesor_view(request):
    return render(request, 'profesor.html')

@login_required
@user_passes_test(lambda u: u.uloga == "STU")
def student_view(request):
    student_id = request.user.id
    return render(request, 'student.html', {"data": student_id})

@login_required
@user_passes_test(lambda u: u.uloga == "ADMIN")
def admin_view(request):
    return render(request, 'admin.html')

def add_subject(request):
    if request.method == 'GET':
        form = SubjectForm()
        return render(request, 'add_subject.html', {'form' : form})
    elif request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')
        else:
            return HttpResponseNotAllowed()
    else:
        return HttpResponseNotAllowed()
   
def delete_subject(request, subject_id):
    Predmeti.objects.filter(id=subject_id).delete()
    return redirect('subjects')

def get_subject_details(request, id):
    subject = get_object_or_404(Predmeti, pk=id)
    return render(request, 'details_subject.html', {'subject': subject})

def edit_subject(request, id):
    subject = Predmeti.objects.get(pk=id)
    if request.method == 'GET':
        form = SubjectForm(instance=subject)
        return render(request, 'edit_subject.html', {"form":form})
    elif request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects')
        else:
            return HttpResponseNotAllowed()
    else:
        return HttpResponseNotAllowed()

def svi_profesori(request):
    profesors = Korisnici.objects.filter(uloga='PROF')
    return render(request, 'profesors_admin_navigation.html', {'profesors': profesors})

def add_profesor(request):
    dict = { "uloga": "PROF", "status": "none"}
    if request.method == 'GET':
        form = UserForm(initial=dict)
        return render(request, 'add_profesor.html', {'form' : form})
    elif request.method == 'POST':
        form = UserForm(request.POST, initial=dict)
        if form.is_valid():
            form.save()
            return redirect('profesors_admin_navigation')
        else:
            return render(request, 'add_profesor.html', {'form': form})
    else:
        return HttpResponseNotAllowed()

def check_prof(request,profesor_id):
    if request.method == 'GET':
        return render(request, 'check_prof_delete.html', {"data": profesor_id})
    return HttpResponseNotAllowed()
    
def delete_profesor(request, profesor_id):
    if 'Da' in request.POST:
        Korisnici.objects.filter(id=profesor_id).delete()
    return redirect('profesors_admin_navigation')

def edit_profesor(request, id):
    profesor = Korisnici.objects.get(pk=id)
    if request.method == 'GET':
        form = UserForm(instance=profesor)
        return render(request, 'edit_profesor.html', {"form":form})
    elif request.method == 'POST':
        form = UserForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
        return redirect('profesors_admin_navigation')
    else:
        return HttpResponseNotAllowed()

def svi_studenti(request):
    students = Korisnici.objects.filter(uloga='STU')
    return render(request, 'students_admin_navigation.html', {'students': students})

def add_student(request):
    dict = { "uloga": "STU"}
    if request.method == 'GET':
        form = UserForm(initial=dict)
        return render(request, 'add_student.html', {'form' : form})
    elif request.method == 'POST':
        form = UserForm(request.POST, initial=dict)
        if form.is_valid():
            form.save()
            return redirect('students_admin_navigation')
        else:
            return render(request, 'add_student.html', {'form': form})
    else:
        return HttpResponse("Beep beep, there is problem.")

def edit_student(request, id):
    student = Korisnici.objects.get(pk=id)
    if request.method == 'GET':
        form = UserForm(instance=student)
        return render(request, 'edit_student.html', {"form" : form})
    elif request.method == 'POST':
        form = UserForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('students_admin_navigation')
    else:
        return HttpResponseNotAllowed()

def delete_student(request, student_id):
    if 'Da' in request.POST:
        Korisnici.objects.filter(id=student_id).delete()
    return redirect('students_admin_navigation')
 
def check_stu(request,student_id):
    if request.method == 'GET':
        return render(request, 'check_stu_delete.html', {"data": student_id})
    return HttpResponseNotAllowed()

@login_required
def studenti_po_predmetu(request, subject_id):
    if str(request.user.uloga) == 'ADMIN':
        upisani = Upisi.objects.filter(predmet_id=subject_id)
        return render(request, 'student_admin_subjects.html', {"data" : upisani})
    elif str(request.user.uloga) == 'PROF':
        subject = Predmeti.objects.get(id=subject_id)
        upisani = Upisi.objects.filter(predmet_id=subject_id)
        return render(request, 'student_profesor_subjects.html',{"data" : upisani, "subject": subject})
    
def change_student_status_prof(request, upis_id):
    upis = get_object_or_404(Upisi, id=upis_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        student_id = request.POST.get('student_id')
        upis.status = status
        upis.save()
        return redirect('student_profesor_subjects', subject_id=upis.predmet_id)
    return render(request, 'student_profesor_subjects.html', {'upisani': upis})

@login_required
def upisni_list(request):
    student = request.user
    predmeti = Predmeti.objects.all()
    upisani_predmeti = student.upisi_set.all().values_list('predmet_id', flat=True)
    return render(request, 'upisni_list.html', {"predmeti": predmeti, "student": student, "upisani_predmeti": upisani_predmeti})

def upis_ili_ispis(request, predmet_id):
    student = request.user
    predmet = Predmeti.objects.get(id=predmet_id)
    try:
        upis = Upisi.objects.get(student=student, predmet=predmet)
        upis.delete()
    except Upisi.DoesNotExist:
        Upisi.objects.create(student=student, predmet=predmet)

    return redirect('upisni_list')

@login_required
@user_passes_test(lambda u: u.uloga == "ADMIN")
def student_upisni_list(request, student_id):
    try:
        student = Korisnici.objects.get(id=student_id)
        predmeti = Predmeti.objects.all()
        upisani_predmeti = [upis.predmet.id for upis in Upisi.objects.filter(student=student)]
        return render(request, 'student_upisni_list.html', {'student': student, 'predmeti': predmeti, 'upisani_predmeti': upisani_predmeti})
    except Korisnici.DoesNotExist:
        return HttpResponseNotAllowed()
    
def upis_ili_ispis_admin(request, student_id, predmet_id):
    student = Korisnici.objects.get(id=student_id)
    predmet = Predmeti.objects.get(id=predmet_id)
    try:
        upis = Upisi.objects.get(student=student, predmet=predmet)
        upis.delete()
    except Upisi.DoesNotExist:
        Upisi.objects.create(student=student, predmet=predmet)

    return redirect('student_upisni_list', student_id=student_id)

def studenti_predmet_upisani(request, subject_id):
    upisani = Upisi.objects.filter(predmet_id=subject_id)
    return render(request, 'studenti_predmet_upisani.html',{"data" : upisani})

def studenti_predmet_polozili(request, subject_id):
    upisani = Upisi.objects.filter(predmet_id=subject_id)
    return render(request, 'studenti_predmet_polozili.html',{"data" : upisani})

def studenti_predmet_pali(request, subject_id):
    upisani = Upisi.objects.filter(predmet_id=subject_id)
    return render(request, 'studenti_predmet_pali.html',{"data" : upisani})

@login_required
@user_passes_test(lambda u: u.uloga == "ADMIN")
def svi_studenti_admin(request):
    students = Korisnici.objects.filter(uloga='STU')
    student_data = []
    svi_predmeti = Predmeti.objects.all()

    for student in students:
        upisani_predmeti = student.upisi_set.filter(status='upis').values_list('predmet_id', flat=True)
        upisani_ects = 0
        polozeni_ects = 0
        
        for predmet_id in upisani_predmeti:
            predmet = Predmeti.objects.get(id=predmet_id)            
            upisani_ects += predmet.ects
        
        for predmet in svi_predmeti:
            if student.upisi_set.filter(predmet=predmet, status='polozen').exists():
                polozeni_ects += predmet.ects
                
        ukupni_ects = upisani_ects + polozeni_ects
        student_data.append({
            'student': student,
            'upisani_ects': upisani_ects,
            'polozeni_ects': polozeni_ects,
            'ukupni_ects': ukupni_ects
        })
    
    return render(request, 'zadatak1.html', {'student_data': student_data})

@login_required
@user_passes_test(lambda u: u.uloga == "ADMIN")
def prikazi_detalje(request, student_id):
    student = Korisnici.objects.get(id=student_id)
    polozeni = Upisi.objects.filter(student=student, status='polozen').values_list('predmet__name', flat=True)
    upisani = Upisi.objects.filter(student=student, status='upis').values_list('predmet__name', flat=True)

    return render(request, 'detalji.html', {'student' : student, 'polozeni' : polozeni, 'upisani': upisani})
