import logging
import threading

from django.shortcuts import redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from config import settings
from .models import User
from django.views.generic import TemplateView
from .tokens import account_activation_token


# 이메일 인증
class EmailAuthView(TemplateView):
    logger = logging.getLogger(__name__)
    template_name = 'email/email_complete.html'

    def get(self, *args, **kwargs):
        uid = force_bytes(urlsafe_base64_decode(kwargs['uid64']))
        token = kwargs['token']

        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            user = None

        if user.is_staff or user is not None and account_activation_token.check_token(user, token):
            user.email_auth = True
            user.save()
        return redirect('login')

    def post(self, request, *args, **kwargs):
        user = User.objects.get(user_id=request.user_id)

        message = render_to_string('email/email-auth-message.txt', {
            'protocol': 'http',
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })

        # email 전송
        email = EmailThread(subject='TopAIs 이메일 인증', message=message, from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[user.email]).start()

        return email


# 비동기로 이메일 전송
class EmailThread(threading.Thread):
    def __init__(self, subject, message, from_email, recipient_list, fail_silently=False, html=None):
        self.subject = subject
        self.message = message
        self.from_email = from_email
        self.recipient_list = recipient_list
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(self.subject, self.message, self.from_email, to=self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        msg.send(self.fail_silently)
