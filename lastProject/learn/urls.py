from django.urls import path
from .views import (Instructionexam, PracticeChoiceQ, PracticeQ, WarmupQ,
                        PracticeMatchQ, ExamQ, submit_choice_q,submit_practic_q)


urlpatterns = [
    path('<int:id>/instruction/', Instructionexam.as_view()),

    path('<str:name>/<int:lesson_number>/<str:qustion_type>/',WarmupQ.as_view()),

    path('choice/<str:name>/<int:lesson_number>/<str:qustion_type>/',PracticeChoiceQ.as_view()),
    path('<int:id>/submit-choice/',submit_choice_q),

    path('quiz/<str:name>/<int:lesson_number>/<str:qustion_type>/',PracticeQ.as_view()),
    path('<int:id>/answer',submit_practic_q),

    path('match/<str:name>/<int:lesson_number>/<str:qustion_type>/',PracticeMatchQ.as_view()),
    path('<int:id>/instruction/', Instructionexam.as_view()),
    path('<int:id>/part-1/', ExamQ.as_view()),


]
