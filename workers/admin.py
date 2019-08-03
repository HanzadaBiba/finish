from django.contrib import admin

# Register your models here.
from django.contrib import admin
from workers.models import Units, Departaments, Departament_block, Position, City, Workers
# Register your models here.
a = [Units, Departaments, Departament_block, Position, City, Workers]
class UnitsAdmin(admin.ModelAdmin):
    list_display = ['name']

class DepartamentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'units']
    list_filter = ['units']
    search_fields = ['name']
class Departament_block_admin(admin.ModelAdmin):
    list_display = ['name', 'deps']
    list_filter = ['deps']
    search_fields = ['name']
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}
class WorkersAdmin(admin.ModelAdmin):
    list_display = ['fullname','status']
    search_fields = ['fullname']
    list_filter = ['status', 'position','deps','deps_block' ]
    list_editable = ['status']
admin_klass = [UnitsAdmin, DepartamentsAdmin, Departament_block_admin, PositionAdmin, CityAdmin, WorkersAdmin]
for i, b in zip(a, admin_klass):
    admin.site.register(i, b)