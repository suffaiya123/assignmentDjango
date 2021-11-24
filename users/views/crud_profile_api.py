from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.serializers import CreateProfileSerializer, EditProfileSerializer
from users.models import CustomUser


@api_view(["GET", "PUT", "DELETE"])
@permission_classes((AllowAny,))
def crud_user_api(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response({"data": [], "message": "User does not exist"}, 404)

    if request.method == "GET":
        serializer = CreateProfileSerializer(user)
        return Response({"data": serializer.data, "message": "view_profile"}, 200)

    if request.method == "PUT":
        serializer = EditProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "edit_profile"}, 200)

        return Response(
            {"data": serializer.errors, "message": serializer.error_messages}, 400
        )

    elif request.method == "DELETE":
        user.delete()
        return Response({"data": [], "message": "User deleted"}, 204)
