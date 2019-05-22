from django.core.exceptions import ValidationError


def checkPassword(password, password_confirmation):
    if(len(password) == 0 and len(password_confirmation) == 0):
        return password
    if len(password) < 8:
        raise ValidationError('Password too short')
    if len(password) != len(password_confirmation):
        raise ValidationError('Passwords don\'t match')
    if False in [password[i] == password_confirmation[i] for i in range(len(password))]:
        raise ValidationError('Passwords don\'t match')
    return password
