from django.shortcuts import render

# Create your views here.
def index(request):
	print "asdasdada"
	return render(request, 'cloudmanufacturing/index.html')
	#return HTTPresponse("asdasd");