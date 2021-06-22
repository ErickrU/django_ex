from django.shortcuts import redirect, render
from .forms import client_form, products_form, order_form
from .models import client, products, order

# Clients CRUD
def select_client(request):
    context = {'select_client':client.objects.all()}
    return render(request, 'form/select_client.html', context)

def insert_client(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = client_form() 
        else:
            clt = client.objects.get(pk=id)
            form = client_form(instance = clt)
        return render(request, 'form/client_form.html',{'form':form})
    else:
        if id == 0:
            form = client_form(request.POST)
        else:
            clt = client.objects.get(pk=id)
            form = client_form(request.POST, instance = clt)
        if(form.is_valid()):
            form.save()
        else:
            return render(request, 'form/client_form.html',{'form':form})
        return redirect('/form/list_client')

def delete_client(request, id):
    clt = client.objects.get(pk=id)
    clt.delete()
    return redirect('/form/list_client')

# products CRUD
def select_products(request):
    context = {'select_products':products.objects.all()}
    return render(request, 'form/select_products.html', context)

def insert_products(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = products_form() 
        else:
            prd = products.objects.get(pk=id)
            form = products_form(instance = prd)
        return render(request, 'form/products_form.html',{'form':form})
    else:
        if id == 0:
            form = products_form(request.POST)
        else:
            prd = products.objects.get(pk=id)
            form = products_form(request.POST, instance = prd)
        if(form.is_valid()):
            form.save()
        else:
            return render(request, 'form/products_form.html',{'form':form})
        return redirect('/form/list_product')

def delete_products(request, id):
    prd = products.objects.get(pk=id)
    prd.delete()
    return redirect('/form/list_product')

# order CRUD
def select_order(request):
    context = {'select_order':order.objects.all()}
    return render(request, 'form/select_order.html', context)

def insert_order(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = order_form() 
        else:
            prd = order.objects.get(pk=id)
            form = order_form(instance = prd)
        return render(request, 'form/order_form.html',{'form':form})
    else:
        if id == 0:
            form = order_form(request.POST)
        else:
            prd = order.objects.get(pk=id)
            form = order_form(request.POST, instance = prd)
        if(form.is_valid()):
            form.save()
        else:
            return render(request, 'form/order_form.html',{'form':form})
        return redirect('/form/list_order')

def delete_order(request, id):
    prd = order.objects.get(pk=id)
    prd.delete()
    return redirect('/form/list_order')