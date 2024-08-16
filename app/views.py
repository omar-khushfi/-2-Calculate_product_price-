from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import View
from django.shortcuts import get_object_or_404
from django.urls import reverse
# Create your views here.
def view_products(request):
    products=Product.objects.all()
    products_with_cost=[]
    for i in products:
        sum=0
        met=Con.objects.filter(product=i)
        for j in met :
            sum+=(j.weight*j.material.price)/1000;
        product_info = {
            'product': i,
            'calculated_cost': sum
        }
        products_with_cost.append(product_info)
    context={
        'products':products_with_cost
    }
    return render(request,'Product.html',context)

def view_Materials(request):
    materials=Material.objects.all()
    context={
        'materials':materials,
    }
    return render(request,'Materials.html',context)


class edit_proudct(View):
    def get(self,request,pk):
        proudct=Product.objects.get(pk=pk)
        pf=productform(instance=proudct)
        context={
        'product':proudct,
        'form':pf,
        }
        return render(request,'edit-prod.html',context)
    def post(self,request,pk):
        proudct=Product.objects.get(pk=pk)
        pro_save=productform(request.POST,request.FILES,instance=proudct)
        if pro_save.is_valid():
            # print(request.FILES)
            pro_save.save()
        return redirect('/')
    
    
    

class edit_mateiral(View):
    def get(self,request,pk):
        material=Material.objects.get(pk=pk)
        mf=materialform(instance=material)
        context={
        'proudct':material,
        'form':mf,
        }
        return render(request,'edit-mat.html',context)
    def post(self,request,pk):
        material=Material.objects.get(pk=pk)
        mat_save=materialform(request.POST,request.FILES,instance=material)
        if mat_save.is_valid():
            print(request.FILES)
            mat_save.save()
        return redirect('/Materials')
    
    
class edit_mateiral_product(View):
    def get(self,request,pk):
       con=Con.objects.filter(product_id=pk)
       fm=conform()
       context={
          'con':con, 
          'form':conform,
       }
       return render(request,'edit-mat-pro.html',context)
    def post(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        form = conform(request.POST)
        weight=request.POST.get('weight')
        material=request.POST.get('material')
   
        mmaterial=Material.objects.get(id=material)
        if Con.objects.filter(product=product,material=mmaterial).exists():
           pass
        else:
            con=Con(product=product,material=mmaterial,weight=weight)
            con.save()
        return redirect(reverse('edit-material-product', args=[pk]))
    
    
def delete_product(requset,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect(reverse('product'))
    
       
def delete_material(requset,pk):
    material=Material.objects.get(pk=pk)
    material.delete()
    return redirect(reverse('Materials'))
    
    
def delete_material_product(requset,pk):
    con=Con.objects.get(pk=pk)
    product=Product.objects.get(pk=con.product.pk)
    PK=product.pk;
    con.delete()
    return redirect(reverse('edit-material-product',args=[PK]))
       
       
       
class add_product(View):
    def get(self,request):
        form=productform()
        context={
            'form':form,
        }
        return render(request,'add-product.html',context)
    
    def post(self,request):
       product=productform(request.POST,request.FILES)
       if product.is_valid():
           product.save()
       return redirect('/')
       

class add_material(View):
    def get(self,request):
        form=materialform()
        context={
            'form':form,
        }
        return render(request,'add-material.html',context)
    
    def post(self,request):
       material=materialform(request.POST,request.FILES)
       if material.is_valid():
           material.save()
       return redirect(reverse('Materials'))
       