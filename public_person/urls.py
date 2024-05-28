from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from person import views  # Импортируем представления из приложения person

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', include('person.urls')),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('approval_pending/', views.approval_pending, name='approval_pending'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
