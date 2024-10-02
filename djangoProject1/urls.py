
from django.contrib import admin
from django.urls import path
from posts import views
from posts.views import post_list_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/posts', views.post_list_api_view),
    path('api/v1/posts/<int:id>/', views.post_detail_api_view)


]
