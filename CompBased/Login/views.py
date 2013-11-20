from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.shortcuts import render, redirect
from .forms import ConnectionForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


def connect(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect("home.views.home")

    error = False
    message = ""
    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            message = "valid"
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("home.views.home")
            else:
                error = True
                message = "Invalid credentials"

        else:
            message = "Fields incomplete."
            error = True
    else:
        form = ConnectionForm()

    return render(request, "login/login.html", locals())


def disconnect(request):
    logout(request)
    return redirect("login.views.connect")


def signup_email(request):
    return render_to_response('login/email_signup.html', {}, RequestContext(request))


def validation_sent(request):
    return render_to_response('login/validation_sent.html', {
        'email': request.session.get('email_validation_address')
    }, RequestContext(request))


def require_email(request):
    if request.method == 'POST':
        request.session['saved_email'] = request.POST.get('email')
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)
    return render(request, 'login/email.html', RequestContext(request))# Create your views here.


def register(request):
    error = False
    message = ""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            complete = True
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email)
            user2 = User.objects.filter(username=username)

            if user:
                message = "Email address already in use"
                error = True
            elif user2:
                message = "Username already in use"
                error = True
            else:
                user3 = User.objects.create_user(username, email, password)
                return redirect("login.views.connect")

        else:
            error = True
            message = "Fields incomplete."
    else:
        form = RegistrationForm()
    return render(request, "login/register.html", locals())