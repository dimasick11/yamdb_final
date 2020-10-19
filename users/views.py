import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from api_yamdb.settings import EMAIL_HOST_USER, logger
from .permissions import IsAdmin
from .serializers import UserSerializer, ReceiveTokenSerializer, MailSerializer

User = get_user_model()


class UserAuthStage(APIView):
    @staticmethod
    def custom_random_pass(string_length=10):
        random_pass = str(uuid.uuid4())
        random_pass = random_pass.upper().replace("-", "")
        return random_pass[0:string_length]

    def post(self, request):
        logger.info('Inside get_pass')
        serializer = MailSerializer(data=request.data)
        user_email = request.data.get('email', None)
        if serializer.is_valid():

            if not user_email:
                return Response('Cant receive E-Mail address', status.HTTP_400_BAD_REQUEST)

            pass_code = self.custom_random_pass(8)
            try:
                User.objects.get(email=user_email)
            except User.DoesNotExist:
                User.objects.create(email=user_email)
            User.objects.filter(email=user_email).update(confirmation_code=make_password(
                pass_code, salt=None, hasher='default'))

            send_mail('Yamdb Access code', f'confirmation_code: {pass_code}', EMAIL_HOST_USER, [user_email])
            logger.info(f'From {EMAIL_HOST_USER} sent greeting mail to {user_email}')

            return Response(f"Confirmation code's sent successful", status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def receive_token(request):
    serializer = ReceiveTokenSerializer(data=request.data)
    if serializer.is_valid():
        user_email = serializer.data.get('email')
        confirmation_code = serializer.data.get('confirmation_code')
        user = get_object_or_404(User, email=user_email)
        if check_password(confirmation_code, user.confirmation_code):
            new_token = AccessToken.for_user(user)
            return Response({'token': f'{new_token}'}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', ]

    @action(detail=False, methods=['patch', 'get'], permission_classes=[IsAuthenticated], )
    def me(self, request):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if request.method == 'GET':
                return Response(serializer.data, status=status.HTTP_200_OK)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
