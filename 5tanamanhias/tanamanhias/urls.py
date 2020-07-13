"""tanamanhias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views
from store import views as storeViews
from users import views as usersViews

urlpatterns = [
    url(r'^artikel/', include('artikel.urls', namespace='artikel')),
    url(r'^store/', include('store.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.loginView, name = 'login'),
    url(r'^logout/$', views.logoutView, name = 'logout'),

    url(r'^$', views.index, name='index'),
    url(r'^profile/',include('users.urls'),name = 'profile'),
    url(r'^cart/',include('store.urls')),
    url(r'^checkout/',include('store.urls')),
    url(r'^update_item/$',storeViews.updateItem,name='update_item'),
    url(r'^process_order/$',storeViews.processOrder,name='process_order'),

     url(r'^register/$',views.registerView,name='register'),

    url(r'^register/register$',views.registerView,name='register'),

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
