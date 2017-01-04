from django.conf.urls import url

from.import views

urlpatterns = [
	url(r'^blog/', views.index, name='index'),
	url(r'^', views.home, name='home'),
]