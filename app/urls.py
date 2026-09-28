from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("show/", views.funtionname, name="show"),
    path("home/", views.home, name="home"),
    path("update/<int:pk>/", views.update_name, name="update"),
    path("delete/<int:pk>/", views.delete_name, name="delete"),
    path("add/", views.add_product, name="add"),
    path('car/<int:pk>/', views.single_car, name='single_car')

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)