
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from APIapp import api_views as v
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='api-login'),
    path('classroomlist/', v.APIListView.as_view(), name='api-classroom-list'),
    path('classroom/<int:classroom_id>detail', v.DetailView.as_view(), name='api-classroom-detail'),
    path('classroom/', v.CreateView.as_view(), name='api-classroom-create'),
    path('classroom/<int:classroom_id>/update', v.UpdateView.as_view(), name='api-classroom-update'),
    path('classroom/<int:classroom_id>/delete', v.DeleteView.as_view(), name='api-classroom-delete'),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
