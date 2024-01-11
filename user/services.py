from .models import User
from django.utils import timezone
from utils.users import email_validator, email_validator

def create_user(data): 
    email_validator(data.get('email'))
    email_validator(data.get('password'))

    user = User.objects.create(**data, created_at=timezone.now())
    return user
    
