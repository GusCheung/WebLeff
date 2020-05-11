from django.db import models

# Create your models here.



class Xtyh(models.Model):
    用户编号 = models.CharField(primary_key=True, max_length=20)
    用户姓名 = models.CharField(max_length=30, blank=True, null=True)
    部门 = models.CharField(max_length=20, blank=True, null=True)
    密码 = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=200)
    背景图片 = models.CharField(max_length=50)
    公司名称 = models.CharField(max_length=50)
    钉钉id = models.CharField(db_column='钉钉ID', max_length=50)  # Field name made lowercase.
    备注 = models.CharField(max_length=50)
    制单人 = models.CharField(max_length=20)
    制单人_name = models.CharField(max_length=30, blank=True, null=True)
    制单日期 = models.DateTimeField()
    更新人 = models.CharField(max_length=20)
    更新人_name = models.CharField(max_length=30, blank=True, null=True)
    更新日期 = models.DateTimeField()
    失效标志 = models.BooleanField()
    是否可以查看所有客户资料 = models.BooleanField()

    class Meta:
        managed = True
        db_table = '系统用户'


# 操作记录表
class WebLogin(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    appname = models.CharField(max_length=50, blank=True, null=True)
    apppage = models.CharField(max_length=50, blank=True, null=True)
    host = models.CharField(db_column='Host', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=50, blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'django_web_login记录'