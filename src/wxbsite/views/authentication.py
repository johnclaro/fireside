from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login as auth_login, 
    logout as auth_logout
)
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import get_user_model

from src.wxbsite.forms import SignupForm, LoginForm
from src.wxbsite.mailgun import Mailgun
from src.wxbsite.tokens import account_activation_token
from src.wxbsite.models import Profile


User = get_user_model()
mailgun = Mailgun(settings.MAILGUN_API_KEY)


def signup(request):
    if request.user.is_authenticated:
        return redirect('wxbsite:dashboard')

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            profile = Profile.objects.create(user=user)
            profile.save()

            message = render_to_string(
                'authentication/email/confirm_account.html',
                {
                    'user': user,
                    'domain': get_current_site(request),
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                }
            )
            recipient = form.cleaned_data.get('email')
            response = mailgun.send_simple_message(
                'Confirm your account', 
                message, 
                [recipient]
            )

            auth_login(request, user, backend='src.wxbsite.backends.EmailAuth')
            return redirect('wxbsite:home')
    else:
        form = SignupForm()

    return render(request, 'authentication/signup.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('wxbsite:dashboard')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                auth_login(request, user, backend='src.wxbsite.backends.EmailAuth')
                return redirect('wxbsite:home')
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('wxbsite:home')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and account_activation_token.check_token(user, token):
        user.profile.is_confirmed = True
        user.profile.save()
        auth_login(request, user, backend='src.wxbsite.backends.EmailAuth')
        messages.success(request, 'Thank you for confirming your email')
        return redirect('wxbsite:home')
    else:
        messages.error(request, 'Activation link is invalid')
        return redirect('wxbsite:login')
