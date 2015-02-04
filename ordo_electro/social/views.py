from social.models import Account
from rest_framework import viewsets
from social.serializers import AccountSerializer



class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer