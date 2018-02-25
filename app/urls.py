from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.frontpage),
    url(r'^settings$', views.settings),
    url(r'^add_category$', views.add_category),
    url(r'^delete_category/(?P<category>\w+)', views.deleteCategory),
    url(r'^add_record$', views.addRecord),
    url(r'^delete_record$', views.deleteRecord),
]
