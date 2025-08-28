from django.urls import path
from django.views.generic import TemplateView


app_name = 'sistema'
urlpatterns = [     
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('computer/', TemplateView.as_view(template_name='computer.html'), name='computer'),
    path('repuestos/', TemplateView.as_view(template_name='repuestos.html'), name='repuestos'),
    path('accesorios/', TemplateView.as_view(template_name='accesorios.html'), name='accesorios'),
    path('informes/', TemplateView.as_view(template_name='informes.html'), name='informes'),
    ]