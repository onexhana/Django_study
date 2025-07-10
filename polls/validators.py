# polls/validators.py

from django.core.exceptions import ValidationError

def validate_com(value):
    if not value.endswith('.com'):
        raise ValidationError('이메일 주소는 .com으로 끝나야 합니다.')
