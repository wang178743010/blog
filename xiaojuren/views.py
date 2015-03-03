from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template.response import TemplateResponse as TR
from xiaojuren.models import book,Image,link,link2,link3,link6,link7,index
def home(request):
	a1 = book.objects.all()[::-1]
	a2 = link.objects.all()
	a3 = link2.objects.all()
	a4 = link3.objects.all()
	a6 = link6.objects.all()
	a7 = link7.objects.all()
	a8 = index.objects.all()

	d = {"a1":a1,"a2":a2,"a3":a3,"a4":a4,"a6":a6,"a7":a7,"a8":a8}
	return TR(request,"juren.html",d)


def upload(request):
	image_form = modelform_factory(book)
	a = image_form(request.POST,request.FILES)
	if a.is_valid():
		img = a.save()
		return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('/media/%s').closest('.mce-window').find('.mce-primary').click();</script>"%img.img)
	return redirect("/index")
                                             


def text(request):
	return render_to_response("text.html")

def null(request):
	d = {}
	all_img = Image.objects.all()
	for a in all_img:
		d[a.name] = a.img
	return TR(request,'juren.html',d)


def add(request):
	a = book()
	a.title = request.POST['title']
	a.content = request.POST['content']
	a.save()
	return redirect('/index')

def all_left(request):

	return render_to_response("left.html")
