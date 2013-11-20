# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from social.backends.google import GooglePlusAuth
from django.conf import settings
from django.contrib.auth.decorators import login_required


# @login_required(login_url="login.views.connect")
# def home(request):
    # request.session['messages'] = PrivateMessage.objects.filter(receiver=request.user, viewed=False).count()
    # return redirect("sections.newsfeed.views.newsfeed")

@login_required(login_url="login.views.connect")
def home(request):
    """Login complete view, displays user data"""
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    return render(request, 'home/done.html', {
        'user': request.user,
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope })
