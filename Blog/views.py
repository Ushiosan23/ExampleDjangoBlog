from django.http import HttpRequest, HttpResponse
from Config import render_with_extra, merge_dictionaries

import ExampleBlog.page_config as p_config
import Blog.forms as b_forms


def blog_extra() -> dict:
	"""
	Get page configuration
	:return:
	"""
	return {
		"config": p_config.configuration,
		"menu": p_config.menu_blog
	}


def index_view(req: HttpRequest) -> HttpResponse:
	"""
	Render index page
	:param req:
	:return:
	"""
	return render_with_extra(req, "blog/start.html", extra=blog_extra())


def login_view(req: HttpRequest) -> HttpResponse:
	"""
	Render login page
	:param req:
	:return:
	"""
	extra = {
		"form": b_forms.FormLoginModel()
	}
	
	final_extra = merge_dictionaries(extra, blog_extra())
	return render_with_extra(req, "blog/login.html", extra=final_extra)


def sign_up_view(req: HttpRequest) -> HttpResponse:
	"""
	Render sing up
	:param req:
	:return:
	"""
	extra = {
		"form": b_forms.FormSignUpModel()
	}
	
	final_extra = merge_dictionaries(extra, blog_extra())
	return render_with_extra(req, "blog/sign_up.html", extra=final_extra)


def logout_view(req: HttpRequest) -> HttpResponse:
	return HttpResponse("")
