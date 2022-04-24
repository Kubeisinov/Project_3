from django.core.mail import send_mail
from django.shortcuts import render,  redirect
from .models import *
from .forms import AddPostForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView



def kazakh(request):
    c=Address.objects.all()
    c1 = Work.objects.all()

    return render(request,'mainer/project.html', {'address':c,'work':c1})

def kazakh1(request):
    c=Address.objects.all()
    c1 = Work.objects.all()
    return render(request,'mainer/action.html',{'address':c,'work':c1})

def kazakh2(request):
    c=Address.objects.all()
    c1 = Work.objects.all()

    return render(request,'mainer/animation.html',{'address':c,'work':c1})

def kazakh3(request):
    c=Address.objects.all()
    c1 = Work.objects.all()

    return render(request,'mainer/comedy.html',{'address':c,'work':c1})

def kazakh4(request):
    c=Address.objects.all()
    c1 = Work.objects.all()

    return render(request,'mainer/horror.html',{'address':c,'work':c1})

def kazakh5(request):
    c=Address.objects.all()
    c1 = Work.objects.all()

    return render(request,'mainer/ch.html',{'address':c,'work':c1})

def kazakh6(request):
    c=Address.objects.all()
    c1 = Work.objects.all()

    return render(request,'mainer/kz.html',{'address':c,'work':c1})

def kazakh7(request):
    c=Address.objects.all()
    c1 = Work.objects.all()

    return render(request,'mainer/ru.html',{'address':c,'work':c1})

def kazakh8(request):
    c=Address.objects.all()
    c1 = Work.objects.all()

    return render(request,'mainer/us.html',{'address':c,'work':c1})

# class NewsDeleteView(DeleteView):
#     model = info
#     success_url = '/info/'
#     template_name = 'mainer/delete.html'
#
#
# class NewsUpdateView(UpdateView):
#     model = info
#     template_name = 'mainer/update.html'
#     # form_class = InfoForm
#
#
# class NewsDetailView(DetailView):
#     # model = info
#     template_name = 'mainer/details_view.html'
#     context_object_name = 'info'

# def insert(request):
#     error = ''
#     if request.method == 'POST':
#         form = InfoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/info')
#         else:
#             error = 'Форма была неверной'
#     form = InfoForm()
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'mainer/insert.html', data)
#
# def info(request):
#     new = info.objects.order_by('-id')
#     return render(request, 'mainer/info.html', {'info': new})

def registration(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('project')
    else:
        form = AddPostForm()
    return render(request, 'mainer/register.html',{'form': form,'title': 'registration'})

def send_message(request):
    send_mail("Web programming:back end", "My content",
              "200103296@stu.sdu.edu.kz",
              ["200103296@stu.sdu.edu.kz", "abdi56466@mail.ru"],
              fail_silently=False, html_message="Хабарлама жіберілді!")
    return render(request, 'mainer/successfull.html')



