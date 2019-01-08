from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from ..models import Borrowing
from oauth2_provider.contrib.rest_framework import TokenHasScope


class BorrowingSerializer(ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ('id', 'code', 'member', 'book', 'due_date', 'back_date')


class BorrowingListAPIView(ListAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        TokenHasScope,
    )
    required_scopes = ('read',)


class BorrowingCreateAPIView(CreateAPIView):
    serializer_class = BorrowingSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        TokenHasScope,
    )
    required_scopes = ('write',)


class BorrowingDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        TokenHasScope,
    )
    required_scopes = ('read', 'write')
