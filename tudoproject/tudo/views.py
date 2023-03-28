from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Tasks




class TaskList(LoginRequiredMixin,ListView):
    model= Tasks
    context_object_name='task'
    template_name='TaskList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        return context


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Tasks
    fields=['title','description','complete',]
    success_url=reverse_lazy('task')
    template_name='taskcreate.html'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Tasks
    fields=['title','description','complete',]
    success_url=reverse_lazy('task')
    template_name='taskcreate.html'


class TaskDelete(SuccessMessageMixin, LoginRequiredMixin,DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('task')
    template_name = 'taskdelete.html'
    success_message = 'Deleted succesfully'

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'taskdetail.html'




def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not same!!")
        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account has been successfully created.")

            return redirect("signin")
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=username, password=pass1)
        messages.success(request, ' Logged in successfully.')
        if user is not None:
            login(request, user)
            return redirect('task')
        else:
            return HttpResponse("username or password is incorrect!!!")
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('signin')



def details(request):
    return render(request,'details.html')




















