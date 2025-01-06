from django.shortcuts import render, get_object_or_404, redirect
from .models import FashionItem

# List View (Read all items)
def fashion_item_list(request):
    items = FashionItem.objects.all()
    return render(request, 'fashion_item_list.html', {'items': items})

# Detail View (Read one item)
def fashion_item_detail(request, pk):
    item = get_object_or_404(FashionItem, pk=pk)
    return render(request, 'fashion_item_detail.html', {'item': item})

# Create View
def fashion_item_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        brand = request.POST['brand']
        category = request.POST['category']
        price = request.POST['price']
        stock_quantity = request.POST['stock_quantity']
        FashionItem.objects.create(
            name=name, brand=brand, category=category, price=price, stock_quantity=stock_quantity
        )
        return redirect('fashion_item_list')
    return render(request, 'fashion_item_form.html')

# Update View
def fashion_item_update(request, pk):
    item = get_object_or_404(FashionItem, pk=pk)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.brand = request.POST['brand']
        item.category = request.POST['category']
        item.price = request.POST['price']
        item.stock_quantity = request.POST['stock_quantity']
        item.save()
        return redirect('fashion_item_list')
    return render(request, 'fashion_item_form.html', {'item': item})

# Delete View
def fashion_item_delete(request, pk):
    item = get_object_or_404(FashionItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('fashion_item_list')
    return render(request, 'fashion_item_confirm_delete.html', {'item': item})
