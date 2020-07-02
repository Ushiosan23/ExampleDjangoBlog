import django.forms as forms

# attributes
f_attrs = {
	"pass_attr": {
		"type": "password"
	},
	"pass_auto_focus": {
		"autofocus": ""
	},
	"auto_focus_attr": {
		"autofocus": ""
	}
}


class FormLoginModel(forms.Form):
	"""
	Login form model
	"""
	
	def __init__(self, *args, **kwargs):
		"""
		Initialize object
		:param args:
		:param kwargs:
		"""
		kwargs.setdefault('label_suffix', '')
		super(FormLoginModel, self).__init__(*args, **kwargs)
	
	# user input
	input_user = forms.CharField(max_length=120, label="User", widget=forms.TextInput(f_attrs["auto_focus_attr"]))
	
	# password input
	input_password = forms.CharField(label="Password", widget=forms.TextInput(f_attrs["pass_attr"]))


class FormSignUpModel(forms.Form):
	"""
	Register form model
	"""
	
	def __init__(self, *args, **kwargs):
		"""
		Initialize object with default properties
		:param args:
		:param kwargs:
		"""
		kwargs.setdefault('label_suffix', '')
		super(FormSignUpModel, self).__init__(*args, **kwargs)
	
	# nick name
	input_nick = forms.CharField(max_length=120, label="Nick name", widget=forms.TextInput(f_attrs["auto_focus_attr"]))
	
	# email
	input_email = forms.EmailField(max_length=255, label="Email")
	
	# password
	input_password = forms.CharField(label="Password", widget=forms.TextInput(f_attrs["pass_attr"]))
	
	# repeat
	input_password_repeat = forms.CharField(label="Repeat password", widget=forms.TextInput(f_attrs["pass_attr"]))
