from __future__ import unicode_literals
from django.db import models

# Logic and Db for Courses project
# ManageCourse class?
class ManageCourse(models.Manager):
	# Get all courses.
	def getAllCourses(self):
		allCourses = self.all()
		return allCourses

	# Get a course by <id>.
	def getACourse(self, id):
		courseGet = self.filter(id = id)
		return courseGet

	# Add a course. Name and info passed in.
	def addCourse(self, name, info):
		self.create(course_name = name, description = info)
		confirmMsg = name + ' has been successfully added.'
		# Tuple with bool added for use with functionality to be added later where the length of course_name passed in by user is checked for valid length < 50 char.
		confirm = (True, confirmMsg)
		return confirm

	# Delete a course by <id>
	def delete(self, id):
		try:
			self.filter(id = id).delete()
			confirm = (True, 'This course has been successfully deleted.')
			return confirm
		except:
			confirm = (False, 'Course not found.')
			return confirm

class Course(models.Model):
	course_name = models.CharField(max_length=50)
	description = models.TextField(default= "Description")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	courseManager = ManageCourse()

	def __str__(self):
		return self.course_name
