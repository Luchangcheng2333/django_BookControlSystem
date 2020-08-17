from django.shortcuts import render
from django.http import HttpResponse
from .models import SoftwarePackage
import os
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

PATH = r'/home/titan/下载/'
# Create your views here.
def index(request):
    return HttpResponse("Hello World!")


def detail(request):
    book_list = SoftwarePackage.objects.order_by('-pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'manager/detail.html', context)


def addBook(request):
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

        myFile = request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("no files for upload!")
        filename = os.path.join(PATH, myFile.name)
        destination = open(filename, 'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        #return HttpResponse("upload over!")

    temp_book = SoftwarePackage(name=temp_name, author=temp_author, \
                     pub_house=temp_pub_house, pub_date=timezone.now(), file=myFile.name, status='待审核')

    temp_book.save()

    return HttpResponseRedirect(reverse('detail'))


def deleteBook(request, book_id):
    bookID = book_id
    SoftwarePackage.objects.filter(id=bookID).delete()

    return HttpResponseRedirect(reverse('detail'))

def upload_file(request):
    if request.method == "POST":
        myFile =request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join(r"/home/titan/下载/",myFile.name),'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")