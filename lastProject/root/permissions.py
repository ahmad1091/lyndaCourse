from django.http import Http404
from rest_framework import permissions
from accounts.models import Student
from root.models import Departmant,InstructionDepartmant
           
class StudentPermission(permissions.BasePermission):
    message = "Student  permission deny"
    edit_methods = ("PUT", "PATCH", "POST")
    safe_methods = ("GET" , "HEAD" , "OPTIONS")

    def get_user_perm(self , request , view , obj):
        try:
            student_id=Student.objects.get(user=request.user).departmant.all().values()
            departmant_id=Departmant.objects.get(id=request.resolver_match.kwargs.get('id')).name  

            if student_id.get()['name'] == departmant_id:
                return True
        except Student.DoesNotExist:
            print("Can't get emp")
            return False
            

       

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if True:
                return self.get_user_perm(request, view,"")
            # return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if obj.author == request.user:
            return True
        if True:
            return self.get_user_perm(request,view,obj)