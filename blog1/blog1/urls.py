from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include
from first_app import views
from django.conf import settings
urlpatterns = [
    path('',views.allb1,name='home'),

    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('login/create/',views.create,name='create'),
    path('home/allb',views.allb,name='allb'),
    # path('home/about',views.about,name='about'),

    path('admin/', admin.site.urls),
    path('home/blog/<int:Blog_id>',views.detail,name='detail'),
    path('home/index/<int:Index_id>',views.detail1,name='detail1'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
  
