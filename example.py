import re

from rest_framework.exceptions import ValidationError


class PasswordValidator:

    def __call__(self, value):

        pattern = re.compile('(?=.*[A-Z]{1})'
                             '(?=.*[a-z]{1})'
                             '(?=.*[0-9]{1})'
                             '(?=.*[!@#]{1}){8,20}')
        if not pattern.match(value):
            raise ValidationError('Ошибка!')
        return value


pattern = re.compile([1-9])

