from django.shortcuts import render,redirect
from django.http import HttpResponse
from learningapp.models import LearningCourses
from django.db.models import Q

# Create your views here.

def edit(request,rid):
    if request.method=="POST":
        Batch_Name=request.POST['bname']
        Course_Category=request.POST['cat']
        Other_Course=request.POST['oc']
        Recruitment=request.POST['re']
        Price=request.POST['amount']
        Batch_Timing=request.POST['bt']
        Status=request.POST['stat']
        p=LearningCourses.objects.filter(id=rid)
        p.update(name=Batch_Name,cat1=Course_Category,cat2=Other_Course,job_type=Recruitment,price=Price,time=Batch_Timing,status=Status)
        return redirect('/dash')
    else:
        p=LearningCourses.objects.filter(id=rid)
        content={}
        content['data']=p
        return render(request,'edit.html',content)



def delete(request,rid):
    p=LearningCourses.objects.filter(id=rid)
    p.delete()
    return redirect('/dash')

def addproduct(request):

    if request.method=="POST":
        Batch_Name=request.POST['bname']
        Course_Category=request.POST['cat']
        Other_Course=request.POST['oc']
        Recruitment=request.POST['re']
        Price=request.POST['amount']
        Batch_Timing=request.POST['bt']
        Status=request.POST['stat']

        p=LearningCourses.objects.create(name=Batch_Name,cat1=Course_Category,cat2=Other_Course,job_type=Recruitment,price=Price,time=Batch_Timing,status=Status)
        p.save()
        return redirect('/dash')
    
    else:
        return render(request,'addproduct.html')

def dashboard(request):
    da=LearningCourses.objects.all()
    content={}
    content['data']=da
    return render(request,'dashboard.html',content)

# filter

def statfilter(request,sv):
    p=LearningCourses.objects.filter(status=sv)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def cat1filter(request,cv1):
    p=LearningCourses.objects.filter(cat1=cv1)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def cat2filter(request,cv2):
    p=LearningCourses.objects.filter(cat2=cv2)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def timefilter(request,tf):
    p=LearningCourses.objects.filter(time=tf)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def pricefilter(request,pf):
    if pf=='1' :
        p=LearningCourses.objects.filter(price__gt=30000)
    else:
        p=LearningCourses.objects.filter(price__lt=30000)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def sortfilter(request,s):
    if s=='0':
        p=LearningCourses.objects.order_by('price')
    else:
        p=LearningCourses.objects.order_by('-price')
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def multifilter(request):

    if request.method=="POST":
        sv=request.POST['status']
        cv1=request.POST['category']
        q1=Q(cat1=cv1)
        q2=Q(status=sv)
        p=LearningCourses.objects.filter(q1 & q2)
        content={}
        content['data']=p
        return render(request,'dashboard.html',content)



