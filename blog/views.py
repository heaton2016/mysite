from django.shortcuts import render

# Create your views here.
#coding = utf-8
from blog.models import BlogsPost
#from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
#from mysite.blog.models import BlogsPost

#create you views here
# def index(request):
# 	blog_list = BlogsPost.objects.all()
# 	return render_to_response('index.html',{'blog_list':blog_list})

def archive(request):
	posts = BlogsPost.objects.all()
	t = loader.get_template("archive.html")
	c = Context({'posts':posts })
	return HttpResponse(t.render(c))