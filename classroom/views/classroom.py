from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


@login_required
def home(request):
    if request.user.is_teacher:
        return redirect(reverse('teachers:quiz_change_list'))
    else:
        return redirect(reverse('students:quiz_list'))
