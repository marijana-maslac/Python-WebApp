from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Korisnici(AbstractUser):
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=10, choices=(('none', 'None'),('redovni', 'Redovni'), ('izvanredni', 'Izvanredni')))
    uloga = models.CharField(max_length=20, choices=(('ADMIN', 'admin'),('PROF', 'profesor'),('STU', 'student')),null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.email, self.uloga)

class Predmeti(models.Model):
    name = models.CharField(max_length=255)
    kod = models.CharField(max_length=16)
    program = models.CharField(max_length=255)
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    IZBORNI_PREDMET = (('Da','Da'), ('Ne','Ne'))
    izborni = models.CharField(max_length=30, choices=IZBORNI_PREDMET, blank=True)
    nositelj = models.ForeignKey(Korisnici, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.kod)

class Upisi(models.Model):
    student = models.ForeignKey(Korisnici, on_delete=models.CASCADE)
    predmet = models.ForeignKey(Predmeti, on_delete=models.CASCADE)
    STATUS = (('upis', 'upisan'), ('da', 'polozen'), ('ne', 'izgubio potpis'))
    status = models.CharField(max_length=64, choices=STATUS,null=True, blank=True, default='upis')

    def __str__(self):
        return '%s %s %s' % (self.student, self.predmet, self.status)