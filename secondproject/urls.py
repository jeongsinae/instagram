
from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name="home"),
    path('blog/<int:blog_id>',blog.views.detail, name="detail"),
    path('',portfolio.views.portfolio,name="portfolio"),
]   
