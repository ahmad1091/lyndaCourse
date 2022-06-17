from numpy import source
from rest_framework import serializers

from root.models import Departmant,ContentDepartmant,InstructionDepartmant,WarmUp,Lesson,ContentLesson




class InstructionDepartmantSerializers(serializers.ModelSerializer):

    class Meta:
        model=InstructionDepartmant
        fields="__all__"
        
class WarmUpSerializers(serializers.ModelSerializer):
    class Meta:
        model=WarmUp
        fields="__all__"


class ContentLessonSerializers(serializers.ModelSerializer):
    class Meta:
        model=ContentLesson
        fields="__all__"

class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields="__all__"

class DepartmantInsturctionSerializers(serializers.ModelSerializer):
    instruction_departmant = InstructionDepartmantSerializers(many=True)    
    class Meta:
        model=Departmant
        fields="__all__"
        
class DepartmantDetailsSerializers(serializers.ModelSerializer):
    instruction_departmant = InstructionDepartmantSerializers(many=True)
    leeson_departmant = serializers.StringRelatedField(many=True)
    
    class Meta:
        model=Departmant
        fields="__all__"



class DepartmantSerializers(serializers.ModelSerializer):
    class Meta:
        model=Departmant
        fields="__all__"

class ContentDepartmantSerializers(serializers.ModelSerializer):
    class Meta:
        model=ContentDepartmant
        fields="__all__"
