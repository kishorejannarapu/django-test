from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class LdapAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print("login middleware")
        user = MyCustomUser('kishore')
        return (user, None)


from django.contrib.auth.models import User


class MyCustomUser(User):
    def __str__(self):
        return f'{self.username}'


from django.contrib.auth.models import Permission


class MyCustomPermission(Permission):
    label = 'Access specific feature'
    codename = 'access_feature'

    def has_permission(self, user, obj):
        # Return True if user has access to the specific feature within the object
        # based on your custom logic, e.g., checking object attributes or relationships.
        return obj.is_active and user.is_staff
