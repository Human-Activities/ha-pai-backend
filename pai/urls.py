from django.urls import path
from .views import add_user_to_group, get_group_link
urlpatterns = [
    path('joinmygroup/<str:randomstring>', add_user_to_group, name="add_user_to_group"),
    path('grouplink/<str:group_uuid>/', get_group_link, name='get_group_link'),
]
