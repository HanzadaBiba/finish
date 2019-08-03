from django.contrib import admin
from account.models import Profile,Position
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','departament','position']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Position)