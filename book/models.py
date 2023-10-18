from django.db import models  
    
class Contact(models.Model):
    name = models.CharField(max_length = 50)
    family_name = models.TextField(max_length = 50)
    surname = models.TextField(max_length = 50)
    phone = models.IntegerField(max_length = 10)
    email = models.EmailField()
    photo = models.ImageField()
    birth = models.DateField()

    def __str__ (self) -> str:
        return (self.name, self.family_name)
    