from django.template import loader
from .models import AllStandard, Topic, Weightage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User

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

def search(request):

        srch='class 9'
        post = AllStandard.objects.all().filter(standardname=srch)
        return render(request, 'MathsFun/search.html', {'post':post})

def success(request, uid):
    template = render_to_string('Mathsfun/newsletter.html', {'name': request.user.email})
    email = EmailMessage(
      "Hi Senpai,from team jarvis",
      template,
      settings.EMAIL_HOST_USER,
      [request.user.email],
    )

    email.fail_silently = False
    email.send()

    project = User.objects.get(id=uid)

    return render(request, 'MathsFun/news.html', {'project':project})
