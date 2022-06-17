from django.contrib import admin
from chat.models import Room,Message
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ("host","name","description","updated","created")

class MessageAdmin(admin.ModelAdmin):
    list_display = ("user","room","body","updated","created")


admin.site.register(Room,RoomAdmin)
admin.site.register(Message,MessageAdmin)