"""
Created on Oct 19, 2016

@author: Jafar Taghiyar (jtaghiyar@bccrc.ca)
"""

#============================
# Django imports
#----------------------------
from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required #, permission_required

#============================
# App imports
#----------------------------
from core.decorators import Render
from khayyam.models import Run

#============================
# Home page of the app
#----------------------------
@Render("picasso/home.html")
def home_view(request):
    """home page of the app."""
    context = {
    }
    # request.session.pop('run')

    return context

@Render("picasso/run_detail.html")
def run_detail(request, pk):
    """home page of the app."""
    run = get_object_or_404(Run, pk=pk)
    is_running = False
    is_authorized = False
    if run.status == "R":
        is_running = True
    if run.user == request.user.username:
        is_authorized = True
    if is_authorized:
        print '*' * 20
    context = {
    'run': run,
    'is_running': is_running,
    'is_authorized': is_authorized,
    }
    return context

@Render("picasso/run_list.html")
def run_list(request):
    """home page of the app."""
    context = {
    'runs': Run.objects.all()
    }
    return context
