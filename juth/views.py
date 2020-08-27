from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException


# TODO: write a serializer
# TODO: Raise custom exceptions
# TODO: Add "logout", "password_change" and "password_reset"
@api_view(['POST'])
def xhr_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        user = authenticate(username=username, password=password)
        if not user:
            raise APIException('Wrong username and/or password')
        if not user.is_active:
            raise APIException('User is not active')
        login(request, user)
        name = user.first_name + user.last_name

        return JsonResponse({
            'id': user.id,
            'name': name,
            'groups': [g.name for g in user.groups.all()]
        })

    return HttpResponseBadRequest()
