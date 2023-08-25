"""
URL configuration for visualizationproject project.

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
from django.urls import path,include
from visualizationapp import views

#API
from visualizationapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.allchart, name='allchart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_delete/<int:id>/', views.dashboard_delete, name='dashboard_delete'),
    path('dashboard_edit/<int:id>/', views.dashboard_edit, name='dashboard_edit'),
    path('filter_dashboard/', views.filter_dashboard, name="filter_dashboard"),
    path('line-chart/', views.line_chart, name='line-chart'),
    path('yearchart/', views.yearchart, name='yearchart'),
    path('doughnutchart/', views.doughnutchart, name='doughnutchart'),
    
]
