from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from employer.models import Employer
from employer.views import create_user_view, login_view,logout_view,manage_employers,delete_employer,edit_employer
from django.contrib.auth.decorators import login_required

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def display_hierarchy(request):
    return render(request, "employers.html", {'employers': Employer.objects.all()})


@login_required(login_url='login')
def read_employers(request):
    return render(request, "main.html", {'employers': Employer.objects.all()})


def register(request):
    return render(request, "register.html")


urlpatterns = [
    path('', display_hierarchy),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Добавили новый маршрут
    path('signup/', create_user_view, name='signup'),
    path('employers/', read_employers, name='read_employers'),
    path('manage_employers/', manage_employers, name='manage_employers'),
    path('delete-employer/<int:employer_id>/', delete_employer, name='delete_employer'),
    path('edit-employer/<int:employer_edit_id>/', edit_employer, name='edit_employer'),

    path('register/', register),
    # path('create-user/', create_user, name='create_user'),
    # path('', display_hierarchy),
    path('admin/', admin.site.urls),

]
