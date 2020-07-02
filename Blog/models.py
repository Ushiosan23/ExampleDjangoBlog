from django.contrib.auth.hashers import make_password
from django.db import models


class UserModel(models.Model):
	"""
	User model in db
	"""
	
	# user complete name
	name = models.TextField(name="name", verbose_name="User name")
	# user nick name
	nick = models.CharField(max_length=255, unique=True, name="nick", verbose_name="User nick")
	# user email
	email = models.EmailField(unique=True, name="email", verbose_name="User email")
	# user password
	password = models.CharField(max_length=255, name="password", verbose_name="User password")
	
	def __str__(self):
		"""
		Get table name
		:return:
		"""
		return f"{self.id} | {self.nick} ({self.email})"
	
	@staticmethod
	def crypt_password(password: str) -> str:
		"""
		Make user password
		:param password:
		:return:
		"""
		return make_password(password)
	
	class Meta:
		"""
		Meta user model class
		"""
		verbose_name = "User"
		verbose_name_plural = "Users"


class TagModel(models.Model):
	"""
	Tag class model in db
	"""
	
	# tag name
	name = models.CharField(max_length=120, unique=True, name="name")
	
	def __str__(self):
		"""
		Get table name
		:return:
		"""
		return self.name
	
	class Meta:
		"""
		Meta tags model class
		"""
		verbose_name = "Tag"
		verbose_name_plural = "Tags"


class ArticleModel(models.Model):
	"""
	Article class model in db
	"""
	
	# article user foreign key
	user_ref = models.ForeignKey(UserModel, on_delete=models.CASCADE, name="ref", verbose_name="Article User reference")
	# article title
	title = models.CharField(max_length=255, name="title", verbose_name="Article title")
	# article description
	description = models.TextField(max_length=300, name="description", verbose_name="Article description")
	# article draft
	draft = models.BooleanField(default=True, name="draft", verbose_name="Article draft")
	# article content
	content = models.TextField(name="content", verbose_name="Article content")
	
	def __str__(self) -> str:
		"""
		Get article name
		:return:
		"""
		return f"{self.title}"
	
	class Meta:
		"""
		Meta articles model class
		"""
		verbose_name = "Article"
		verbose_name_plural = "Articles"
