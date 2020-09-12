from django.core.validators import RegexValidator
from django.utils.regex_helper import _lazy_re_compile


phone_no_validator = RegexValidator(
    _lazy_re_compile(r'^0[0-9]{9}\Z'),
    message='Enter a valid phone number (it must start with 0 and be 10 characters long).',
    code='invalid',
)
