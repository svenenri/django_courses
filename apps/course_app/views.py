from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Course

# Views for Courses project.
def index(request):

	# use qSelect to display items in db
	try:
		courseSelect = Course.courseManager.getAllCourses()
		courses = {
			'allCourses': courseSelect,
		}
		return render(request, 'course_app/index.html', courses)
	except:
		return render(request, 'course_app/index.html')

def process(request):
	if request.method == 'POST':
		if request.POST['add']:
			course = request.POST['name']
			description = request.POST['description']
			addCourse = Course.courseManager.addCourse(course, description)
			messages.success(request, addCourse[1])
			return redirect(reverse('courses:courses_index'))
	return redirect(reverse('courses:courses_index'))

def destroy(request, id):
	userID = id
	courseSelect = Course.courseManager.getACourse(userID)
	courses = {
		'allCourses': courseSelect,
	}
	return render(request, 'course_app/destroy.html', courses)

def delete(request, id):
	if request.method == 'POST':
		if 'yes' in request.POST:
			userID = id
			courseDelete = Course.courseManager.delete(userID)
			if courseDelete[0] == True:
				messages.success(request, courseDelete[1])
				return redirect(reverse('courses:courses_index'))
			else:
				messages.error(request, courseDelete[1])
				return redirect(reverse('courses:courses_index'))
		elif 'no' in request.POST:
			return redirect(reverse('courses:courses_index'))
