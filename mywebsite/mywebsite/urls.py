"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app001.views import sayhello, hello2, hello3, hello4, dice, employee
import students.views as stdViews
import cookiessessions.views as csViews
import flower.views as fviews
import news.views as newsView

from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render

# 創建一個主頁視圖
def home(request):
    return render(request, "home.html", locals())

urlpatterns = [
    path('admin/', admin.site.urls),
    # app001
    # path('', stdViews.index),
    path('', home),
    path('hello2/<str:username>', hello2),
    path('hello3/<str:username>', hello3),
    path('hello4/<str:username>', hello4),
    path('dice/', dice),
    path('employee/', employee),
    # students app
    path('students/index/', stdViews.index),
    path('students/stdSearch/', stdViews.stdSearch),
    path('students/stdFormModel/', stdViews.stdFormModel),
    path('students/stdForm/', stdViews.stdForm),
    
    path('students/delete/<int:id>', stdViews.delete),
    path('students/edit/<int:id>/',stdViews.edit),
    path('students/edit/<int:id>/<str:mode>',stdViews.edit),
    path('students/edit2/<int:id>/<str:mode>',stdViews.edit2),

    # cookiessessions
    # cookies
    path('set_cookie/<str:key>/<str:value>/',csViews.set_cookie),
    path('get_cookie/<str:key>/',csViews.get_cookie),
    path('set_cookie2/<str:key>/<str:value>/',csViews.set_cookie2),
    path('get_allcookies/', csViews.get_allcookies),
    path('delete_cookie/<str:key>/', csViews.delete_cookie),
    # sessions
    path('set_session/<str:key>/<str:value>/',csViews.set_session),
    path('get_session/<str:key>/',csViews.get_session),
    path('set_session2/<str:key>/<str:value>/',csViews.set_session2),
    path('get_allsessions/', csViews.get_allsessions),
    path('delete_session/<str:key>/', csViews.delete_session),
    # 應用
    path('cookie_session/',csViews.cookie_session),
    path('vote/',csViews.vote),
    path('cookiessessions/login/', csViews.login),
    path('cookiessessions/logout/', csViews.logout),
    # 管理員功能
    path('user_admin/users/', csViews.user_list),
    path('user_admin/users/add/', csViews.add_user),
    path('user_admin/users/manage/', csViews.manage_users),
    path('user_admin/users/edit/<int:user_id>/', csViews.edit_user),

     # allauth URLs
    path('accounts/', include('allauth.urls')),

    # flower 
    path('flower/',fviews.flowers,name='flower'),
    path('flower/<slug:slug>/', fviews.detail, name='detail'), 

    # news app
    path('news/',newsView.index),
    path('news/detail/<int:detail_id>/',newsView.detail,name="detail"),

]
# 處理媒體檔案
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
