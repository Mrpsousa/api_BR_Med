from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app_main.urls')),
]



# from django.conf.urls import url
# from django.conf.urls import url, include
# from django.urls import path, include

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Melhor Envio API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact_generic@email.com"),
#       license=openapi.License(name="Test License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )


# urlpatterns = [
#     url(r'^api/', include('teste.urls')),
#     path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path("redoc", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ] 