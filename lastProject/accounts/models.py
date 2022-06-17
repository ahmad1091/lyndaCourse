from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from root.models import Departmant, Lesson


class User(AbstractUser):
  """
  Implement user model 
  """

  is_student = models.BooleanField(default=True)
  is_teacher = models.BooleanField(default=False)
  
  def __str__(self):
       return self.username



class Teacher(models.Model):
  """
  Implement teacher model
  """
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def __str__(self):
      return self.user.username + ' ' +self.user.email

class Student(models.Model):
  """
  Implement student mode 
  """
  user = models.OneToOneField(User, on_delete=models.CASCADE)  
  departmant=models.ManyToManyField(Departmant)
  def __str__(self):
      return self.user.username + ' ' +self.user.email

class Grade(models.Model):
  """
  Implement Grade model
  """
  student=models.ForeignKey(Student,on_delete=models.CASCADE)
  departmant=models.ForeignKey(Departmant,on_delete=models.CASCADE)
  lesson_accomplished=models.IntegerField(default=0)
  pas_exam=models.BooleanField(default=False)
  Exam_score = models.CharField(max_length=255,blank=True,null=True,verbose_name = "Student Test Score")

class ResultLesson(models.Model):
  lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
  is_warmup=models.BooleanField(default=False)
  is_lesson=models.BooleanField(default=False)
  is_practice=models.BooleanField(default=False)
