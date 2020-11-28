from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views import generic



class HomePage(TemplateView):
    template_name='index1.html'

class MunnarPage(TemplateView):
    template_name='munnar.html'

class AlappuzhaPage(TemplateView):
    template_name='alappuzha.html'

class KannurPage(TemplateView):
    template_name='kannur.html'

class KottayamPage(TemplateView):
    template_name='kottayam.html'

class WayanadPage(TemplateView):
	template_name='wayanad.html'

class ThrissurPage(TemplateView):
	template_name='thrissur.html'

class ConnectPage(LoginRequiredMixin,generic.TemplateView):
	template_name='connect.html'

class TestPage(TemplateView):
    template_name='test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'
