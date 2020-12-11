from django.db import models
from django.contrib.auth.models import User
from django.views import defaults
from PIL import Image



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=False)
    currentLocation = models.CharField(max_length=25, blank=True, default='-')
    phoneNumber = models.CharField(max_length=32, blank=False)


    def save(self , *args , **kwargs):
        print("printing args in Profile" , args)
        super().save(*args , **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
    def __str__(self):
        return f'{self.user.username} Profile'





# class Order(models.Model):
#     user_id = models.ForeignKey(User , on_delete=models.CASCADE)
#     off = models.PositiveIntegerField()
#     order_datetime = models.DateTimeField(auto_now_add=True, null=True)
 

