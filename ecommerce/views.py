from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

# Home Page
def home(request):
    # print(request.session.get("first_name", "Unknown"))
    context = {
        "title":"Home"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAHH"
    return render(request, "home.html", context)

# About Page
def about(request):
    context = {}
    return render(request, "about.html", context)

# Contact Page
def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form": contact_form,
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == 'POST':
        # print(request.POST)
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))
    return render(request, 'contact.html', context)

# Login Page
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated)
        if user is not None:
            # print(request.user.is_authenticated)
            login(request, user)
            # context['form'] = LoginForm() clears out form
            return redirect("/")
        else:
            print("Error")
    return render(request, "auth/login.html", context)

# Register Page
User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)