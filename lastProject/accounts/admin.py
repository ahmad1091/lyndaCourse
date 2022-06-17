from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import Student, Teacher,Grade,User,ResultLesson
# Register your models here.

class GradeAdmin(admin.ModelAdmin):
    list_display = ['student','departmant','Exam_score','lesson_accomplished','pas_exam']

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','email']

class ResultLessonAdmin(admin.ModelAdmin):
    list_display = ['lesson','is_warmup','is_lesson','is_practice']

class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'is_student', 'is_teacher']
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register([Teacher,Student])
admin.site.register(Grade,GradeAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(ResultLesson,ResultLessonAdmin)