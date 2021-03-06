from django.urls import include, path
from rest_framework import routers

from helloproject.helloapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserInfoView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('users/', views.users),
    path('user/', views.index),
    path('user/<int:pk>/', views.user_by_pk),
    path('user/<uuid:user_id>/', views.user_by_uuid),
    path('user/<str:user_name>/', views.user_by_name),
    path('user/<slug:custom_slug>', views.index_slug),
]
