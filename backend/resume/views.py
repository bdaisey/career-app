from django.shortcuts import render

def sample_resume(request):
    return render(request, 'sample_resume.html')
