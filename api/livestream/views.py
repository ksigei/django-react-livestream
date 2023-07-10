from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Livestream, Comment
from .serializers import LivestreamSerializer, CommentSerializer, UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LivestreamViewSet(viewsets.ModelViewSet):
    queryset = Livestream.objects.all()
    serializer_class = LivestreamSerializer
    
    @action(detail=True, methods=['GET'])
    def status(self, request, pk=None):
        livestream = self.get_object()
        # Implement logic to check the livestream status (e.g., ongoing, ended)
        # Return the status as a response
        return Response({'status': 'ongoing'})
    
    @action(detail=True, methods=['POST'])
    def join(self, request, pk=None):
        livestream = self.get_object()
        user_id = request.data.get('user_id')
        if user_id:
            user = get_object_or_404(User, pk=user_id)
            livestream.viewers.add(user)
            return Response({'message': 'Joined the livestream'})
        else:
            return Response({'error': 'User ID is required'}, status=400)

    @action(detail=True, methods=['POST'])
    def leave(self, request, pk=None):
        livestream = self.get_object()
        user_id = request.data.get('user_id')
        if user_id:
            user = get_object_or_404(User, pk=user_id)
            livestream.viewers.remove(user)
            return Response({'message': 'Left the livestream'})
        else:
            return Response({'error': 'User ID is required'}, status=400)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        livestream_id = self.kwargs['livestream_pk']
        livestream = get_object_or_404(Livestream, pk=livestream_id)
        serializer.save(user=self.request.user, livestream=livestream)
