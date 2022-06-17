from django.contrib import admin
from .models import (QuestionType,QuestionChoice ,QuestionPractice,QuestionMatch,
                        InstructionExam)
# Register your models here.

class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display=['lesson','type_question','question','op1','op2','op3','op4','ans']


class QuestionPracticeAdmin(admin.ModelAdmin):
    list_display=['lesson','type_question','text_question','text_to_voice','ans_1','ans_2']

class QuestionMatchAdmin(admin.ModelAdmin):
    list_display=['lesson','type_question','text_to_voice']

class InstructionExamAdmin(admin.ModelAdmin):
    list_display=['departmant','instruction']

admin.site.register(QuestionType)
admin.site.register(InstructionExam,InstructionExamAdmin)
admin.site.register(QuestionChoice,QuestionChoiceAdmin)
admin.site.register(QuestionPractice,QuestionPracticeAdmin)
admin.site.register(QuestionMatch,QuestionMatchAdmin)