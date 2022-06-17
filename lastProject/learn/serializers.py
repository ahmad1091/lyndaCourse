from rest_framework import serializers
import os 

from .models import QuestionChoice,QuestionMatch,QuestionPractice,QuestionType,InstructionExam

class InstructionExamSerializers(serializers.ModelSerializer):
    class Meta:
        model=InstructionExam
        fields="__all__"

class QuestionPracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model=QuestionPractice
        fields=('text_question','text_to_voice')

class QuestionMatchSerializers(serializers.ModelSerializer):
    class Meta:
        model=QuestionMatch
        fields="__all__"

class QuestionChoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model=QuestionChoice
        fields="__all__"

class QuestionChoicePracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model=QuestionChoice
        fields="__all__"

class QuestionTypeSerializers(serializers.ModelSerializer):
    lesson_C_T = QuestionChoiceSerializers(many=True)
    lesson_M_T = QuestionMatchSerializers(many=True)
    lesson_P_T = QuestionPracticeSerializers(many=True)
    
    class Meta:
        model=QuestionType
        fields="__all__"