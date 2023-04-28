from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

#class User(AbstractUser):
    #is_seller = models.BooleanField(default=False,null=True)
    #is_buyer = models.BooleanField(default=False,null=True)

class Category(models.Model):
	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length = 150, unique=True ,db_index=True)
	icon = models.FileField(upload_to = "category/")
	create_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name



charitychoice = (("0","0"),("400","400"))

class Book(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
	writer = models.ForeignKey(Writer, on_delete = models.CASCADE,null=True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE,null=True)
	name = models.CharField(max_length = 100,null=True)
	slug = models.SlugField(max_length=100, db_index=True ,null=True)
	price = models.IntegerField(null=True)
	charitypoints = models.CharField(max_length=10,choices=charitychoice,null=True)
	stock = models.IntegerField()
	coverpage = models.FileField(upload_to = "coverpage/",null=True)
	bookpage = models.FileField(upload_to = "bookpage/",null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	totalreview = models.IntegerField(default=1)
	totalrating = models.IntegerField(default=5)
	status = models.IntegerField(default=0)
	description = models.TextField()

	def __str__(self):
	    return self.name

# class User(AbstractUser):
# 	is_seller = models.BooleanField(default=False)

# 	is_buyer = models.BooleanField(default=False)

# 	class Meta:
# 		db_table = 'user'


