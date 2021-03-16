from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from job.models import Application, Job

@login_required
def dashboard(request):
    return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})

@login_required
def view_application(request, application_id):
    
    application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    return render(request, 'userprofile/view_application.html', {'application': application})

@login_required
def view_dashboard_projects(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)
    
    if request.method == "POST":
        job.delete()
        return redirect('dashboard')
    
    return render(request, 'userprofile/view_dashboard_projects.html', {'job': job})