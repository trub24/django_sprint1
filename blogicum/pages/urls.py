from django.urls import path
from pages.views import rules
from django.views.generic import TemplateView


app_name = 'pages'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='pages/about.html'),
         name='about'),
    path('rules/', rules, name='rules')
]
