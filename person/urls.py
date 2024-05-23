from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import add_person, list_persons, signup, login_view, logout_view, person_detail, person_biography, person_works, delete_person

urlpatterns = [
    path('add/', add_person, name='add_person'),
    path('list/', list_persons, name='list_persons'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<int:pk>/', person_detail, name='person_detail'),
    path('<int:pk>/biography/', person_biography, name='person_biography'),
    path('<int:pk>/works/', person_works, name='person_works'),
    path('<int:pk>/delete/', delete_person, name='delete_person'),
]
