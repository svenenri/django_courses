from django.shortcuts import render, redirect, HttpResponse

from .models import Course

# Create your views here.
def index(request):

	# use qSelect to display items in db
	try:
		courseSelect = Course.objects.all()
	except:
		return render(request, 'course_app/index.html')

	courses = {
		'allCourses': courseSelect,
	}

	return render(request, 'course_app/index.html', courses)

def process(request):
	"""

	Need to resolve description One-to-One relationship issue. Not able to traverse from Course to Description info using related_name

	"""
	if request.method == 'POST':
		if request.POST['add']:
			course = request.POST['name']
			description = request.POST['description']
			# use qAdd
			qAddCourse = Course.objects.create(course_name = course, description = description)
			# qAddDescription = Description.objects.create(info = description)
			return redirect('/')

	return redirect('/')

# Need to add id variable to destroy
def destroy(request, id):
	courseSelect = Course.objects.filter(id = id)
	# descriptionSelect = Description.objects.filter(id = id)
	courses = {
		'allCourses': courseSelect,
	}
	return render(request, 'course_app/destroy.html', courses)

def delete(request, id):
	if request.method == 'POST':
		if 'yes' in request.POST:
			courseDelete = Course.objects.filter(id = id).delete()
			# descriptionDelete = Description.objects.filter(id= id).delete()
			return redirect('/')
		elif 'no' in request.POST:
			return redirect('/')
