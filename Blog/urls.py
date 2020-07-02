from django.urls import path, re_path
import Blog.views as views

urlpatterns = [
	path('', views.index_view, name="blog_index"),
	
	# login sections
	path('login/', views.login_view, name="blog_login"),
	path('sign_up/', views.sign_up_view, name="blog_sign_up"),
	path('logout/', views.logout_view, name="blog_logout")
]
