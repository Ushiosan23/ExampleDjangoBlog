from django.contrib import admin
from Blog import models


@admin.register(models.UserModel)
class AdminUserModel(admin.ModelAdmin):
	"""
	User administrator model
	"""
	
	list_display = ('id', 'name', 'nick', 'email')
	list_display_links = ('id', 'name', 'nick', 'email')
	search_fields = ('nick', 'email')


@admin.register(models.TagModel)
class AdminTagModel(admin.ModelAdmin):
	"""
	Tag administrator model
	"""
	
	list_display = ('id', 'name')
	list_display_links = ('id', 'name')
	search_fields = ('name',)


@admin.register(models.ArticleModel)
class AdminArticleModel(admin.ModelAdmin):
	"""
	Article administrator model
	"""
	
	list_display = ('id', 'title', 'draft')
	list_display_links = ('id', 'title')
	search_fields = ('title',)
