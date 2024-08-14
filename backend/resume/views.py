from django.contrib.auth import get_user_model
from django.shortcuts import render

def sample_resume(request):
    usr = get_user_model().objects.first()
    rez = usr.resumes.first()

    context = {'usr': usr, 'rez': rez}
    template = 'sample_resume.html'
    return render(request, template, context)
