from django.urls import path
from account import views
from django.contrib.auth import views as auth_views
urlpatterns=[
path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('admin/<int:id>',views.admin_home,name='admin_home'),
path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
path('register/', views.register, name='register'),
path('work/<int:id>',views.work_index,name='work'),
path('dyp/<int:id>',views.dyp_index,name='dyp'),
path('dit/<int:id>',views.dit_index,name='dit'),


path('worker_edit/<str:slug>',views.worker_edit,name='worker_edit'),


path('units_list',views.units_list,name='units_list'),
path('unit/<str:slug>',views.units_detail,name='unit_detail'),
path('unit/<str:slug>/delete',views.units_delete,name='Units_delete'),
path('unit/<str:slug>/update',views.Units_update.as_view(),name='Units_update'),
path('unit_create',views.Units_create.as_view(),name='Units_create'),


path('departament/<str:slug>',views.departament_detail,name='departament_detail'),
path('departament/<str:slug>/update',views.Departament_update.as_view(),name='departament_update'),
path('departament/<str:slug>/delete',views.Departament_delete,name='departament_delete'),
path('departament_create/<int:id>',views.Departament_create,name='Departament_create'),

path('departament_block/<str:slug>',views.departament_block_detail,name='departament_block_detail'),
path('departament_block/<int:id>/create',views.Departament_block_create,name='departament_block_create'),
path('departament_block/<str:slug>/update',views.Departament_block_update.as_view(),name='departament_block_update'),
path('departament_block/<str:slug>/delete',views.Departament_block_delete,name='departament_block_delete'),

path('worker/<str:slug>',views.worker_detail,name='worker_detail'),
path('worker_create/<int:id>',views.worker_create,name='worker_create'),
path('worker_block_create/<int:deps_id>/<int:deps_block_id>',views.worker_add,name='block_worker_add'),

path('new_worker_edit/<str:slug>',views.new_worker_edit,name='new_worker_edit'),
path('worker/<str:slug>/delete',views.Worker_delete,name='WorkerDeleteView')

]