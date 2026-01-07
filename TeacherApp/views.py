from django.shortcuts import render, redirect
from .models import herotext, contentcolumn,Certification,contentbody,ContactMessage,footer,comparison,whyus
# Create your views here.
def home(request):
    hero = herotext.objects.get(id=1)
    content = contentcolumn.objects.filter(is_active=True)
    Certificate= Certification.objects.filter(is_active=True)
    body = contentbody.objects.filter(is_active=True)
    foot = footer.objects.filter(is_active=True)
    head = footer.objects.filter(is_active=False)
    comp = comparison.objects.filter(is_active=True)
    why = whyus.objects.filter(is_active=True)
    whytitle = whyus.objects.filter(is_active=False)
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        return redirect('home')
    context = {
        'hero':hero,
        'content':content,
        'Certificate':Certificate,
        'body':body,
        'foot':foot,
        'comp':comp,
        'why':why,
        'whytitle':whytitle
    }

    return render(request, 'index.html',context)

import os
from django.http import HttpResponse

def test_env(request):
    value = os.environ.get("CLOUDINARY_URL")
    return HttpResponse(value or "NOT FOUND")
