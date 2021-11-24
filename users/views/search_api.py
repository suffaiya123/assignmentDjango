from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.serializers import CreateProfileSerializer, EditProfileSerializer
from users.models import CustomUser
from django.db.models import Q


@api_view(["GET"])
@permission_classes((AllowAny,))
def search_view(request):
    name = request.GET.get("name")
    if name is None or name == "":
        name = None
    print(name)
    user_objs = CustomUser.objects.filter(
        Q(first_name__icontains=name) | Q(last_name__icontains=name)
    )
    print(user_objs)
    serializer = EditProfileSerializer(user_objs, many=True)
    return Response({"data": serializer.data, "message": "search by name"}, 200)