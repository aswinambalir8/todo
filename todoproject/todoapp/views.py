from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import newform
from .models import todo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class todolist(ListView):
    model = todo
    template_name = 'index.html'
    context_object_name = 'task1'

class tododetail(DetailView):
    model = todo
    template_name = 'details.html'
    context_object_name = 'detail'

class todoupdate(UpdateView):
    model = todo
    template_name = 'upgrade.html'
    context_object_name = 'update'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('gendetail',kwargs={'pk':self.object.id})
class tododelete(DeleteView):
    model = todo
    template_name = 'delete.html'
    success_url = reverse_lazy('genlist')

def main(request):
    task1 = todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = todo(name=name,priority=priority,date=date)
        task.save()
    return render(request,'index.html',{'task1':task1})


def details(request):
    task = todo.objects.all()
    return render(request,'details.html',{'task':task})

def delete(request,todoid):
    task = todo.objects.get(id=todoid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    t1 = todo.objects.get(id=id)

    frm = newform(request.POST or None,instance=t1)
    if frm.is_valid():
        frm.save()
        return redirect('/')
    return render(request,'update.html',{'t1':t1,'frm':frm})
