from django.db import models
class User(models.Model):
    name = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    nbloggedin = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    def getAge(self):
        return self.age
    def check_age(self,age):
        if self.age == age:
           return self.age
        return False
    def setNbLoggedin(self):
        self.nbloggedin += 1
    def getName(self):
        return self.name
# Create your models here.
