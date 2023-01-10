from rest_framework.viewsets import ModelViewSet
from ..serializers import UserSerializer
from ..models import User


class UserViewSet(ModelViewSet):
    
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    # def retrieve(self, request, *args, **kwargs):

    #     params = kwargs
    #     name = params['pk']
    #     print(params)

    #     users = User.objects.filter(name__icontains=name)
    #     serializer = UserSerializer(users, many=True)

    #     return Response(serializer.data)
