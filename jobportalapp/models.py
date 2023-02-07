from django.db import models

# Create your models here.

class regmodel(models.Model):
    cname = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)
    phone = models.IntegerField()
    address=models.CharField(max_length=25)

class pagemodel(models.Model):
    catchoice1=[
        ('Full time','Full time'),
        ('Part time','Part time')

    ]
    catchoice2 = [
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote')

    ]
    catchoice3 = [
        ('0-1', '0-1'),
        ('2-5', '2-5'),
        ('6-10','6-10')

    ]
    cname=models.CharField(max_length=30)
    email=models.EmailField()
    jname=models.CharField(max_length=30)
    jtype=models.CharField(max_length=30,choices=catchoice1)
    wtype=models.CharField(max_length=30,choices=catchoice2)
    exp=models.CharField(max_length=30,choices=catchoice3)



class profilemodel(models.Model):
    image=models.FileField(upload_to='jobportalapp/static')
    fname=models.CharField(max_length=20)
    email=models.EmailField()
    resume=models.FileField(upload_to='jobportalapp/static')
    education=models.CharField(max_length=20)
    exp=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()

class applymodel(models.Model):
    company=models.CharField(max_length=40)
    title=models.CharField(max_length=40)
    fname = models.CharField(max_length=40)
    email = models.EmailField()
    resume = models.FileField(upload_to='jobportalapp/static')
    education = models.CharField(max_length=20)
    exp = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()

class wishmodel(models.Model):
    cname = models.CharField(max_length=30)
    email = models.EmailField()
    jname = models.CharField(max_length=30)
    jtype = models.CharField(max_length=30)
    wtype = models.CharField(max_length=30)
    exp = models.CharField(max_length=30)

