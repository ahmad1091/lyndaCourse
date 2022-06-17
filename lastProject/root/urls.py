from django.urls import path
from root.views import (ContentlessonUpdate,ContentlessonList, DepartmantLessonList, DepartmantLessonUpdate, DepartmantList,DepartmantDetails,
                        DepartmantOverview, DepartmantOverviewlist,UpdateDepartmant, 
                        InstructionDepartmantList, UpdateInstructionDepartmant,
                        WarmUpList, WarmUpUpdate)


urlpatterns = [
    
    path('',DepartmantList.as_view()),
    path('<int:id>/', DepartmantDetails.as_view(),name="departmant-detail"),
    path('<int:pk>/update/', UpdateDepartmant.as_view(),name="departmant-update"),

    path('<int:id>/instruction/', InstructionDepartmantList.as_view()),
    path('<int:pk>/instruction-update/', UpdateInstructionDepartmant.as_view()),

    path('<int:id>/content/', DepartmantOverviewlist.as_view()),
    path('<int:departmant>/content-update/', DepartmantOverview.as_view()),

    path('<int:id>/lesson/', DepartmantLessonList.as_view()),
    path('<int:pk>/lesson-update/', DepartmantLessonUpdate.as_view()),

    path('<int:warmup_lesson>/warmup/', WarmUpList.as_view()),
    path('<int:pk>/warmup-update/', WarmUpUpdate.as_view()),

    path('<int:id>/lesson-content/', ContentlessonList.as_view()),
    path('<int:pk>/lesson-content/update/', ContentlessonUpdate.as_view()),


]
