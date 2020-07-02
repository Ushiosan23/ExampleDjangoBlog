from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def merge_dictionaries(one: dict, two: dict) -> dict:
	"""
	Merge 2 dictionaries
	:param one:
	:param two:
	:return:
	"""
	d_final = one.copy()
	d_final.update(two)
	
	return d_final


def render_with_extra(req: HttpRequest,
					  template_name: str,
					  context: dict = None,
					  content_type: str = None,
					  status: int = None,
					  using=None,
					  extra: dict = None) -> HttpResponse:
	"""
	Render page with configuration page
	:param req:
	:param template_name:
	:param context:
	:param content_type:
	:param status:
	:param using:
	:param extra:
	:return:
	"""
	
	if context is None:
		context = {}
	if extra is None:
		extra = {}
	
	final_context = merge_dictionaries(extra, context)
	return render(req, template_name, final_context, content_type, status, using)
