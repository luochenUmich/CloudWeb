from django.shortcuts import render
from azure.storage import BlobService
from django.core.mail import send_mail
# Create your views here.


def index(request):
	return render(request, 'cloudmanufacturing/index.html')

def data(request):
	# blob_service = BlobService(account_name='cloudmanufaturing', 
	# account_key='Uan008l1ORwlMs7V/SqLH5fbuhEEA0CSYQBGfnT69634txKae+gh5164yltivm/h6ej6JlZ8cibmdjDgPyJ+4g==')
	# blob_service.get_blob_to_path(
	# 	'testcontainer', 
	# 	'test.dat', 
	# 	'localtest.dat')
	# download_file = open('localtest.dat', 'r')
	# str = download_file.read(10);
	# #send_mail('test_azure', 'test', 'luochen@umich.edu', ['luochen@umich.edu'])
	# context = {'data': str}
	if 'last_download_time' not in request.session.keys():
		request.session['']
	select 
	return json()

def send_email(request):
	send_email()