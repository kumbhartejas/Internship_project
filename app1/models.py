from django.db import models
from django.utils.text import slugify
# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length=255)

    def save1(self, *args, **kwargs):
     if not self.slug:
        self.slug = slugify(self.name)  # Create slug from the title
     super().save(*args, **kwargs)


    def __str__(self):
        return self.name

class item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="item")
    image=models.ImageField( upload_to='images/' ,null=True)
    price = models.IntegerField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True)
    slug=models.SlugField(unique=True)


    def save2(self, *args, **kwargs):
     if not self.slug:
        self.slug = slugify(self.name)  # Create slug from the title
     super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class scroll(models.Model):
   image = models.ImageField(upload_to="images/")
   name = models.CharField(max_length=255,null=True)
   count = models.PositiveIntegerField(default=1,null=True)

   def __str__(self):
       return self.name



class m_form(models.Model):
   name=models.CharField(max_length=50)
   lastname=models.CharField(max_length=50)
   email=models.EmailField()
   subject=models.TextField(max_length=200 ,null=True)
   message=models.TextField(max_length=700, null=True)
  
   def __str__(self):
       return f'{self.name}  |   {self.lastname} '
   
class log(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


# class booking(models.)