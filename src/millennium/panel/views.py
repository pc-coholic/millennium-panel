from django.shortcuts import render, redirect
# Create your views here.

def change_tenant(request, tenant):
    if (request.user.groups.filter(id=tenant).exists() == True):
        request.session['tenant'] = tenant
    return redirect('admin:index')
