from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.serializers import CreateProfileSerializer


@api_view(["POST"])
@permission_classes((AllowAny,))
def create_user_api(request):
    data = request.data
    try:
        if len(data["phone_number"]) != 10:
            raise Exception
        phone_number = int(data["phone_number"])
    except:
        return Response({"data": [], "message": "Invalid phone Number"}, 400)

    serializer = CreateProfileSerializer(
        data=data, context={"phone_number": phone_number}
    )
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data, "message": "create_profile"}, 201)

    return Response(
        {"data": serializer.errors, "message": serializer.error_messages}, 400
    )
