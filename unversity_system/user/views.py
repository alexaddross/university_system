from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSerializer


class GetAllStudentsView(APIView):
    def get(self, request):
        queryset = User.objects.all()

        serializer = UserSerializer(instance=queryset, many=True)

        return Response(serializer.data)
