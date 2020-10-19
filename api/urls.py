from django.urls import path, include

from users.views import UserAuthStage, receive_token
from .router import router

urlpatterns = [
    path('v1/auth/email/', UserAuthStage.as_view(), name='get_uid'),
    path('v1/auth/token/', receive_token, name='send_confirmation_code'),
    path('v1/', include(router.urls)),

]
