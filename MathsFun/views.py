from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import AllStandard, Topic, Weightage
from django.contrib.auth.decorators import login_required


def Standard(request):
    ac = AllStandard.objects.all()
    template = loader.get_template('MathsFun/Standard.html')
    context = {
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))
def detail(request, pk):
    topic = Topic.objects.filter(Topicname = pk)
    return render(request, 'MathsFun/Topic.html', {'topic':topic})
@login_required
def weightage(request):
    wg = Weightage.objects.all()
    return render(request, 'MathsFun/Weightage.html', {'wg':wg})
def About(request):
    return render(request,'MathsFun/About.html')
