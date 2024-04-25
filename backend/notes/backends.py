from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class PlaintextAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None