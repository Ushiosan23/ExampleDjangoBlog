from django.contrib import admin
from django.urls import path, include
import ExampleBlog.views as views

urlpatterns = [
	# simple pages
	path('', views.start_view, name="page_index"),
	path('services/', views.services_view, name="page_services"),
	path('store/', views.store_view, name="page_store"),
	path('contact/', views.contact_view, name="page_contact"),
	
	# page sections
	path('blog/', include('Blog.urls'), name="blog_page"),
	path('admin/', admin.site.urls, name="admin_page")
]
