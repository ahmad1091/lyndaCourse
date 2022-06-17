from django.db import models

class Departmant(models.Model):
    """
    Implement Departmant models 
    """
    name        =models.CharField(max_length=255, blank=True,null=True)
    is_active   =models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    




class ContentDepartmant(models.Model):
    """
    Implement Content Departmant models 
    """
    
    title       =models.CharField(max_length=200,null=True, blank=True)
    departmant  =models.OneToOneField(Departmant,on_delete=models.CASCADE , related_name='content_departmant')
    video       =models.FileField(upload_to='videos/', null=True)
    content     =models.TextField(blank=True,null=True)


class InstructionDepartmant(models.Model):
    """
    Implement Instruction models 
    """
    departmant              =models.ForeignKey(Departmant,on_delete=models.CASCADE , related_name='instruction_departmant')
    instruction             =models.TextField(blank=True,null=True)

    def __str__(self):
        return self.instruction 


class Lesson(models.Model):
    """
    Implement Lesson models 
    """
    title           =models.CharField(max_length=200)
    description     =models.TextField(blank=True)
    is_done         =models.BooleanField(default=False)
    departmant      =models.ForeignKey(Departmant,on_delete=models.CASCADE,related_name="leeson_departmant")
    lesson_number   =models.IntegerField(blank=True,null=True)   
    is_active       =models.BooleanField(default=True)

    def __str__(self):
        return self.title 

class WarmUp(models.Model):
    """
    Implement Warm Up models 
    """
    title       =models.CharField(max_length=200)
    videofile   = models.FileField(upload_to='videos/', null=True)
    lesson_warmup        =models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name="lesson",null=True,blank=True)


    def __str__(self):
        return self.title

class ContentLesson(models.Model):
    """
    Implement Content Lesson models 
    """
    lesson  =models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name="content_lesson")
    title   =models.CharField(max_length=200)
    video   =models.FileField(upload_to='videos/', null=True)
    content =models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title