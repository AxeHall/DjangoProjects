from django.conf import settings
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path, include
from main.views import RegistrationView
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("login/", LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="main/logout.html"), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("reservation/", include("reservation.urls"))
]


""" urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("reservation/", include("reservation.urls")),
    path("login/", LoginView.as_view(template_name="main/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="main/logout.html"), name="logout"
    ),
    path("registration/", RegistrationView.as_view(), name="registration"),
]
 """

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
