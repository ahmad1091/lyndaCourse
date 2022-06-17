from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from root.models import Departmant, Lesson
from .serializers import InstructionExamSerializers, QuestionChoiceSerializers, QuestionMatchSerializers, QuestionPracticeSerializers,QuestionChoicePracticeSerializers
from .models import   InstructionExam, QuestionChoice, QuestionMatch, QuestionType,QuestionPractice
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse


class WarmupQ(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionChoiceSerializers

    def get_queryset(self):
        departmant_id=Departmant.objects.get(name=self.kwargs['name']).id
        lesson_id=Lesson.objects.get(lesson_number=self.kwargs['lesson_number'],departmant=departmant_id).id
        q_type_id=QuestionType.objects.get(qustion_type=self.kwargs['qustion_type']).id
        return QuestionChoice.objects.filter(lesson=lesson_id,type_question=q_type_id)

class PracticeChoiceQ(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionChoicePracticeSerializers

    def get_queryset(self):
        departmant_id=Departmant.objects.get(name=self.kwargs['name']).id
        lesson_id=Lesson.objects.get(lesson_number=self.kwargs['lesson_number'],departmant=departmant_id).id
        q_type_id=QuestionType.objects.get(qustion_type=self.kwargs['qustion_type']).id
        return QuestionChoice.objects.filter(lesson=lesson_id,type_question=q_type_id)

class PracticeQ(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionPracticeSerializers

    def get_queryset(self):
        departmant_id=Departmant.objects.get(name=self.kwargs['name']).id
        print(departmant_id)
        lesson_id=Lesson.objects.get(lesson_number=self.kwargs['lesson_number'],departmant=departmant_id).id
        print(lesson_id)
        
        q_type_id=QuestionType.objects.get(qustion_type=self.kwargs['qustion_type']).id
        print(q_type_id)
        
        return QuestionPractice.objects.filter(lesson=lesson_id,type_question=q_type_id)

class PracticeMatchQ(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionMatchSerializers

    def get_queryset(self):
        departmant_id=Departmant.objects.get(name=self.kwargs['name']).id
        print(departmant_id)
        lesson_id=Lesson.objects.get(lesson_number=self.kwargs['lesson_number'],departmant=departmant_id).id
        print(lesson_id)
        
        q_type_id=QuestionType.objects.get(qustion_type=self.kwargs['qustion_type']).id
        print(q_type_id)
        
        return QuestionMatch.objects.filter(lesson=lesson_id,type_question=q_type_id)


class Instructionexam(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InstructionExamSerializers

    def get_queryset(self):
        return InstructionExam.objects.filter(departmant=self.kwargs['id'])


class ExamQ(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionChoiceSerializers

    def get_queryset(self):
        departmant=Departmant.objects.get(id=self.kwargs['id'])
        return QuestionChoice.objects.filter(departmant=departmant,type_question=1)

@api_view(['POST','OPTIONS'])
def submit_choice_q(request,id):
    q=QuestionChoice.objects.get(id=id)
    print(q.lesson)
    if q.ans == request.data['answer']:
        return Response({'message':'you  submit correct answer'})
    else :
        return Response({'message':'you  submit wrong answerplese review {} lesson'.format(q.lesson)})


@api_view(['POST','OPTIONS'])
def submit_practic_q(request,id):
    answer=QuestionPractice.objects.get(id=id).ans_1
    if answer == request.data['answer']:
        return Response({'message':'you  submit correct answer'})
    else :
        return Response({'message':'you  submit wrong answer'})

