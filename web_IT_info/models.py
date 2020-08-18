from django.db import models

# Create your models here.

class it资产(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    资产编号 = models.CharField(max_length=50)
    资产名称 = models.CharField(max_length=50, blank=True, null=True)
    资产类型 = models.CharField(max_length=50, blank=True, null=True)
    区域 = models.CharField(max_length=50, blank=True, null=True)
    位置 = models.CharField(max_length=50, blank=True, null=True)
    使用人 = models.CharField(max_length=50, blank=True, null=True)
    使用人部门 = models.CharField(max_length=50, blank=True, null=True)
    使用状态 = models.CharField(max_length=50)
    cpu = models.CharField(db_column='CPU', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpu序列号 = models.CharField(db_column='CPU序列号', max_length=100, blank=True, null=True)  # Field name made lowercase.
    主板 = models.CharField(max_length=100, blank=True, null=True)
    操作系统 = models.CharField(max_length=100, blank=True, null=True)
    显卡 = models.CharField(max_length=100, blank=True, null=True)
    硬盘 = models.CharField(max_length=100, blank=True, null=True)
    硬盘序列号 = models.CharField(max_length=100, blank=True, null=True)
    内存 = models.CharField(max_length=100, blank=True, null=True)
    内存插槽 = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(db_column='IP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    购买日期 = models.DateTimeField(blank=True, null=True)
    管理人 = models.CharField(max_length=50, blank=True, null=True)
    电脑名称 = models.CharField(max_length=50, blank=True, null=True)
    删除标记 = models.CharField(max_length=10, blank=True, null=True)
    贴纸编码 = models.CharField(max_length=50, blank=True, null=True)
    备注 = models.CharField(max_length=200, blank=True, null=True)
    制单人 = models.CharField(max_length=50, blank=True, null=True)
    制单日期 = models.DateTimeField(blank=True, null=True)
    更新人 = models.CharField(max_length=50, blank=True, null=True)
    更新日期 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IT资产'