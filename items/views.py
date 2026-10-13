from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item


def item_list(request):
    status = request.GET.get('status')
    items = Item.objects.all()
    if status in ('lost', 'found'):
        items = items.filter(status=status)
    return render(request, 'items/item_list.html', {'items': items, 'current': status})


def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'items/item_form.html', {'form': form})