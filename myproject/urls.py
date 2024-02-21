"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views_org
from django.conf import settings
from django.conf.urls.static import static
from crud.views.product_list_view import ProductListView
from crud.views.top_view import TopView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TopView.as_view(), name="top"),
    path('crud/', ProductListView.as_view(), name="list"),
    path('crud/new/',views_org.ProductCreateView.as_view(), name="new"),
    path('crud/edit/<int:pk>', views_org.ProductUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>', views_org.ProductDeleteView.as_view(), name="delete"),
    path('login/', views_org.LoginView.as_view(), name="login"),
    path('logout/', views_org.LogoutView.as_view(), name="logout"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)