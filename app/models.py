from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    selling_price=models.DecimalField(decimal_places=2,max_digits=10)
    image=models.ImageField(upload_to='photo',null=True,blank=True)
    def __str__(self):
        return self.name
    
class Material(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    def __str__(self):
        return self.name
    
class Con(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    material=models.ForeignKey(Material,on_delete=models.CASCADE)
    weight=models.DecimalField(decimal_places=2,max_digits=10)
    def __str__(self):
        return self.material.name+"_"+self.product.name
    