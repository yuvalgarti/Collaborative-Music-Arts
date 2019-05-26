from django.core.exceptions import ValidationError
from django.shortcuts import redirect


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

def editUser(currUser,newUser):
    currUser.__setattr__('email', newUser.email)
    currUser.__setattr__('first_name', newUser.first_name)
    currUser.__setattr__('last_name', newUser.last_name)
    if len(newUser.password) > 0:
        currUser.set_password(newUser.password)
        redirection = redirect('login')
    else:
        redirection = redirect('profile', username=currUser.username)
    currUser.save()
    return redirection
