from django.contrib import admin

from root.models import  InstructionDepartmant, Lesson, WarmUp,Departmant,ContentLesson,ContentDepartmant

# Register your models here.


class DepartmantAdmin(admin.ModelAdmin):
    list_display = ['name' ,'is_active']


class ContentDepartmantAdmin(admin.ModelAdmin):
    list_display=['departmant','video','content']


class InstructionDepartmantAdmin(admin.ModelAdmin):
    list_display=['departmant','instruction']

class InstructionExamAdmin(admin.ModelAdmin):
    list_display=['departmant','instruction']

class WarmUpAdmin(admin.ModelAdmin):
    list_display=['title','videofile']

class LessonAdmin(admin.ModelAdmin):
    list_display=['title','description','is_done','departmant','lesson_number']

class ContentLessonAdmin(admin.ModelAdmin):
    list_display=['lesson','title','video','content']

admin.site.register(Departmant,DepartmantAdmin)
admin.site.register(ContentDepartmant,ContentDepartmantAdmin)
admin.site.register(InstructionDepartmant,InstructionDepartmantAdmin)
admin.site.register(WarmUp,WarmUpAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(ContentLesson,ContentLessonAdmin)