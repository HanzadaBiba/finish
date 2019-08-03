from django.urls import path,include
from workers import views
app_name='home'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('units/<str:slug>',views.unit_detail,name='units_detail'),
    path('departament/<str:slug>',views.departament_detail,name='departament_detail'),
    path('worker/<str:slug>',views.worker_detail,name='worker_detail'),
    path('found/',views.founded,name='founded'),
    path('status/<str:slug>/<str:work>',views.status_workers,name='status_workers')
]
