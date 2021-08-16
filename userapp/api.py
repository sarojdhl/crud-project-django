from rest_framework.viewsets import GenericViewSet, mixins
from userapp.models import User
from userapp.serializer import UserSerializer



class UserAPI(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

