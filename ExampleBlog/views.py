from django.http import HttpRequest, HttpResponse
from Config import render_with_extra
import ExampleBlog.page_config as p_config


def extra_config() -> dict:
	"""
	Get extra configuration.
	:return:
	"""
	return {
		"config": p_config.configuration,
		"menu": p_config.menu_page
	}


def start_view(req: HttpRequest) -> HttpResponse:
	"""
	Render index page
	:param req: page request
	:return:
	"""
	return render_with_extra(req, 'page/start.html', extra=extra_config())


def contact_view(req: HttpRequest) -> HttpResponse:
	"""
	Render contact page
	:param req: page request
	:return:
	"""
	return render_with_extra(req, 'page/contact.html', extra=extra_config())


def services_view(req: HttpRequest) -> HttpResponse:
	"""
	Render services page
	:param req: page request
	:return:
	"""
	return render_with_extra(req, 'page/services.html', extra=extra_config())


def store_view(req: HttpRequest) -> HttpResponse:
	"""
	Render store page
	:param req: page request
	:return:
	"""
	return render_with_extra(req, 'page/store.html', extra=extra_config())
