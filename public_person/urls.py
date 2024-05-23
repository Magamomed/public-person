from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from django.contrib import admin
from django.urls import path, include
from person.views import add_person, list_persons, signup, login_view, logout_view, person_detail, person_biography, person_works, delete_person

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', include('person.urls')),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/signup/', signup, name='signup'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
