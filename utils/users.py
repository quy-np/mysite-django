import re

from django.core.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email
    
def email_validator(email): 
    # regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    # if re.fullmatch(regex, email):
    #     return True
    # else:
    #     return False
    try:
        django_validate_email(email)
    except ValidationError:
        raise ValidationError('Invalid email address')
    

def email_validator(password):
    regex = r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$'
    
    if re.match(regex, password):
        return True
    else: 
        raise ValidationError('Password must contain at least one letter, one number, and be at least 8 characters long')