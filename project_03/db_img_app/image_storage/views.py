from django.shortcuts import *
from django.views.generic import *
from image_storage.forms import *
from image_storage.models import *
# ------------------------- ----------------------client---------------
class client_img_view(TemplateView):
    form = client_form
    template_name = 'client/client_form.html'
    
    def post(self,  request, id=0):
        if id == 0:
            form = client_form(request.POST, request.FILES)
        else:
            clt = client.objects.get(pk=id)
            form = client_form(request.POST, request.FILES , instance = clt)
        if (form.is_valid()):
            form.save()                
            return redirect('client_display')
        context = self.get_context_data(form = form)
        return self.render_to_response(context)

    def get(self, request, id=0, *args, **kwargs):
        if id == 0:
            return self.post(request, id)
        else:
            clt = client.objects.get(pk=id)
            form = client_form(instance = clt)
            return render(request, 'client/client_form.html', {'form': form})

    
    
def print_client(request):
    context = {
        'print_client':client.objects.all()
        }
    return render(request, 'client/client_display.html', context)
    
def delete_client(request, id):
    clt = client.objects.get(pk=id)
    clt.delete()
    return redirect('client_display')

#-------------------- PRODUCTS --------------       ---------------------- --------------
class products_img_view(TemplateView):
    form = products_form
    template_name = 'products/products_form.html'
    
    def post(self,  request, id=0):
        if id == 0:
            form = products_form(request.POST, request.FILES)
        else:
            clt = products.objects.get(pk=id)
            form = products_form(request.POST, request.FILES, instance = clt)
        if form.is_valid():
            form.save()
            return redirect('products_display')
        context = self.get_context_data(form = form)
        return self.render_to_response(context)

    def get(self, request, id=0, *args, **kwargs):
        if id == 0:
            return self.post(request, id)
        else:
            clt = products.objects.get(pk=id)
            form = products_form(instance = clt)
            return render(request, 'products/products_form.html', {'form': form})
  
    
def print_products(request):
    context = {
        'print_products':products.objects.all()
        }
    return render(request, 'products/products_display.html', context)
    
def delete_products(request, id):
    clt = products.objects.get(pk=id)
    clt.delete()
    return redirect('products_display')

#-------------------- order --------------       ---------------------- --------------
class order_img_view(TemplateView):
    form = order_form
    template_name = 'order/order_form.html'
    
    def post(self,  request, id=0):
        if id == 0:
            form = order_form(request.POST, request.FILES)
        else:
            clt = order.objects.get(pk=id)
            form = order_form(request.POST, request.FILES, instance = clt)
        if form.is_valid():
            form.save()
            return redirect('order_display')
        context = self.get_context_data(form = form)
        return self.render_to_response(context)

    def get(self, request, id=0, *args, **kwargs):
        if id == 0:
            return self.post(request, id)
        else:
            clt = order.objects.get(pk=id)
            form = order_form(instance = clt)
            return render(request, 'order/order_form.html', {'form': form})
  
    
def print_order(request):
    context = {
        'print_order':order.objects.all()
        }
    return render(request, 'order/order_display.html', context)
    
def delete_order(request, id):
    clt = order.objects.get(pk=id)
    clt.delete()
    return redirect('order_display')