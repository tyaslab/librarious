from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from ..models import Member
from oauth2_provider.contrib.rest_framework import TokenHasScope


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'address')


class MemberListAPIView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        TokenHasScope,
    )
    required_scopes = ('read',)


class MemberCreateAPIView(CreateAPIView):
    serializer_class = MemberSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        TokenHasScope,
    )
    required_scopes = ('write',)


class MemberDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        TokenHasScope,
    )
    required_scopes = ('read', 'write')
