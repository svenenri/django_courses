from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	course_name = models.CharField(max_length=50)
	description = models.TextField(default= "Description")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.course_name

# class Description(models.Model):
# 	info = models.TextField()
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)
#
# 	def __str__(self):
# 		return self.info


"""
	courseDescrip = models.OneToOneField(Course, default=1, related_name='details')
"""
