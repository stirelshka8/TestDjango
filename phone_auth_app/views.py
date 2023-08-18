from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .models import UserProfile
import random
import string
import time

# Функция для генерации случайного пригласительного кода
def generate_invite_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def auth_phone(request):
    """
    Аутентификация пользователя по номеру телефона.

    Отправляет пользователю пригласительный код для авторизации.

    Args:
        request (HttpRequest): HTTP-запрос с номером телефона.

    Returns:
        Response: Ответ с сообщением и пригласительным кодом.
    """
    phone_number = request.data.get("phone_number")
    user, created = UserProfile.objects.get_or_create(phone_number=phone_number)

    if created:
        time.sleep(1)  # Имитация задержки для эмуляции отправки кода
        code = "1234"  # Вместо этого следует использовать реальную логику отправки кода
        user.invite_code = generate_invite_code()
        user.save()
        return Response({"message": "Код отправлен на ваш телефон.", "code": code})
    else:
        return Response({"message": "Пользователь уже существует."})

@api_view(['POST'])
def auth_code(request):
    """
    Подтверждение авторизации по пригласительному коду.

    Проверяет, соответствует ли предоставленный код ожидаемому.

    Args:
        request (HttpRequest): HTTP-запрос с номером телефона и кодом.

    Returns:
        Response: Ответ с сообщением о статусе проверки кода.
    """
    phone_number = request.data.get("phone_number")
    code = request.data.get("code")

    user = UserProfile.objects.get(phone_number=phone_number)

    time.sleep(2)  # Имитация задержки для эмуляции проверки кода

    if code == "1234":  # Заменить на реальную логику проверки кода
        return Response({"message": "Код подтвержден."})
    else:
        return Response({"message": "Недействительный код."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_profile(request):
    """
    Получение профиля пользователя.

    Получает информацию о номере телефона и возвращает соответствующий профиль пользователя.

    Args:
        request (HttpRequest): HTTP-запрос с номером телефона.

    Returns:
        Response: Ответ с информацией о профиле пользователя.
    """
    phone_number = request.data.get("phone_number")
    try:
        user = UserProfile.objects.get(phone_number=phone_number)
        return Response({"phone_number": user.phone_number, "invite_code": user.invite_code})
    except UserProfile.DoesNotExist:
        return Response({"message": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def activate_invite(request):
    """
    Активация пригласительного кода.

    Активирует пригласительный код для текущего пользователя.

    Args:
        request (HttpRequest): HTTP-запрос с номером телефона и пригласительным кодом.

    Returns:
        Response: Ответ с сообщением о статусе активации пригласительного кода.
    """
    phone_number = request.data.get("phone_number")
    invite_code = request.data.get("invite_code")

    try:
        user = UserProfile.objects.get(phone_number=phone_number)
        if user.used_invite_codes.count() == 0:
            try:
                invited_user = UserProfile.objects.get(invite_code=invite_code)
                user.used_invite_codes.add(invited_user)
                user.save()
                return Response(
                    {"message": "Пригласительный код активирован.", "activated_invite_code": invited_user.invite_code})
            except UserProfile.DoesNotExist:
                return Response({"message": "Недействительный пригласительный код."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Вы уже активировали пригласительный код."}, status=status.HTTP_400_BAD_REQUEST)
    except UserProfile.DoesNotExist:
        return Response({"message": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def invited_users(request):
    """
    Получение списка пользователей, активировавших пригласительный код.

    Получает информацию о номере телефона пользователя и возвращает список активированных пригласительных кодов.

    Args:
        request (HttpRequest): HTTP-запрос с номером телефона.

    Returns:
        Response: Ответ со списком активированных пригласительных кодов.
    """
    phone_number = request.data.get("phone_number")
    try:
        user = UserProfile.objects.get(phone_number=phone_number)
        invited_users = user.used_invite_codes.all()
        invited_numbers = [invited_user.phone_number for invited_user in invited_users]
        return Response({"invited_users": invited_numbers})
    except UserProfile.DoesNotExist:
        return Response({"message": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)
