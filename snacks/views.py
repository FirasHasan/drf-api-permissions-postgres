from rest_framework import generics
from .models import snacks
from .serializers import snacksSerializer
from .permissions import IsOwnerOrReadOnly

class snacksList(generics.ListCreateAPIView):
    queryset = snacks.objects.all()
    serializer_class = snacksSerializer
    
class snacksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = snacks.objects.all()
    serializer_class = snacksSerializer
    permission_classes = (IsOwnerOrReadOnly,)