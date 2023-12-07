from django.shortcuts import render, get_object_or_404, redirect
from .models import Automobiles
from .forms import AutoForm

# Create your views here.

def automobiles(request):
    automobile = Automobiles.objects.all()
    return render(request, 'automobile.html', {'automobile':automobile})

def auto(request, pk):
    auto = get_object_or_404(Automobiles, id=pk)
    return render(request, 'auto.html', context={'auto':auto})

def postdelete(request, pk):
    auto = get_object_or_404(Automobiles, id=pk)
    auto.delete()
    return redirect('/automobiles')

def updatepost(request, pk):
    auto = get_object_or_404(Automobiles, id=pk)
    form = AutoForm(initial={"title":auto.title, "short_desc":auto.short_desc, "body":auto.body})

    if request.method == "AUTO":
        form = AutoForm(request.AUTO, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('/automobiles')
    return render(request, "update.html", context={'form':form})