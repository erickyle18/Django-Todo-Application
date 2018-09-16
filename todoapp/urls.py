from django.contrib import admin
from django.urls import path
from todoapp import views
from django.conf.urls import url

app_name = 'todoapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$',views.IndexView.as_view(),name='index'),
    # todoapp/1
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail')
    
]
