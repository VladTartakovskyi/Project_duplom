from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import AddPostForm, RegisterUserForm, LoginUserForm, UnemployedF
from .utils import *



class VacanciesHome(DataMixin,ListView):
    paginate_by = 3
    model = Vacancies
    template_name = 'vacancies/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Головна сторінка")
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        context['menu'] = user_menu
        if not self.request.user.is_superuser:
            user_menu.pop(1)
        context['menu'] = user_menu
        return dict(list(context.items()) + list(c_def.items()))




def about(request):
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(2)
    return render(request, 'vacancies/about.html', {'menu': user_menu, 'title': 'Про сайт'})







class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'vacancies/post.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавлення вакансії'
        context['menu'] = menu
        return context

def contact(request):
    if request.method == 'POST':
        form = UnemployedF(request.POST)

        user_menu = menu.copy()
        if not request.user.is_superuser:
            user_menu.pop(1)
        if form.is_valid():

            try:
                Unemployed.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Помилка добавлення')

    else:
        form = UnemployedF()

    return render(request, 'vacancies/contact.html', {'form': form, 'menu': menu, 'title': 'Добавлення даних про користувача'})





def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')


def show_post(request, post_id):
    post = get_object_or_404(Vacancies, pk=post_id)



    context = {
        'post': post,
        'menu': menu,
        'title': post.posada,
        'cat_selected': post.pr_id,
    }

    return render(request, 'vacancies/post.html', {'title': 'Добавити дані про себе'})


def show_profession(request, pr_id):

    posts = Vacancies.objects.filter(pr_id=pr_id)

    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(2)
    context = {
        'posts': posts,
        'menu': user_menu,
        'title': 'Відображення по професіях',
        'cat_selected': pr_id,
    }


    return render(request, 'vacancies/index.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'vacancies/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'vacancies/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизація")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return  reverse_lazy('home')


def logout_user(request):
    logout(request)
    return  redirect('login')


class Search(ListView):
    model = Vacancies
    template_name = 'vacancies/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Vacancies.objects.filter(city=self.request.GET.get("search"))


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search"] = self.request.GET.get("search")

        user_menu = menu.copy()
        if not self.request.user.is_superuser:
            user_menu.pop(2)
        context['menu'] = user_menu
        return context



class Sear(ListView):
    model = Vacancies
    template_name = 'vacancies/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Vacancies.objects.filter(salary=self.request.GET.get("sear"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["sear"] = self.request.GET.get("sear")

        user_menu = menu.copy()
        if not self.request.user.is_superuser:
            user_menu.pop(2)
        context['menu'] = user_menu
        return context
