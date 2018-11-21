"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from collection import views

urlpatterns = [
    path('', views.index, name='home'),
    path('htmlcss/', TemplateView.as_view(template_name='htmlcss.html'), name='htmlcss'),
    path('django/', TemplateView.as_view(template_name='django.html'), name='django'),
    path('ruby/', TemplateView.as_view(template_name='ruby.html'), name='ruby'),
    path('javascript/', TemplateView.as_view(template_name='javascript.html'), name='javascript'),
    path('python/', TemplateView.as_view(template_name='python.html'), name='python'),
    path('books/<slug>/', views.book_detail, name='book_detail'),
    path('books/<slug>/edit', views.edit_book, name='edit_book'),
    path('admin/', admin.site.urls),
]
