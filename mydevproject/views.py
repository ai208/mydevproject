from django.views.generic import TemplateView

class MenuPageView(TemplateView):
    template_name='menu.html'


class HomePageView(TemplateView):
    template_name='base.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'