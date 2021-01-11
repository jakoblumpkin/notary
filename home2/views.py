from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Review
from datetime import datetime
# Create your views here.

def home(request):
    last3items=list(Review.objects.all())[-3:]
    context={"last3items":last3items}
    return render(request, 'index.html', context)


#this send email to customer everytime some one some feel out the contact Us Section
def sendmail(request):
    document = request.POST['document']
    message=request.POST['message']
    email=request.POST['email']
    name=request.POST['name']
    if request.method=='POST':
       send_mail('Notary Website Message ',
                 'Message: '+message+'\nName: '+name+'\nEmail: '+email+'\nDocument: '+document,
                 'Lumpkinjakobr@gmail.com',
                 ['charlottelumpkin@yahoo.com', 'Lumpkinjakobr@gmail.com'],
                 fail_silently=False)
    return redirect('/')


# This is adding the review of the customer customers data added to the database
def comment(request):
    if request.method=='POST':
        email=request.POST['email']
        comment = request.POST['review']
        timeanddate=datetime.now()
        Review.objects.create(email=email,message=comment,date=timeanddate)
        Review.save
    return redirect('/')
