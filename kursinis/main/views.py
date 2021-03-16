from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse

from job.models import Job
from userprofile.models import Userprofile
# Create your views here.
def frontpage(request):
    jobs = Job.objects.filter(status=Job.ACTIVE).order_by('-created_at')[0:50]

    return render(request, 'core/frontpage.html', {'jobs': jobs})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'fundseeker')

            if account_type == 'investor': 
                userprofile = Userprofile.objects.create(user=user, is_investor=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()
            login(request, user)

            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})