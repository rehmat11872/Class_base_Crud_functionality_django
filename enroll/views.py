from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import *
from .forms import StudentAddForm
from .models import *
from django.urls import reverse, reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = 'enroll/home.html'
    model = Student

    def get_context_data(self, **kwargs):
        kwargs = super(HomeView, self).get_context_data(**kwargs)
        kwargs['form'] = StudentAddForm()
        kwargs['students'] = Student.objects.all()
        return kwargs

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = StudentAddForm(request.POST)
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            student = Student.objects.create(name=name, email=email, password=password)
            messages.success(request, "success")
            return redirect('home')
        else:
            form = StudentAddForm()
            messages.error(request, 'Invalid')
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, 'enroll/home.html', context)
            

class UpdateStudentView(UpdateView):
    template_name = 'enroll/home.html'
    fields = ['name', 'email', 'password']
    model = Student

    def get_success_url(self):
        return reverse('home')         


class DeleteStudentView(DeleteView):
    template_name = 'enroll/home.html'
    model = Student

    def get_success_url(self):
        return reverse('home')