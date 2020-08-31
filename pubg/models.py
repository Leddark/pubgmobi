from django.db import models

# Create your models here.

class Loginy (models.Model):
    username = models.CharField(max_length=150 , null=True  , verbose_name="اسم المستخدم او البريد" , db_column="اسم مستخدم او رقم او بريد")
    password = models.CharField(max_length=100 , null=True , verbose_name="كلمة السر" , db_column="كلمة السر")

    def __str__(self):
        return str(self.username)


class Datay (models.Model):
    
    nameRP= models.CharField(max_length=100 , null=True , verbose_name="تصنيف RP" , db_column="تصنيف RP")
    typeUs= models.CharField(max_length=100 , null=True , verbose_name="نوع الجهاز" , db_column="نوع الجهاز")
    level = models.IntegerField(null=True , verbose_name="مستوي الحساب" , db_column="مستوي الحساب")
    acID = models.IntegerField(null=True , verbose_name="id اللاعب" , db_column="id اللاعب")


    def __str__(self):
        return str(self.acID) 


