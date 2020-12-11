from django.db import models

# Create your models here.




class Product(models.Model):
    
    product_id = models.CharField(primary_key=True , max_length=100)
    price = models.IntegerField()
    brand = models.CharField(max_length=128)
    description = models.TextField()
    color = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.brand+" " + self.name


class Phone(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    size = models.TextField()
    ram = models.IntegerField()
    resolutionscreen = models.TextField()
    camera_desc = models.TextField()

    def __str__(self):
        return self.product.brand +" "+ self.product.name



# class HeadPhone(models.Model):
# 
    # product = models.ForeignKey(Product , on_delete = models.CASCADE )