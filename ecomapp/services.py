from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .utils import generate_token


def send_activation_email(user):
  email_subject = "Activate Your Account"
  message=render_to_string('activate.html',{
    'user': user,
    'domain': '127.0.0.1:8000',
    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    'token': generate_token.make_token(user)
  })

  print(message)

  email_message = EmailMessage(email_subject, message, to=[user.email])
  email_message.content_subtype = 'html'
  email_message.send()
