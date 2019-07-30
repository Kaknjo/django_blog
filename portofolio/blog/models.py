from django.db import models

# Create your models here.


class Category(models.Model):
	name=models.CharField(max_length=70)


class Post(models.Model):
	title=models.CharField(max_length=50)
	sadrzaj=models.TextField()
	 # auto_now_add=true postavlja vrijeme kada se objekat instancira
	created_on=models.DateTimeField(auto_now_add=True)
	 # auto_now=true postavlja trenutno vrijeme kada god se updatuje objekat
	last_edited=models.DateTimeField(auto_now=True) 
	categories=models.ManyToManyField('Category', related_name='posts')


class Comment(models.Model):
	author=models.CharField(max_length=70)
	sadrzaj=models.TextField()
	created_on=models.DateTimeField(auto_now_add=True)
	post=models.ForeignKey('Post', on_delete=models.CASCADE)


