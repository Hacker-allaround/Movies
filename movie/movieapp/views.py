from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies=Movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movies=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movies':movies})

def add_movie(request):
    if request.method=='POST':
        n=request.POST.get('name')
        d=request.POST.get('desc')
        y=request.POST.get('year')
        i=request.FILES['img']
        movies=Movie(name=n,desc=d,year=y,img=i)
        movies.save()


    return render(request,'add.html')

def update(request,id):
    movies=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movies':movies})
def delete(request,id):
    if request.method=='POST':
        movies=Movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')
