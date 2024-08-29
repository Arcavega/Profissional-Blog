from django.db import models

# Create your models here.

class mh(models.Model):
    texto1 = models.TextField()

class c(models.Model):
    texto1 = models.TextField()

class h(models.Model):
    texto1 = models.TextField()

class e(models.Model):
    texto1 = models.TextField()

class t(models.Model):
    texto1 = models.TextField()

class m1(models.Model):
    foto = models.ImageField(upload_to='foto/')
    texto1 = models.CharField(max_length=50)