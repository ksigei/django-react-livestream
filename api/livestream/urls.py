from django.urls import path
from rest_framework import routers
from .views import LivestreamViewSet, CommentViewSet, UserListView

router = routers.DefaultRouter()
router.register(r'livestreams', LivestreamViewSet, basename='livestream')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('livestreams/', LivestreamViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('livestreams/<int:pk>/', LivestreamViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('livestreams/<int:pk>/status/', LivestreamViewSet.as_view({
        'get': 'status'
    })),
    path('livestreams/<int:pk>/join/', LivestreamViewSet.as_view({
        'post': 'join'
    })),
    path('livestreams/<int:pk>/leave/', LivestreamViewSet.as_view({
        'post': 'leave'
    })),
    path('livestreams/<int:livestream_pk>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('livestreams/<int:livestream_pk>/comments/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]


urlpatterns += router.urls


