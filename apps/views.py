from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.serializers import UserSerializer
from drf_spectacular.utils import extend_schema


class TelegramApiView(APIView):
    serializer_class = UserSerializer

    @extend_schema(
        request=UserSerializer,
        responses={201: UserSerializer},
        tags=['Telegram Auth'])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
