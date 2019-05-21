from django.db import models

# Create your models here.


class Department(models.Model):
    d_name = models.CharField(max_length=50,null=False)

    class Meta:
        db_table = 'department'
class Position(models.Model):
    p_name = models.CharField(max_length=50,null=False)

    class Meta:
        db_table = 'position'
class User_type(models.Model):
    t_name = models.CharField(max_length=50,null=False)

    class Meta:
        db_table = 'type'

class User(models.Model):
    username = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=256,null=False)
    dep_id = models.ForeignKey(to=Department,on_delete=models.CASCADE)
    pos_id = models.ForeignKey(to=Position,on_delete=models.CASCADE)
    type_id = models.ForeignKey(to=User_type,on_delete=models.CASCADE)

    class Meta:
        db_table = 'user'

class Log(models.Model):
    record = models.CharField(max_length=500)

    class Meta:
        db_table = 'log'

