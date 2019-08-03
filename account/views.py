from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from account.forms import LoginForm,UserRegistrationForm,Departament_form,Departament_block_form,Departament_workers_form
from account.models import Profile
from workers.models import Workers,Departaments,Units,Departament_block
@login_required
def admin_home(request,id):
    profile = get_object_or_404(Profile, user__id=id)
    departament=profile.departament
    print(departament)
    workers=Workers.objects.filter(deps=departament)
    user = request.user
    return render(request,'admin/admin.html',locals())

def register(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            cd=user_form.cleaned_data
            departament=cd['departament']
            position=cd['position']
            new_profile=Profile.objects.create(user=new_user,departament=departament,position=position)
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form=UserRegistrationForm()
    return render(request,'registration/register.html',locals())
from django.urls import reverse
def work_index(request,id):
    profile = get_object_or_404(Profile, user__id=id)
    departament = profile.departament
    print(profile.position_id)
    print('profile=',profile.id)
    if profile.position_id==1:
        return HttpResponseRedirect(reverse('dit',args=[profile.id]))
    else:
        return HttpResponseRedirect(reverse('dyp',args=[profile.id]))

"""DIT"""
def dit_index(request,id):
    profile = get_object_or_404(Profile, id=id)
    departament = profile.departament.id
    print(departament)
    workers=Workers.objects.filter(deps_id=departament)
    return render(request,'admin/dit_index.html',locals())
from account.forms import WorkerEdit,WorkerAdd,New_worker_edit,Units_form
from django.contrib import messages

def worker_edit(request,slug):
    user_id=request.user.id
    profile=get_object_or_404(Profile,user_id=user_id)
    worker=get_object_or_404(Workers,slug=slug)
    if request.method=="POST":
        worker_form = WorkerEdit(instance=worker,data=request.POST)
        if worker_form.is_valid():
            worker_form.save()
            return HttpResponseRedirect(reverse('dit', args=[profile.id]))
        else:
            messages.error(request, 'Изменение не удалось')
    else:
        worker_form = WorkerEdit(instance=worker)
    return render(request,'admin/worker_edit.html',locals())

from django.views.generic import DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy
"""DYP"""
def dyp_index(request,id):
    profile = get_object_or_404(Profile, id=id)
    departament = profile.departament


    return HttpResponseRedirect(reverse('units_list'))
"""units"""
def units_list(request):
    units=Units.objects.all().order_by('id')
    return render(request, 'admin/units/units_list.html', locals())

def units_detail(request,slug):
    unit=get_object_or_404(Units,slug=slug)
    departaments=Departaments.objects.filter(units=unit)
    return render(request, 'admin/units/units_detail.html', locals())
class Units_create(CreateView):
    model = Units
    template_name = 'admin/units/Units_create.html'
    fields = ['name']
    def get_context_data(self, **kwargs):
        context=super(Units_create, self).get_context_data(**kwargs)
        return context
class Units_update(UpdateView):
    model = Units
    fields = ['name']
    template_name = 'admin/units/units_update.html'
def units_delete(request,slug):
    object=get_object_or_404(Units,slug=slug)
    if request.method=='POST':
        object.delete()
        return HttpResponseRedirect(reverse('units_list'))
    return render(request,'admin/units/units_delete.html',locals())

"""departaments"""

def departament_detail(request,slug):
    departament=get_object_or_404(Departaments,slug=slug)
    unit=departament.units
    workers=Workers.objects.filter(deps=departament)
    departament_blocks=Departament_block.objects.filter(deps=departament)
    return render(request, 'admin/departament/departament_detail.html', locals())
def Departament_create(request,id):
    unit=Units.objects.get(id=id)
    form=Departament_form(initial={'units':unit})
    if request.method=="POST":
        form=Departament_form(data=request.POST)
        if form.is_valid():
            new_departament = form.save(commit=False)
            new_departament.save()
            unit=new_departament.units.slug
            return HttpResponseRedirect(reverse('unit_detail',args=[unit]))
        else:
            messages.error(request, 'Не удалось создать департамент')
    else:
        worker_form = Departament_form()
    return render(request,'admin/departament/Departament_create.html',locals())

class Departament_update(UpdateView):
    model = Departaments
    form_class=Departament_form
    template_name = 'admin/departament/departament_update.html'


def Departament_delete(request,slug):
    object=get_object_or_404(Departaments,slug=slug)
    unit=object.units.slug
    if request.method=='POST':
        object.delete()
        return HttpResponseRedirect(reverse('unit_detail',args=[unit]))
    return render(request,'admin/departament/departaments_delete.html',locals())

"""departament_block"""
def departament_block_detail(request,slug):
    departament_block=get_object_or_404(Departament_block,slug=slug)
    departament=departament_block.deps
    workers=Workers.objects.filter(deps_block=departament_block)
    return render(request,'admin/departament_block/departament_block_detail.html',locals())
class Departament_block_update(UpdateView):
    model = Departament_block
    form_class = Departament_block_form
    template_name = 'admin/departament_block/departament_block_update.html'
def Departament_block_delete(request,slug):
    object=get_object_or_404(Departament_block,slug=slug)
    deps=object.deps.slug
    if request.method=='POST':
        object.delete()
        return HttpResponseRedirect(reverse('departament_detail',args=[deps]))
    return render(request,'admin/departament/departaments_delete.html',locals())

def Departament_block_create(request,id):
    deps=Departaments.objects.get(id=id)
    form=Departament_block_form(initial={'deps':deps})
    if request.method=="POST":
        form=Departament_block_form(data=request.POST)
        if form.is_valid():
            new_departament = form.save(commit=False)
            new_departament.save()
            deps=new_departament.deps.slug
            return HttpResponseRedirect(reverse('departament_detail',args=[deps]))
        else:
            messages.error(request, 'Не удалось создать отдел')
    else:
        worker_form = Departament_form()
    return render(request,'admin/departament_block/Departament_block_create.html',locals())



"""worker"""

from account.forms import Departament_workers_form
def worker_detail(request,slug):
    worker=get_object_or_404(Workers,slug=slug)
    return render(request,'admin/worker_detail.html',locals())
def worker_create(request,id):
    deps = Departaments.objects.get(id=id)
    form=Departament_workers_form(initial={'deps':deps})
    if request.method=='POST':
        form=Departament_workers_form(data=request.POST)
        if form.is_valid():
            new_worker = form.save(commit=False)
            new_worker.save()
            deps=new_worker.deps.slug
            return HttpResponseRedirect(reverse('departament_detail',args=[deps]))
        else:
            messages.error(request, 'Не удалось создать сотрудника')
    else:
        form=Departament_workers_form(initial={'deps':deps})
    return render(request,'admin/worker/worker_create.html',locals())
def worker_add(request,deps_id,deps_block_id):
    deps = Departaments.objects.get(id=deps_id)
    deps_block = Departament_block.objects.get(id=deps_block_id)
    form=WorkerAdd(initial={'deps_block':deps_block,'deps':deps})
    if request.method=="POST":
        form=WorkerAdd(data=request.POST)
        if form.is_valid():
            new_worker=form.save(commit=False)
            new_worker.save()
            deps = new_worker.deps_block.slug
            return HttpResponseRedirect(reverse('departament_block_detail',args=[deps]))
    else:
        worker_add_form=WorkerAdd(initial={'deps_block':deps_block,'deps':deps})
    return render(request,'admin/worker/departaments_block_worker_create.html',locals())

def new_worker_edit(request,slug):
    worker=get_object_or_404(Workers,slug=slug)
    if request.method=='POST':
        edit_form=New_worker_edit(instance=worker,data=request.POST)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('worker_detail',args=[worker.slug]))
    else:
        edit_form = New_worker_edit(instance=worker)
    return render(request,'admin/new_worker_edit.html',locals())
def Worker_delete(request,slug):
    object=get_object_or_404(Workers,slug=slug)
    deps=object.deps.slug
    if request.method=='POST':
        object.delete()
        return HttpResponseRedirect(reverse('departament_detail',args=[deps]))
    return render(request,'admin/worker/worker_delete.html',locals())
