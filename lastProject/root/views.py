from django.shortcuts import render
from requests import request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from accounts.models import Student
from root.permissions import StudentPermission
from root.serializers import (DepartmantSerializers,ContentDepartmantSerializers,
                            InstructionDepartmantSerializers,WarmUpSerializers,
                            LessonSerializers,ContentLessonSerializers,DepartmantDetailsSerializers
                            )


from root.models import  (Departmant,ContentDepartmant,InstructionDepartmant,WarmUp,
                        Lesson,ContentLesson)

from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse


# Create your views here.

class DepartmantList(generics.ListAPIView,generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DepartmantSerializers

    def get_queryset(self):
        return Departmant.objects.all()


class DepartmantDetails(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field='id'
    queryset = Departmant.objects.all()
    serializer_class = DepartmantDetailsSerializers
    

class UpdateDepartmant(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Departmant.objects.all()
    serializer_class = DepartmantSerializers


class InstructionDepartmantList(generics.ListAPIView,generics.CreateAPIView):
    permission_classes = [IsAuthenticated,StudentPermission]
    serializer_class = InstructionDepartmantSerializers

    def get_queryset(self):
        return InstructionDepartmant.objects.filter(departmant=self.kwargs['id'])

class UpdateInstructionDepartmant(generics.UpdateAPIView,generics.DestroyAPIView):

    queryset = InstructionDepartmant.objects.all()
    serializer_class = InstructionDepartmantSerializers


class DepartmantOverviewlist(generics.ListAPIView,generics.CreateAPIView):
    permission_classes = [IsAuthenticated,StudentPermission]
    serializer_class = ContentDepartmantSerializers

    def get_queryset(self):
        return ContentDepartmant.objects.filter(departmant=self.kwargs['id'])


class DepartmantOverview(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    lookup_field='departmant'
    queryset = ContentDepartmant.objects.all()
    serializer_class = ContentDepartmantSerializers

class DepartmantLessonList(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = LessonSerializers

    def get_queryset(self):
        return Lesson.objects.filter(departmant=self.kwargs['id'])

class DepartmantLessonUpdate(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class WarmUpList(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = WarmUpSerializers

    def get_queryset(self):
        return WarmUp.objects.filter(lesson_warmup=self.kwargs['warmup_lesson'])

class WarmUpUpdate(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = WarmUp.objects.all()
    serializer_class = WarmUpSerializers
        

class ContentlessonList(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = ContentLessonSerializers

    def get_queryset(self):
        return ContentLesson.objects.filter(lesson=self.kwargs['id'])


class ContentlessonUpdate(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = ContentLesson.objects.all()
    serializer_class = ContentLessonSerializers




