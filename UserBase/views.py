
from .models import User
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.response import Response

from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PATCH', 'DELETE'])
def user_id(request, no):

    try:
        part = User.objects.get(PhoneNo=no)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = UserSerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_access(request, token):

    try:
        part = User.objects.get(AccessToken=token)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(part)
        return Response(serializer.data)


"""
@csrf_exempt
def new_user(request):

    if request.method == 'POST':
        u = User.objects.create_user(request.POST.get('phone'), request.POST.get('email'), request.POST.get('password') )
        u.last_name = request.POST.get('last')
        u.first_name = request.POST.get('first')
        u.AvgRating = request.POST.get('rating')
        u.n = request.POST.get('n')
        u.save()

        return HttpResponse("Successfully registered")

@csrf_exempt
def user_login(request):

    username = request.POST.get('phone')
    password = request.POST.get('password')
    u = authenticate(request, username=username, password=password)
    if u is not None:
        login(u, request)
        return HttpResponse("Successfully login")
    else:
        return HttpResponse("Invalid Login")


"""




