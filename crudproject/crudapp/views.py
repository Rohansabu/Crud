from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
# Create your views here



from django.shortcuts import render

from .models import Crud
def index(request):
    crud = Crud.objects.all()
    if request.method == 'POST':
        slno=request.POST.get('slno','')
        name=request.POST.get('itemname','')
        description=request.POST.get('description','')
        data=Crud(slno=slno,itemname=name,description=description)
        data.save()
    return render(request,'base.html',{'crud':crud})
      
    
   

def update(request, id):
    crud = Crud.objects.get(id=id)
    if request.method == 'POST':
        crud.slno = request.POST.get('slno', '')
        crud.itemname = request.POST.get('itemname', '')
        crud.description = request.POST.get('description', '')
        crud.save()
        return redirect('/')
    return render(request, 'update.html', {'crud': crud})

def delete(request,crudid):
    crud=Crud.objects.get(id=crudid)
    if request.method =='POST':
        crud.delete()
        return redirect('/')

    return render(request,'delete.html')


