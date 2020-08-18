# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aa(models.Model):
    ״̬ = models.CharField(max_length=50)
    Ʒ�� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��� = models.CharField(max_length=50)
    ë�� = models.CharField(max_length=50)
    �ӹ��� = models.CharField(max_length=50)
    �ɱ��� = models.CharField(max_length=50)
    ��˰�� = models.CharField(max_length=50)
    Ա���� = models.CharField(max_length=50)
    �ƹ�ɱ��� = models.CharField(max_length=50)
    ���Ƽ� = models.CharField(max_length=50)
    ������ = models.CharField(max_length=50)
    ���������� = models.CharField(max_length=50)
    �������� = models.CharField(max_length=50)
    leff������ = models.IntegerField(db_column='LEFF������')  # Field name made lowercase.
    leff�������� = models.IntegerField(db_column='LEFF��������')  # Field name made lowercase.
    �ճ���� = models.CharField(max_length=50)
    ���ջ�� = models.CharField(max_length=50)
    ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��� = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AA��Ʒ�۸���'


class A(models.Model):
    spdm = models.CharField(max_length=50, blank=True, null=True)
    pp = models.CharField(max_length=50, blank=True, null=True)
    spmc = models.CharField(max_length=50, blank=True, null=True)
    ml = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'A��������'


class Bsxlmx(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Ʒ������ = models.CharField(max_length=50, blank=True, null=True)
    ��� = models.CharField(max_length=50, blank=True, null=True)
    ���� = models.CharField(max_length=50, blank=True, null=True)
    �������� = models.CharField(max_length=50, blank=True, null=True)
    ���� = models.CharField(max_length=50, blank=True, null=True)
    �������� = models.CharField(max_length=50, blank=True, null=True)
    �������� = models.CharField(max_length=50, blank=True, null=True)
    ��� = models.CharField(max_length=50, blank=True, null=True)
    ���ʦ = models.CharField(max_length=50, blank=True, null=True)
    ��Ʒ���� = models.CharField(max_length=50, blank=True, null=True)
    ��Ʒ���� = models.CharField(max_length=50, blank=True, null=True)
    ��ɫ���� = models.CharField(max_length=50, blank=True, null=True)
    ��ɫ���� = models.CharField(max_length=50, blank=True, null=True)
    �ߴ���� = models.CharField(max_length=50, blank=True, null=True)
    �ߴ����� = models.CharField(max_length=50, blank=True, null=True)
    ��Ʒ״̬ = models.CharField(max_length=50, blank=True, null=True)
    ���� = models.IntegerField(blank=True, null=True)
    ���� = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ��� = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    �ɱ����� = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    �ɱ���� = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    �������� = models.CharField(max_length=50, blank=True, null=True)
    ���ݱ�� = models.CharField(max_length=50, blank=True, null=True)
    ԭ���ݺ� = models.CharField(max_length=50, blank=True, null=True)
    �������� = models.DateTimeField(blank=True, null=True)
    �ͻ����� = models.CharField(max_length=50, blank=True, null=True)
    �ͻ����� = models.CharField(max_length=50, blank=True, null=True)
    �ֿ���� = models.CharField(max_length=50, blank=True, null=True)
    �ֿ����� = models.CharField(max_length=50, blank=True, null=True)
    ������ = models.CharField(max_length=50, blank=True, null=True)
    ���� = models.CharField(max_length=50, blank=True, null=True)
    �� = models.CharField(max_length=50, blank=True, null=True)
    ������ = models.CharField(max_length=50, blank=True, null=True)
    ������� = models.CharField(max_length=50, blank=True, null=True)
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BSXLMX'


class Bs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    �� = models.CharField(max_length=50)
    ���� = models.CharField(max_length=50)
    ������ = models.CharField(max_length=50)
    �ͻ����� = models.CharField(max_length=50)
    �ͻ��������� = models.IntegerField()
    �ͻ����� = models.CharField(max_length=50)
    �������� = models.IntegerField()
    ���۽�� = models.IntegerField()
    ������������ = models.IntegerField()
    ���۽��� = models.IntegerField()
    ������������ = models.IntegerField()
    ���۽������ = models.IntegerField()
    ��������ƽ�� = models.IntegerField()
    ���۽��ƽ�� = models.IntegerField()
    ������������ = models.IntegerField()
    ���۽������ = models.IntegerField()
    ������������ = models.IntegerField()
    ���۽������ = models.IntegerField()
    ����������Ʒ = models.IntegerField()
    ���۽����Ʒ = models.IntegerField()
    ����������Ʒ = models.IntegerField()
    ���۽����Ʒ = models.IntegerField()
    �˻����� = models.IntegerField()
    �˻���� = models.IntegerField()
    �˻��������� = models.IntegerField()
    �˻����� = models.IntegerField()
    �˻��������� = models.IntegerField()
    �˻�������� = models.IntegerField()
    �˻�����ƽ�� = models.IntegerField()
    �˻����ƽ�� = models.IntegerField()
    �˻��������� = models.IntegerField()
    �˻�������� = models.IntegerField()
    �˻��������� = models.IntegerField()
    �˻�������� = models.IntegerField()
    �˻�������Ʒ = models.IntegerField()
    �˻������Ʒ = models.IntegerField()
    �˻�������Ʒ = models.IntegerField()
    �˻������Ʒ = models.IntegerField()
    ��ע = models.CharField(max_length=250)
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS���ۼ�'


class Bs30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS����30��'


class Bs30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS����������Ӫ30��'


class Bs30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS����ΨƷ��30��'


class Bs17(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS����ΨƷ���1��7��'


class Bs27(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS����ΨƷ���2��7��'


class Bs37(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS����ΨƷ���3��7��'


class Bs30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS������ΨƷ��30��'


class Bs17(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS������ΨƷ���1��7��'


class Bs27(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS������ΨƷ���2��7��'


class Bs37(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS������ΨƷ���3��7��'


class Config(models.Model):
    csys = models.CharField(db_column='cSys', max_length=30)  # Field name made lowercase.
    citem = models.CharField(db_column='cItem', primary_key=True, max_length=50)  # Field name made lowercase.
    bcost = models.BooleanField(db_column='bCost')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Config'


class DdscztCnpi(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lxdm = models.CharField(db_column='LXDM', max_length=50)  # Field name made lowercase.
    cplx = models.CharField(db_column='CPLX', max_length=50)  # Field name made lowercase.
    yjcn = models.IntegerField(db_column='YJCN', blank=True, null=True)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.
    gxr = models.CharField(db_column='GXR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gxrq = models.DateTimeField(db_column='GXRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DDSCZT_CNPI'


class DdscztCzrz(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    zdm = models.CharField(db_column='ZDM', max_length=50)  # Field name made lowercase.
    cznr = models.CharField(db_column='CZNR', max_length=50)  # Field name made lowercase.
    djbh = models.CharField(db_column='DJBH', max_length=50)  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=300, blank=True, null=True)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.
    gxr = models.CharField(db_column='GXR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gxrq = models.DateTimeField(db_column='GXRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DDSCZT_CZRZ'


class DdscztYgrs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rs = models.IntegerField(db_column='RS', blank=True, null=True)  # Field name made lowercase.
    rq = models.DateTimeField(db_column='RQ', blank=True, null=True)  # Field name made lowercase.
    djbh = models.CharField(db_column='DJBH', max_length=50)  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=300, blank=True, null=True)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.
    gxr = models.CharField(db_column='GXR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gxrq = models.DateTimeField(db_column='GXRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DDSCZT_YGRS'


class Efast(models.Model):
    djbh = models.CharField(db_column='DJBH', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EFAST�ϴ�����'


class Erpspkcb(models.Model):
    ckdm = models.CharField(db_column='CKDM', max_length=20)  # Field name made lowercase.
    kwdm = models.CharField(db_column='KWDM', max_length=20)  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=20)  # Field name made lowercase.
    gg1dm = models.CharField(db_column='GG1DM', max_length=20)  # Field name made lowercase.
    gg2dm = models.CharField(db_column='GG2DM', max_length=20)  # Field name made lowercase.
    sl = models.DecimalField(db_column='SL', max_digits=18, decimal_places=4)  # Field name made lowercase.
    sl1 = models.DecimalField(db_column='SL1', max_digits=18, decimal_places=4)  # Field name made lowercase.
    sl2 = models.DecimalField(db_column='SL2', max_digits=18, decimal_places=4)  # Field name made lowercase.
    sl3 = models.DecimalField(db_column='SL3', max_digits=18, decimal_places=4)  # Field name made lowercase.
    sl4 = models.DecimalField(db_column='SL4', max_digits=18, decimal_places=4)  # Field name made lowercase.
    sl5 = models.DecimalField(db_column='SL5', max_digits=18, decimal_places=4)  # Field name made lowercase.
    sl6 = models.DecimalField(db_column='SL6', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sl7 = models.DecimalField(db_column='SL7', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sl8 = models.DecimalField(db_column='SL8', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sl9 = models.DecimalField(db_column='SL9', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sl10 = models.DecimalField(db_column='SL10', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ydsl = models.DecimalField(db_column='YDSL', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.TextField(db_column='LastChanged')  # Field name made lowercase. This field type is a guess.
    ts = models.DateTimeField(db_column='TS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ERPSPKCB'


class It(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ���� = models.CharField(max_length=50, blank=True, null=True)
    ���� = models.IntegerField(blank=True, null=True)
    ���� = models.CharField(max_length=50, blank=True, null=True)
    ��ע = models.CharField(max_length=100, blank=True, null=True)
    ʹ������ = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IT_�ʲ��Ĳ���ϸ'


class It(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    �ʲ���� = models.CharField(max_length=50)
    �ʲ����� = models.CharField(max_length=50, blank=True, null=True)
    �ʲ����� = models.CharField(max_length=50, blank=True, null=True)
    ���� = models.CharField(max_length=50, blank=True, null=True)
    λ�� = models.CharField(max_length=50, blank=True, null=True)
    ʹ���� = models.CharField(max_length=50, blank=True, null=True)
    ʹ���˲��� = models.CharField(max_length=50, blank=True, null=True)
    ʹ��״̬ = models.CharField(max_length=50)
    cpu = models.CharField(db_column='CPU', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpu���к� = models.CharField(db_column='CPU���к�', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ���� = models.CharField(max_length=100, blank=True, null=True)
    ����ϵͳ = models.CharField(max_length=100, blank=True, null=True)
    �Կ� = models.CharField(max_length=100, blank=True, null=True)
    Ӳ�� = models.CharField(max_length=100, blank=True, null=True)
    Ӳ�����к� = models.CharField(max_length=100, blank=True, null=True)
    �ڴ� = models.CharField(max_length=100, blank=True, null=True)
    �ڴ��� = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(db_column='IP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    �������� = models.DateTimeField(blank=True, null=True)
    ������ = models.CharField(max_length=50, blank=True, null=True)
    �������� = models.CharField(max_length=50, blank=True, null=True)
    ɾ����� = models.CharField(max_length=10, blank=True, null=True)
    ��ֽ���� = models.CharField(max_length=50, blank=True, null=True)
    ��ע = models.CharField(max_length=200, blank=True, null=True)
    �Ƶ��� = models.CharField(max_length=50, blank=True, null=True)
    �Ƶ����� = models.DateTimeField(blank=True, null=True)
    ������ = models.CharField(max_length=50, blank=True, null=True)
    �������� = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IT�ʲ�'


class It(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    �ʲ���� = models.CharField(max_length=50)
    �ʲ����� = models.CharField(max_length=50)
    �ʲ����� = models.CharField(max_length=50)
    �ʲ���� = models.CharField(max_length=50)
    �ʲ��ͺ� = models.CharField(max_length=50)
    �������� = models.DateTimeField(blank=True, null=True)
    ��Ӧ������ = models.CharField(max_length=50)
    ������� = models.CharField(max_length=50)
    �������� = models.DateTimeField(blank=True, null=True)
    ���޽�ֹ���� = models.DateTimeField(blank=True, null=True)
    ʹ������ = models.DateTimeField(blank=True, null=True)
    Ԥ��ʹ������ = models.IntegerField(blank=True, null=True)
    Ԥ�Ʊ������� = models.DateTimeField(blank=True, null=True)
    ԭʼ�۸� = models.DecimalField(max_digits=18, decimal_places=2)
    ʹ��״̬ = models.CharField(max_length=50)
    ����λ�� = models.CharField(max_length=50)
    ������ = models.CharField(max_length=50)
    �����˲��� = models.CharField(max_length=50)
    ������ = models.CharField(max_length=50)
    �����ͺ� = models.CharField(max_length=50)
    �������_sn = models.CharField(db_column='�������_SN', max_length=50)  # Field name made lowercase.
    cpu1��� = models.CharField(db_column='CPU1���', max_length=50)  # Field name made lowercase.
    cpu1�ͺ� = models.CharField(db_column='CPU1�ͺ�', max_length=50)  # Field name made lowercase.
    cpu1���_sn = models.CharField(db_column='CPU1���_SN', max_length=50)  # Field name made lowercase.
    cpu1���ȱ�� = models.CharField(db_column='CPU1���ȱ��', max_length=50)  # Field name made lowercase.
    cpu1���� = models.CharField(db_column='CPU1����', max_length=50)  # Field name made lowercase.
    cpu1�������_sn = models.CharField(db_column='CPU1�������_SN', max_length=50)  # Field name made lowercase.
    cpu2��� = models.CharField(db_column='CPU2���', max_length=50)  # Field name made lowercase.
    cpu2�ͺ� = models.CharField(db_column='CPU2�ͺ�', max_length=50)  # Field name made lowercase.
    cpu2���_sn = models.CharField(db_column='CPU2���_SN', max_length=50)  # Field name made lowercase.
    cpu2���ȱ�� = models.CharField(db_column='CPU2���ȱ��', max_length=50)  # Field name made lowercase.
    cpu2���� = models.CharField(db_column='CPU2����', max_length=50)  # Field name made lowercase.
    cpu2�������_sn = models.CharField(db_column='CPU2�������_SN', max_length=50)  # Field name made lowercase.
    cpu3��� = models.CharField(db_column='CPU3���', max_length=50)  # Field name made lowercase.
    cpu3�ͺ� = models.CharField(db_column='CPU3�ͺ�', max_length=50)  # Field name made lowercase.
    cpu3���_sn = models.CharField(db_column='CPU3���_SN', max_length=50)  # Field name made lowercase.
    cpu3���ȱ�� = models.CharField(db_column='CPU3���ȱ��', max_length=50)  # Field name made lowercase.
    cpu3���� = models.CharField(db_column='CPU3����', max_length=50)  # Field name made lowercase.
    cpu3�������_sn = models.CharField(db_column='CPU3�������_SN', max_length=50)  # Field name made lowercase.
    cpu4��� = models.CharField(db_column='CPU4���', max_length=50)  # Field name made lowercase.
    cpu4�ͺ� = models.CharField(db_column='CPU4�ͺ�', max_length=50)  # Field name made lowercase.
    cpu4���_sn = models.CharField(db_column='CPU4���_SN', max_length=50)  # Field name made lowercase.
    cpu4���ȱ�� = models.CharField(db_column='CPU4���ȱ��', max_length=50)  # Field name made lowercase.
    cpu4���� = models.CharField(db_column='CPU4����', max_length=50)  # Field name made lowercase.
    cpu4�������_sn = models.CharField(db_column='CPU4�������_SN', max_length=50)  # Field name made lowercase.
    �������1��� = models.CharField(max_length=50)
    �������1 = models.CharField(max_length=50)
    �������1���_sn = models.CharField(db_column='�������1���_SN', max_length=50)  # Field name made lowercase.
    �������2��� = models.CharField(max_length=50)
    �������2 = models.CharField(max_length=50)
    �������2���_sn = models.CharField(db_column='�������2���_SN', max_length=50)  # Field name made lowercase.
    ����1��� = models.CharField(max_length=50)
    ����1�ͺ� = models.CharField(max_length=50)
    ����1���_sn = models.CharField(db_column='����1���_SN', max_length=50)  # Field name made lowercase.
    ����2��� = models.CharField(max_length=50)
    ����2�ͺ� = models.CharField(max_length=50)
    ����2���_sn = models.CharField(db_column='����2���_SN', max_length=50)  # Field name made lowercase.
    ����3��� = models.CharField(max_length=50)
    ����3�ͺ� = models.CharField(max_length=50)
    ����3���_sn = models.CharField(db_column='����3���_SN', max_length=50)  # Field name made lowercase.
    ����4��� = models.CharField(max_length=50)
    ����4�ͺ� = models.CharField(max_length=50)
    ����4���_sn = models.CharField(db_column='����4���_SN', max_length=50)  # Field name made lowercase.
    ������� = models.CharField(max_length=50)
    �����ͺ� = models.CharField(max_length=50)
    �������_sn = models.CharField(db_column='�������_SN', max_length=50)  # Field name made lowercase.
    �Կ���� = models.CharField(max_length=50)
    �Կ��ͺ� = models.CharField(max_length=50)
    �Կ����sn = models.CharField(db_column='�Կ����SN', max_length=50)  # Field name made lowercase.
    �Կ��ӿ� = models.CharField(max_length=50)
    �Կ����� = models.CharField(max_length=50)
    ��Դ��� = models.CharField(max_length=50)
    ��Դ�ͺ� = models.CharField(max_length=50)
    ��Դ���_sn = models.CharField(db_column='��Դ���_SN', max_length=50)  # Field name made lowercase.
    ��Դ���� = models.CharField(max_length=50)
    ����� = models.CharField(max_length=50)
    Ӳ��1��� = models.CharField(max_length=50)
    Ӳ��1 = models.CharField(max_length=50)
    Ӳ��1���_sn = models.CharField(db_column='Ӳ��1���_SN', max_length=50)  # Field name made lowercase.
    Ӳ��1�ӿ� = models.CharField(max_length=50)
    Ӳ��1���� = models.CharField(max_length=50)
    Ӳ��2��� = models.CharField(max_length=50)
    Ӳ��2 = models.CharField(max_length=50)
    Ӳ��2���sn = models.CharField(db_column='Ӳ��2���SN', max_length=50)  # Field name made lowercase.
    Ӳ��2�ӿ� = models.CharField(max_length=50)
    Ӳ��2���� = models.CharField(max_length=50)
    Ӳ��3��� = models.CharField(max_length=50)
    Ӳ��3 = models.CharField(max_length=50)
    Ӳ��3���_sn = models.CharField(db_column='Ӳ��3���_SN', max_length=50)  # Field name made lowercase.
    Ӳ��3�ӿ� = models.CharField(max_length=50)
    Ӳ��3���� = models.CharField(max_length=50)
    Ӳ��4��� = models.CharField(max_length=50)
    Ӳ��4 = models.CharField(max_length=50)
    Ӳ��4���_sn = models.CharField(db_column='Ӳ��4���_SN', max_length=50)  # Field name made lowercase.
    Ӳ��4�ӿ� = models.CharField(max_length=50)
    Ӳ��4���� = models.CharField(max_length=50)
    �ڴ�1��� = models.CharField(max_length=50)
    �ڴ�1 = models.CharField(max_length=50)
    �ڴ�1���_sn = models.CharField(db_column='�ڴ�1���_SN', max_length=50)  # Field name made lowercase.
    �ڴ�1�ӿ� = models.CharField(max_length=50)
    �ڴ�1���� = models.CharField(max_length=50)
    �ڴ�2��� = models.CharField(max_length=50)
    �ڴ�2 = models.CharField(max_length=50)
    �ڴ�2���_sn = models.CharField(db_column='�ڴ�2���_SN', max_length=50)  # Field name made lowercase.
    �ڴ�2�ӿ� = models.CharField(max_length=50)
    �ڴ�2���� = models.CharField(max_length=50)
    �ڴ�3��� = models.CharField(max_length=50)
    �ڴ�3 = models.CharField(max_length=50)
    �ڴ�3���_sn = models.CharField(db_column='�ڴ�3���_SN', max_length=50)  # Field name made lowercase.
    �ڴ�3�ӿ� = models.CharField(max_length=50)
    �ڴ�3���� = models.CharField(max_length=50)
    �ڴ�4��� = models.CharField(max_length=50)
    �ڴ�4 = models.CharField(max_length=50)
    �ڴ�4���_sn = models.CharField(db_column='�ڴ�4���_SN', max_length=50)  # Field name made lowercase.
    �ڴ�4�ӿ� = models.CharField(max_length=50)
    �ڴ�4���� = models.CharField(max_length=50)
    ����1��� = models.CharField(max_length=50)
    ����1 = models.CharField(max_length=50)
    ����1���_sn = models.CharField(db_column='����1���_SN', max_length=50)  # Field name made lowercase.
    ����1�ӿ� = models.CharField(max_length=50)
    ����1���� = models.CharField(max_length=50)
    ����2��� = models.CharField(max_length=50)
    ����2 = models.CharField(max_length=50)
    ����2���_sn = models.CharField(db_column='����2���_SN', max_length=50)  # Field name made lowercase.
    ����2�ӿ� = models.CharField(max_length=50)
    ����2���� = models.CharField(max_length=50)
    ������ = models.CharField(max_length=50)
    ���� = models.CharField(max_length=50)
    �������_sn = models.CharField(db_column='�������_SN', max_length=50)  # Field name made lowercase.
    ��ʾ����� = models.CharField(max_length=50)
    ��ʾ���ͺ� = models.CharField(max_length=50)
    ��ʾ�����_sn = models.CharField(db_column='��ʾ�����_SN', max_length=50)  # Field name made lowercase.
    ��ʾ������ = models.CharField(max_length=50)
    ��ʾ���ߴ� = models.CharField(max_length=50)
    ���̱�� = models.CharField(max_length=50)
    �����ͺ� = models.CharField(max_length=50)
    �������_sn = models.CharField(db_column='�������_SN', max_length=50)  # Field name made lowercase.
    ���̽ӿ� = models.CharField(max_length=50)
    �������� = models.CharField(max_length=50)
    ����� = models.CharField(max_length=50)
    ����ͺ� = models.CharField(max_length=50)
    ������_sn = models.CharField(db_column='������_SN', max_length=50)  # Field name made lowercase.
    ���ӿ� = models.CharField(max_length=50)
    ������� = models.CharField(max_length=50)
    �˺� = models.CharField(max_length=50)
    ��ȫ���� = models.CharField(max_length=50)
    ip��ַ1 = models.CharField(db_column='IP��ַ1', max_length=50)  # Field name made lowercase.
    ip��ַ2 = models.CharField(db_column='IP��ַ2', max_length=50)  # Field name made lowercase.
    ip��ַ3 = models.CharField(db_column='IP��ַ3', max_length=50)  # Field name made lowercase.
    ip��ַ4 = models.CharField(db_column='IP��ַ4', max_length=50)  # Field name made lowercase.
    mac��ַ1 = models.CharField(db_column='MAC��ַ1', max_length=50)  # Field name made lowercase.
    mac��ַ2 = models.CharField(db_column='MAC��ַ2', max_length=50)  # Field name made lowercase.
    mac��ַ3 = models.CharField(db_column='MAC��ַ3', max_length=50)  # Field name made lowercase.
    mac��ַ4 = models.CharField(db_column='MAC��ַ4', max_length=50)  # Field name made lowercase.
    �绰���� = models.CharField(max_length=50)
    ���Ѷ�� = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    �Զ���1 = models.CharField(max_length=100)
    �Զ���2 = models.CharField(max_length=100)
    �Զ���3 = models.CharField(max_length=100)
    �Զ���4 = models.CharField(max_length=100)
    �Զ���5 = models.CharField(max_length=100)
    �Զ���6 = models.CharField(max_length=100)
    �Զ���7 = models.CharField(max_length=100)
    �Զ���8 = models.CharField(max_length=100)
    �Զ���9 = models.CharField(max_length=100)
    �Զ���10 = models.CharField(max_length=100)
    �Զ���11 = models.CharField(max_length=100)
    �Զ���12 = models.CharField(max_length=100)
    �Զ���13 = models.CharField(max_length=100)
    �Զ���14 = models.CharField(max_length=100)
    �Զ���15 = models.CharField(max_length=100)
    �Զ���16 = models.CharField(max_length=100)
    �Զ���17 = models.CharField(max_length=100)
    �Զ���18 = models.CharField(max_length=100)
    �Զ���19 = models.CharField(max_length=100)
    �Զ���20 = models.CharField(max_length=100)
    �Զ���21 = models.CharField(max_length=100)
    �Զ���22 = models.CharField(max_length=100)
    �Զ���23 = models.CharField(max_length=100)
    �Զ���24 = models.CharField(max_length=100)
    �Զ���25 = models.CharField(max_length=100)
    �Զ���26 = models.CharField(max_length=100)
    �Զ���27 = models.CharField(max_length=100)
    �Զ���28 = models.CharField(max_length=100)
    �Զ���29 = models.CharField(max_length=100)
    �Զ���30 = models.CharField(max_length=100)
    ��ע = models.CharField(max_length=100)
    �Ƶ��� = models.CharField(max_length=20)
    �Ƶ����� = models.DateTimeField(blank=True, null=True)
    ������ = models.CharField(max_length=20)
    �������� = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IT�ʲ�����'


class It(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ���� = models.CharField(max_length=50)
    ֵ = models.CharField(max_length=50)
    ��ע = models.CharField(max_length=100)
    �Ƶ��� = models.CharField(max_length=20)
    �Ƶ����� = models.DateTimeField(blank=True, null=True)
    ������ = models.CharField(max_length=20)
    �������� = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IT�ʲ����������������'


class Leffspkcb(models.Model):
    �����ֿ� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ���� = models.CharField(max_length=50)
    ��λ = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ���� = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LEFFSPKCB'


class LogLogin(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', primary_key=True, max_length=36)  # Field name made lowercase.
    app_name = models.CharField(db_column='App_Name', max_length=128, blank=True, null=True)  # Field name made lowercase.
    app_version = models.CharField(db_column='App_Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_no = models.CharField(db_column='User_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(db_column='Account_Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    login_res = models.BooleanField(db_column='Login_Res', blank=True, null=True)  # Field name made lowercase.
    login_message = models.CharField(db_column='Login_Message', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sql_spid = models.IntegerField(db_column='SQL_SPID', blank=True, null=True)  # Field name made lowercase.
    sql_user = models.CharField(db_column='SQL_User', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Log_Login'


class LogLogout(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    date = models.DateTimeField()
    guid = models.ForeignKey(LogLogin, models.DO_NOTHING, db_column='Guid')  # Field name made lowercase.
    is_exception = models.BooleanField(db_column='Is_exception')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Log_Logout'


class PrCpylb(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    spmc = models.CharField(db_column='SPMC', max_length=50)  # Field name made lowercase.
    spdm1 = models.CharField(db_column='SPDM1', max_length=50)  # Field name made lowercase.
    spmc1 = models.CharField(db_column='SPMC1', max_length=50)  # Field name made lowercase.
    wjys = models.CharField(db_column='WJYS', max_length=50)  # Field name made lowercase.
    ml1_dm = models.CharField(db_column='ML1_DM', max_length=50)  # Field name made lowercase.
    ml1_bhyl = models.DecimalField(db_column='ML1_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    ml2_dm = models.CharField(db_column='ML2_DM', max_length=50)  # Field name made lowercase.
    ml2_bhyl = models.DecimalField(db_column='ML2_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    ml3_dm = models.CharField(db_column='ML3_DM', max_length=50)  # Field name made lowercase.
    ml3_bhyl = models.DecimalField(db_column='ML3_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    lb1_dm = models.CharField(db_column='LB1_DM', max_length=50)  # Field name made lowercase.
    lb1_bhyl = models.DecimalField(db_column='LB1_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    lb2_dm = models.CharField(db_column='LB2_DM', max_length=50)  # Field name made lowercase.
    lb2_bhyl = models.DecimalField(db_column='LB2_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    pl1_dm = models.CharField(db_column='PL1_DM', max_length=50)  # Field name made lowercase.
    pl1_bhyl = models.DecimalField(db_column='PL1_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    pl2_dm = models.CharField(db_column='PL2_DM', max_length=50)  # Field name made lowercase.
    pl2_bhyl = models.DecimalField(db_column='PL2_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    pl3_dm = models.CharField(db_column='PL3_DM', max_length=50)  # Field name made lowercase.
    pl3_bhyl = models.DecimalField(db_column='PL3_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    zd1_dm = models.CharField(db_column='ZD1_DM', max_length=50)  # Field name made lowercase.
    zd1_bhyl = models.DecimalField(db_column='ZD1_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    zd2_dm = models.CharField(db_column='ZD2_DM', max_length=50)  # Field name made lowercase.
    zd2_bhyl = models.DecimalField(db_column='ZD2_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    zd3_dm = models.CharField(db_column='ZD3_DM', max_length=50)  # Field name made lowercase.
    zd3_bhyl = models.DecimalField(db_column='ZD3_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    zd4_dm = models.CharField(db_column='ZD4_DM', max_length=50)  # Field name made lowercase.
    zd4_bhyl = models.DecimalField(db_column='ZD4_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj1_dm = models.CharField(db_column='WJ1_DM', max_length=50)  # Field name made lowercase.
    wj1_bhyl = models.DecimalField(db_column='WJ1_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj2_dm = models.CharField(db_column='WJ2_DM', max_length=50)  # Field name made lowercase.
    wj2_bhyl = models.DecimalField(db_column='WJ2_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj3_dm = models.CharField(db_column='WJ3_DM', max_length=50)  # Field name made lowercase.
    wj3_bhyl = models.DecimalField(db_column='WJ3_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj4_dm = models.CharField(db_column='WJ4_DM', max_length=50)  # Field name made lowercase.
    wj4_bhyl = models.DecimalField(db_column='WJ4_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj5_dm = models.CharField(db_column='WJ5_DM', max_length=50)  # Field name made lowercase.
    wj5_bhyl = models.DecimalField(db_column='WJ5_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj6_dm = models.CharField(db_column='WJ6_DM', max_length=50)  # Field name made lowercase.
    wj6_bhyl = models.DecimalField(db_column='WJ6_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj7_dm = models.CharField(db_column='WJ7_DM', max_length=50)  # Field name made lowercase.
    wj7_bhyl = models.DecimalField(db_column='WJ7_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj8_dm = models.CharField(db_column='WJ8_DM', max_length=50)  # Field name made lowercase.
    wj8_bhyl = models.DecimalField(db_column='WJ8_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj9_dm = models.CharField(db_column='WJ9_DM', max_length=50)  # Field name made lowercase.
    wj9_bhyl = models.DecimalField(db_column='WJ9_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj10_dm = models.CharField(db_column='WJ10_DM', max_length=50)  # Field name made lowercase.
    wj10_bhyl = models.DecimalField(db_column='WJ10_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj11_dm = models.CharField(db_column='WJ11_DM', max_length=50)  # Field name made lowercase.
    wj11_bhyl = models.DecimalField(db_column='WJ11_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj12_dm = models.CharField(db_column='WJ12_DM', max_length=50)  # Field name made lowercase.
    wj12_bhyl = models.DecimalField(db_column='WJ12_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj13_dm = models.CharField(db_column='WJ13_DM', max_length=50)  # Field name made lowercase.
    wj13_bhyl = models.DecimalField(db_column='WJ13_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj14_dm = models.CharField(db_column='WJ14_DM', max_length=50)  # Field name made lowercase.
    wj14_bhyl = models.DecimalField(db_column='WJ14_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj15_dm = models.CharField(db_column='WJ15_DM', max_length=50)  # Field name made lowercase.
    wj15_bhyl = models.DecimalField(db_column='WJ15_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    wj16_dm = models.CharField(db_column='WJ16_DM', max_length=50)  # Field name made lowercase.
    wj16_bhyl = models.DecimalField(db_column='WJ16_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    ot1_dm = models.CharField(db_column='OT1_DM', max_length=50)  # Field name made lowercase.
    ot1_bhyl = models.DecimalField(db_column='OT1_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    ot2_dm = models.CharField(db_column='OT2_DM', max_length=50)  # Field name made lowercase.
    ot2_bhyl = models.DecimalField(db_column='OT2_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    ot3_dm = models.CharField(db_column='OT3_DM', max_length=50)  # Field name made lowercase.
    ot3_bhyl = models.DecimalField(db_column='OT3_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    ot4_dm = models.CharField(db_column='OT4_DM', max_length=50)  # Field name made lowercase.
    ot4_bhyl = models.DecimalField(db_column='OT4_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    ot5_dm = models.CharField(db_column='OT5_DM', max_length=50)  # Field name made lowercase.
    ot5_bhyl = models.DecimalField(db_column='OT5_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    ot6_dm = models.CharField(db_column='OT6_DM', max_length=50)  # Field name made lowercase.
    ot6_bhyl = models.DecimalField(db_column='OT6_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    bz1_dm = models.CharField(db_column='BZ1_DM', max_length=50)  # Field name made lowercase.
    bz1_bhyl = models.DecimalField(db_column='BZ1_BHYL', max_digits=18, decimal_places=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PR_CPYLB'


class PrCpylbJc(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    spmc = models.CharField(db_column='SPMC', max_length=50)  # Field name made lowercase.
    wjys = models.CharField(db_column='WJYS', max_length=50)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=50)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.
    gxr = models.CharField(db_column='GXR', max_length=50)  # Field name made lowercase.
    gxrq = models.DateTimeField(db_column='GXRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PR_CPYLB_JC'


class PrCpylbJcmx(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    gyswldm = models.CharField(db_column='GYSWLDM', max_length=50)  # Field name made lowercase.
    gysmc = models.CharField(db_column='GYSMC', max_length=50)  # Field name made lowercase.
    wldm = models.CharField(db_column='WLDM', max_length=50)  # Field name made lowercase.
    wlmc = models.CharField(db_column='WLMC', max_length=50)  # Field name made lowercase.
    bzyl = models.DecimalField(db_column='BZYL', max_digits=18, decimal_places=5)  # Field name made lowercase.
    yldw = models.CharField(db_column='YLDW', max_length=50)  # Field name made lowercase.
    wldj = models.DecimalField(db_column='WLDJ', max_digits=18, decimal_places=3)  # Field name made lowercase.
    lx = models.CharField(db_column='LX', max_length=50)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=100)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.
    gxr = models.CharField(db_column='GXR', max_length=50)  # Field name made lowercase.
    gxrq = models.DateTimeField(db_column='GXRQ', blank=True, null=True)  # Field name made lowercase.
    sl = models.IntegerField(db_column='SL')  # Field name made lowercase.
    zl = models.DecimalField(db_column='ZL', max_digits=29, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    wlkc = models.IntegerField(db_column='WLKC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PR_CPYLB_JCMX'


class PrCpylbJcrz(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    wldm = models.CharField(db_column='WLDM', max_length=50)  # Field name made lowercase.
    zdname = models.CharField(db_column='ZDNAME', max_length=50)  # Field name made lowercase.
    contents = models.CharField(db_column='Contents', max_length=250)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=100)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PR_CPYLB_JCRZ'


class PrCpylbLx(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    lx = models.CharField(db_column='LX', max_length=50)  # Field name made lowercase.
    lxmc = models.CharField(db_column='LXMC', max_length=50)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=100)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.
    gxr = models.CharField(db_column='GXR', max_length=50)  # Field name made lowercase.
    gxrq = models.DateTimeField(db_column='GXRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PR_CPYLB_LX'


class PrCpylbYldw(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    yldw = models.CharField(db_column='YLDW', max_length=50)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=100)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.
    gxr = models.CharField(db_column='GXR', max_length=50)  # Field name made lowercase.
    gxrq = models.DateTimeField(db_column='GXRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PR_CPYLB_YLDW'


class PrJscpylbSpdm(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    sl = models.IntegerField(db_column='SL')  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=50)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PR_JSCPYLB_SPDM'


class PrXhjlb(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ΨƷ����� = models.CharField(max_length=50, blank=True, null=True)
    ΨƷ����Ʒ���� = models.CharField(max_length=50, blank=True, null=True)
    ���Ƿ� = models.CharField(max_length=50, blank=True, null=True)
    �з����� = models.CharField(max_length=50, blank=True, null=True)
    Ʒ�� = models.CharField(max_length=50, blank=True, null=True)
    ��Ʒ״̬ = models.CharField(max_length=50, blank=True, null=True)
    �������� = models.CharField(max_length=50, blank=True, null=True)
    �ֹ��� = models.CharField(max_length=50, blank=True, null=True)
    ԭ���� = models.CharField(max_length=300, blank=True, null=True)
    ������ = models.CharField(max_length=50, blank=True, null=True)
    ͬ�ߴ������� = models.CharField(max_length=50)
    ͬ�ߴ��˿ӡ�� = models.CharField(max_length=50)
    ������ͬ�� = models.CharField(max_length=50)
    ��ע = models.CharField(max_length=250)
    �Ƶ��� = models.CharField(max_length=50)
    �Ƶ����� = models.DateTimeField(blank=True, null=True)
    ������ = models.CharField(max_length=50)
    �������� = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PR_XHJLB'


class PrXhjlbRz(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    �����ֶ����� = models.CharField(max_length=50)
    ����˵�� = models.CharField(max_length=250)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ע = models.CharField(max_length=250)
    �Ƶ��� = models.CharField(max_length=50)
    �Ƶ����� = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PR_XHJLB_RZ'


class SpSpjgb(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    dpj = models.DecimalField(db_column='DPJ', max_digits=18, decimal_places=2)  # Field name made lowercase.
    ykj = models.DecimalField(db_column='YKJ', max_digits=18, decimal_places=2)  # Field name made lowercase.
    rcj = models.DecimalField(db_column='RCJ', max_digits=18, decimal_places=2)  # Field name made lowercase.
    wdbj = models.DecimalField(db_column='WDBJ', max_digits=18, decimal_places=2)  # Field name made lowercase.
    leffj = models.DecimalField(db_column='LEFFJ', max_digits=18, decimal_places=2)  # Field name made lowercase.
    hdj = models.DecimalField(db_column='HDJ', max_digits=18, decimal_places=2)  # Field name made lowercase.
    nzhdj = models.DecimalField(db_column='NZHDJ', max_digits=18, decimal_places=2)  # Field name made lowercase.
    ml = models.DecimalField(db_column='ML', max_digits=18, decimal_places=2)  # Field name made lowercase.
    jgf = models.DecimalField(db_column='JGF', max_digits=18, decimal_places=2)  # Field name made lowercase.
    ygj = models.DecimalField(db_column='YGJ', max_digits=18, decimal_places=2)  # Field name made lowercase.
    hsj = models.DecimalField(db_column='HSJ', max_digits=18, decimal_places=2)  # Field name made lowercase.
    bz = models.CharField(max_length=300)
    zdr = models.CharField(max_length=50)
    zdrq = models.DateTimeField(blank=True, null=True)
    gxr = models.CharField(max_length=50)
    gxrq = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SP_SPJGB'


class SpWeeks(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    sjrq = models.DateTimeField(db_column='SJRQ', blank=True, null=True)  # Field name made lowercase.
    sjts = models.IntegerField(db_column='SJTS', blank=True, null=True)  # Field name made lowercase.
    w1rq = models.DateTimeField(db_column='W1RQ', blank=True, null=True)  # Field name made lowercase.
    w2rq = models.DateTimeField(db_column='W2RQ', blank=True, null=True)  # Field name made lowercase.
    w3rq = models.DateTimeField(db_column='W3RQ', blank=True, null=True)  # Field name made lowercase.
    w4rq = models.DateTimeField(db_column='W4RQ', blank=True, null=True)  # Field name made lowercase.
    w5rq = models.DateTimeField(db_column='W5RQ', blank=True, null=True)  # Field name made lowercase.
    w6rq = models.DateTimeField(db_column='W6RQ', blank=True, null=True)  # Field name made lowercase.
    w1xl = models.IntegerField(db_column='W1XL', blank=True, null=True)  # Field name made lowercase.
    w2xl = models.IntegerField(db_column='W2XL', blank=True, null=True)  # Field name made lowercase.
    w3xl = models.IntegerField(db_column='W3XL', blank=True, null=True)  # Field name made lowercase.
    w4xl = models.IntegerField(db_column='W4XL', blank=True, null=True)  # Field name made lowercase.
    w5xl = models.IntegerField(db_column='W5XL', blank=True, null=True)  # Field name made lowercase.
    w6xl = models.IntegerField(db_column='W6XL', blank=True, null=True)  # Field name made lowercase.
    w1xllx = models.CharField(db_column='W1XLLX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    w2xllx = models.CharField(db_column='W2XLLX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    w3xllx = models.CharField(db_column='W3XLLX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    w4xllx = models.CharField(db_column='W4XLLX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    w5xllx = models.CharField(db_column='W5XLLX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    w6xllx = models.CharField(db_column='W6XLLX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ts = models.DateTimeField(db_column='TS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_WEEKS'


class SpXpsxjcb(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    pp = models.CharField(max_length=50)
    sx = models.CharField(max_length=30)
    lb = models.CharField(max_length=30)
    bz = models.CharField(max_length=300)
    zdr = models.CharField(max_length=50)
    zdrq = models.DateTimeField(blank=True, null=True)
    gxr = models.CharField(max_length=50)
    gxrq = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SP_XPSXJCB'


class SpXpsxls(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    Ʒ�� = models.CharField(max_length=50)
    ���� = models.CharField(max_length=50)
    ���� = models.IntegerField()
    ����ռ�� = models.CharField(max_length=50)
    ��� = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sku = models.IntegerField(db_column='SKU')  # Field name made lowercase.
    skuռ�� = models.CharField(db_column='SKUռ��', max_length=50)  # Field name made lowercase.
    spu = models.IntegerField(db_column='SPU')  # Field name made lowercase.
    ��� = models.CharField(max_length=50)
    �·� = models.CharField(max_length=50)
    bz = models.CharField(max_length=300)
    zdr = models.CharField(max_length=50)
    zdrq = models.DateTimeField(blank=True, null=True)
    gxr = models.CharField(max_length=50)
    gxrq = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SP_XPSXLS'


class SpZdysj(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    sqlstr = models.CharField(db_column='SQLstr', max_length=5000)  # Field name made lowercase.
    where = models.CharField(max_length=500)
    groupby = models.CharField(max_length=500)
    orderby = models.CharField(max_length=500)
    lx = models.CharField(max_length=50)
    bz = models.CharField(max_length=300)
    zdr = models.CharField(max_length=50)
    zdrq = models.DateTimeField(blank=True, null=True)
    gxr = models.CharField(max_length=50)
    gxrq = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SP_ZDYSJ'


class StPhdbd(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    djbh = models.CharField(db_column='DJBH', max_length=50)  # Field name made lowercase.
    sd = models.BooleanField(db_column='SD')  # Field name made lowercase.
    sdrq = models.DateTimeField(db_column='SDRQ', blank=True, null=True)  # Field name made lowercase.
    ys = models.BooleanField(db_column='YS')  # Field name made lowercase.
    ysrq = models.DateTimeField(db_column='YSRQ', blank=True, null=True)  # Field name made lowercase.
    lx = models.CharField(db_column='LX', max_length=50)  # Field name made lowercase.
    ts = models.DateTimeField(db_column='TS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ST_PHDBD'


class StPhdbdmx(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    djbh = models.CharField(db_column='DJBH', max_length=50)  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    glck = models.CharField(db_column='GLCK', max_length=50)  # Field name made lowercase.
    kw = models.CharField(db_column='KW', max_length=50)  # Field name made lowercase.
    dbkw = models.CharField(db_column='DBKW', max_length=50)  # Field name made lowercase.
    qy = models.CharField(db_column='QY', max_length=50)  # Field name made lowercase.
    xs = models.IntegerField(db_column='XS')  # Field name made lowercase.
    num = models.IntegerField(db_column='NUM')  # Field name made lowercase.
    ppkw = models.CharField(db_column='PPKW', max_length=50)  # Field name made lowercase.
    ppxs = models.IntegerField(db_column='PPXS')  # Field name made lowercase.
    ppsl = models.IntegerField(db_column='PPSL')  # Field name made lowercase.
    isok = models.BooleanField(db_column='ISOK')  # Field name made lowercase.
    iscancel = models.BooleanField(db_column='ISCancel')  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=200)  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.
    gxr = models.CharField(db_column='GXR', max_length=50)  # Field name made lowercase.
    gxrq = models.DateTimeField(db_column='GXRQ', blank=True, null=True)  # Field name made lowercase.
    ts = models.DateTimeField(db_column='TS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ST_PHDBDMX'


class StPhdbdqd(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    djbh = models.CharField(db_column='DJBH', max_length=50)  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    kw = models.CharField(db_column='KW', max_length=50)  # Field name made lowercase.
    quyu = models.CharField(db_column='QUYU', max_length=50)  # Field name made lowercase.
    ck = models.CharField(db_column='CK', max_length=50)  # Field name made lowercase.
    xs = models.IntegerField(db_column='XS')  # Field name made lowercase.
    sl = models.IntegerField(db_column='SL')  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=2)  # Field name made lowercase.
    ts = models.DateTimeField(db_column='TS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ST_PHDBDQD'


class StPhdbdNo(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    djbh = models.CharField(db_column='DJBH', max_length=50)  # Field name made lowercase.
    ts = models.DateTimeField(db_column='TS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ST_PHDBD_NO'


class TsMrsj(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    zdname = models.CharField(db_column='ZDNAME', max_length=200)  # Field name made lowercase.
    zdz = models.CharField(db_column='ZDZ', max_length=100)  # Field name made lowercase.
    zdlx = models.CharField(db_column='ZDLX', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50)  # Field name made lowercase.
    ts = models.DateTimeField(db_column='TS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TS_MRSJ'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ddsczt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    djbh = models.CharField(db_column='DJBH', max_length=50)  # Field name made lowercase.
    xdxh = models.CharField(db_column='XDXH', max_length=50)  # Field name made lowercase.
    ddlx = models.CharField(db_column='DDLX', max_length=50)  # Field name made lowercase.
    pp = models.CharField(db_column='PP', max_length=50)  # Field name made lowercase.
    spdm = models.CharField(db_column='SPDM', max_length=50)  # Field name made lowercase.
    spmc = models.CharField(db_column='SPMC', max_length=50)  # Field name made lowercase.
    pic = models.TextField(db_column='PIC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sjs = models.CharField(db_column='SJS', max_length=50)  # Field name made lowercase.
    cplx = models.CharField(db_column='CPLX', max_length=50)  # Field name made lowercase.
    ys = models.CharField(db_column='YS', max_length=50)  # Field name made lowercase.
    sl = models.IntegerField(db_column='SL')  # Field name made lowercase.
    fd = models.BooleanField(db_column='FD', blank=True, null=True)  # Field name made lowercase.
    xslx = models.CharField(db_column='XSLX', max_length=50)  # Field name made lowercase.
    rgdj = models.IntegerField(db_column='RGDJ')  # Field name made lowercase.
    gc = models.CharField(db_column='GC', max_length=50)  # Field name made lowercase.
    gcry = models.IntegerField(db_column='GCRY', blank=True, null=True)  # Field name made lowercase.
    gcpprs = models.IntegerField(db_column='GCPPRS', blank=True, null=True)  # Field name made lowercase.
    gcbybs = models.IntegerField(db_column='GCBYBS', blank=True, null=True)  # Field name made lowercase.
    gcryzgs = models.IntegerField(db_column='GCRYZGS', blank=True, null=True)  # Field name made lowercase.
    ddzgs = models.IntegerField(db_column='DDZGS', blank=True, null=True)  # Field name made lowercase.
    byxdsl = models.IntegerField(db_column='BYXDSL', blank=True, null=True)  # Field name made lowercase.
    gszb = models.CharField(db_column='GSZB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rycn = models.IntegerField(db_column='RYCN', blank=True, null=True)  # Field name made lowercase.
    qc = models.CharField(db_column='QC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spxd = models.DateTimeField(db_column='SPXD', blank=True, null=True)  # Field name made lowercase.
    spxq = models.DateTimeField(db_column='SPXQ', blank=True, null=True)  # Field name made lowercase.
    spsczq = models.IntegerField(db_column='SPSCZQ', blank=True, null=True)  # Field name made lowercase.
    scts = models.IntegerField(db_column='SCTS', blank=True, null=True)  # Field name made lowercase.
    djrq = models.DateTimeField(db_column='DJRQ', blank=True, null=True)  # Field name made lowercase.
    htjg = models.IntegerField(db_column='HTJG', blank=True, null=True)  # Field name made lowercase.
    xxbrq = models.DateTimeField(db_column='XXBRQ', blank=True, null=True)  # Field name made lowercase.
    qryrq = models.DateTimeField(db_column='QRYRQ', blank=True, null=True)  # Field name made lowercase.
    zgrq = models.DateTimeField(db_column='ZGRQ', blank=True, null=True)  # Field name made lowercase.
    ddrq = models.DateTimeField(db_column='DDRQ', blank=True, null=True)  # Field name made lowercase.
    qsyrq = models.DateTimeField(db_column='QSYRQ', blank=True, null=True)  # Field name made lowercase.
    qsyxjts = models.IntegerField(db_column='QSYXJTS', blank=True, null=True)  # Field name made lowercase.
    qsycs = models.IntegerField(db_column='QSYCS', blank=True, null=True)  # Field name made lowercase.
    qsyrq1 = models.DateTimeField(db_column='QSYRQ1', blank=True, null=True)  # Field name made lowercase.
    dhtgrq = models.DateTimeField(db_column='DHTGRQ', blank=True, null=True)  # Field name made lowercase.
    htrq = models.DateTimeField(db_column='HTRQ', blank=True, null=True)  # Field name made lowercase.
    ddzq = models.IntegerField(db_column='DDZQ', blank=True, null=True)  # Field name made lowercase.
    spxqcy = models.IntegerField(db_column='SPXQCY', blank=True, null=True)  # Field name made lowercase.
    wlzt = models.CharField(db_column='WLZT', max_length=50)  # Field name made lowercase.
    wlrq = models.DateTimeField(db_column='WLRQ', blank=True, null=True)  # Field name made lowercase.
    mlrq = models.DateTimeField(db_column='MLRQ', blank=True, null=True)  # Field name made lowercase.
    llrq = models.DateTimeField(db_column='LLRQ', blank=True, null=True)  # Field name made lowercase.
    wjrq = models.DateTimeField(db_column='WJRQ', blank=True, null=True)  # Field name made lowercase.
    llrq1 = models.DateTimeField(db_column='LLRQ1', blank=True, null=True)  # Field name made lowercase.
    dplq = models.DateTimeField(db_column='DPLQ', blank=True, null=True)  # Field name made lowercase.
    tzlq = models.DateTimeField(db_column='TZLQ', blank=True, null=True)  # Field name made lowercase.
    dwwlrq = models.DateTimeField(db_column='DWWLRQ', blank=True, null=True)  # Field name made lowercase.
    zq01 = models.IntegerField(db_column='ZQ01', blank=True, null=True)  # Field name made lowercase.
    gyqp = models.DateTimeField(db_column='GYQP', blank=True, null=True)  # Field name made lowercase.
    wlwjrq = models.DateTimeField(db_column='WLWJRQ', blank=True, null=True)  # Field name made lowercase.
    wlwjjg = models.BooleanField(db_column='WLWJJG', blank=True, null=True)  # Field name made lowercase.
    wlsjrq = models.DateTimeField(db_column='WLSJRQ', blank=True, null=True)  # Field name made lowercase.
    wlsjjg = models.BooleanField(db_column='WLSJJG', blank=True, null=True)  # Field name made lowercase.
    wlqp = models.DateTimeField(db_column='WLQP', blank=True, null=True)  # Field name made lowercase.
    cqyrq = models.DateTimeField(db_column='CQYRQ', blank=True, null=True)  # Field name made lowercase.
    zq02 = models.IntegerField(db_column='ZQ02', blank=True, null=True)  # Field name made lowercase.
    gcyf = models.BooleanField(db_column='GCYF', blank=True, null=True)  # Field name made lowercase.
    jhsx = models.DateTimeField(db_column='JHSX', blank=True, null=True)  # Field name made lowercase.
    kskl = models.DateTimeField(db_column='KSKL', blank=True, null=True)  # Field name made lowercase.
    kljd = models.CharField(db_column='KLJD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tmjd = models.CharField(db_column='TMJD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zcjd = models.CharField(db_column='ZCJD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drrs = models.IntegerField(db_column='DRRS', blank=True, null=True)  # Field name made lowercase.
    ljrs = models.IntegerField(db_column='LJRS', blank=True, null=True)  # Field name made lowercase.
    cpjd = models.CharField(db_column='CPJD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ksbzrq = models.DateTimeField(db_column='KSBZRQ', blank=True, null=True)  # Field name made lowercase.
    bzjd = models.CharField(db_column='BZJD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ycbz = models.CharField(db_column='YCBZ', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sjjy = models.DateTimeField(db_column='SJJY', blank=True, null=True)  # Field name made lowercase.
    bzwc = models.DateTimeField(db_column='BZWC', blank=True, null=True)  # Field name made lowercase.
    cpjysl = models.IntegerField(db_column='CPJYSL', blank=True, null=True)  # Field name made lowercase.
    cpjg = models.BooleanField(db_column='CPJG', blank=True, null=True)  # Field name made lowercase.
    yysh = models.DateTimeField(db_column='YYSH', blank=True, null=True)  # Field name made lowercase.
    ljshcs = models.IntegerField(db_column='LJSHCS', blank=True, null=True)  # Field name made lowercase.
    yyshsl = models.IntegerField(db_column='YYSHSL', blank=True, null=True)  # Field name made lowercase.
    ljshsl = models.IntegerField(db_column='LJSHSL', blank=True, null=True)  # Field name made lowercase.
    rdycrq = models.DateTimeField(db_column='RDYCRQ', blank=True, null=True)  # Field name made lowercase.
    njrq = models.DateTimeField(db_column='NJRQ', blank=True, null=True)  # Field name made lowercase.
    njlqrq = models.IntegerField(db_column='NJLQRQ', blank=True, null=True)  # Field name made lowercase.
    njhgsl = models.IntegerField(db_column='NJHGSL', blank=True, null=True)  # Field name made lowercase.
    ljthsl = models.IntegerField(db_column='LJTHSL', blank=True, null=True)  # Field name made lowercase.
    cpsl = models.IntegerField(db_column='CPSL', blank=True, null=True)  # Field name made lowercase.
    ytghssl = models.IntegerField(db_column='YTGHSSL', blank=True, null=True)  # Field name made lowercase.
    fxhhrq = models.DateTimeField(db_column='FXHHRQ', blank=True, null=True)  # Field name made lowercase.
    sl1 = models.IntegerField(db_column='SL1', blank=True, null=True)  # Field name made lowercase.
    yqrq = models.DateTimeField(db_column='YQRQ', blank=True, null=True)  # Field name made lowercase.
    yqsl = models.IntegerField(db_column='YQSL', blank=True, null=True)  # Field name made lowercase.
    qddzs = models.IntegerField(db_column='QDDZS', blank=True, null=True)  # Field name made lowercase.
    zjrq = models.DateTimeField(db_column='ZJRQ', blank=True, null=True)  # Field name made lowercase.
    rzcrq = models.DateTimeField(db_column='RZCRQ', blank=True, null=True)  # Field name made lowercase.
    rzcsl = models.IntegerField(db_column='RZCSL', blank=True, null=True)  # Field name made lowercase.
    jhjhrq = models.DateTimeField(db_column='JHJHRQ', blank=True, null=True)  # Field name made lowercase.
    ddgbrq = models.DateTimeField(db_column='DDGBRQ', blank=True, null=True)  # Field name made lowercase.
    zq03 = models.IntegerField(db_column='ZQ03', blank=True, null=True)  # Field name made lowercase.
    zq04 = models.IntegerField(db_column='ZQ04', blank=True, null=True)  # Field name made lowercase.
    zq04rq = models.DateTimeField(db_column='ZQ04RQ', blank=True, null=True)  # Field name made lowercase.
    bf90rq = models.DateTimeField(db_column='BF90RQ', blank=True, null=True)  # Field name made lowercase.
    zq05 = models.IntegerField(db_column='ZQ05', blank=True, null=True)  # Field name made lowercase.
    xdd60ts = models.IntegerField(db_column='XDD60TS', blank=True, null=True)  # Field name made lowercase.
    xdd90ts = models.IntegerField(db_column='XDD90TS', blank=True, null=True)  # Field name made lowercase.
    zr = models.IntegerField(db_column='ZR', blank=True, null=True)  # Field name made lowercase.
    sp = models.CharField(db_column='SP', max_length=50)  # Field name made lowercase.
    zz = models.CharField(db_column='ZZ', max_length=50)  # Field name made lowercase.
    ddzt = models.CharField(db_column='DDZT', max_length=50)  # Field name made lowercase.
    sc = models.CharField(db_column='SC', max_length=50)  # Field name made lowercase.
    xz = models.BooleanField(db_column='XZ')  # Field name made lowercase.
    zdr = models.CharField(db_column='ZDR', max_length=50)  # Field name made lowercase.
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.
    gxr = models.CharField(db_column='GXR', max_length=50)  # Field name made lowercase.
    gxrq = models.DateTimeField(db_column='GXRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ddsczt'


class DjangoMc3(models.Model):
    ��Ʒ���� = models.CharField(max_length=50)
    ��Ʒ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    ��ɫ���� = models.CharField(max_length=50)
    �ߴ���� = models.CharField(max_length=50)
    �ߴ����� = models.CharField(max_length=50)
    ������� = models.IntegerField()
    ���ֿ��ÿ�� = models.IntegerField()
    �������� = models.IntegerField()
    ����ȱ�� = models.IntegerField()
    jit�ֿ��ÿ�� = models.IntegerField(db_column='JIT�ֿ��ÿ��')  # Field name made lowercase.
    jit������ = models.IntegerField(db_column='JIT������')  # Field name made lowercase.
    jit��ȱ�� = models.IntegerField(db_column='JIT��ȱ��')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'django_MC3�������'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoWeb(models.Model):
    ���� = models.CharField(max_length=50, blank=True, null=True)
    λ�� = models.CharField(max_length=50, blank=True, null=True)
    �˺�1 = models.CharField(max_length=100, blank=True, null=True)
    ����1 = models.CharField(max_length=100, blank=True, null=True)
    �˺�2 = models.CharField(max_length=100, blank=True, null=True)
    ����2 = models.CharField(max_length=100, blank=True, null=True)
    ��ϸ1 = models.CharField(max_length=100, blank=True, null=True)
    ��ϸ2 = models.CharField(max_length=100, blank=True, null=True)
    ��ϸ3 = models.CharField(max_length=100, blank=True, null=True)
    ��ϸ4 = models.CharField(max_length=100, blank=True, null=True)
    ��ϸ5 = models.CharField(max_length=100, blank=True, null=True)
    ��ϸ6 = models.CharField(max_length=100, blank=True, null=True)
    ��ϸ7 = models.CharField(max_length=100, blank=True, null=True)
    ��ϸ8 = models.CharField(max_length=100, blank=True, null=True)
    ��Ƭ���� = models.CharField(max_length=50, blank=True, null=True)
    ��Ƭ��ʶ = models.CharField(max_length=50, blank=True, null=True)
    ���� = models.CharField(max_length=50, blank=True, null=True)
    �Ƿ����� = models.IntegerField(blank=True, null=True)
    ��ע = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'django_web_��˾�����ַ'


class DjangoWmXsdd(models.Model):
    ordersn = models.CharField(max_length=100, blank=True, null=True)
    deal_code = models.CharField(max_length=100, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    fhck = models.CharField(max_length=50, blank=True, null=True)
    shipping_time_fh = models.DateTimeField(blank=True, null=True)
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'django_wm_XSDD'


class DjangoWmXsddmx(models.Model):
    ordersn = models.CharField(max_length=100, blank=True, null=True)
    deal_code = models.CharField(max_length=100, blank=True, null=True)
    goods_sn = models.CharField(max_length=100, blank=True, null=True)
    brocode = models.CharField(max_length=100, blank=True, null=True)
    goods_number = models.IntegerField(blank=True, null=True)
    zdrq = models.DateTimeField(db_column='ZDRQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'django_wm_XSDDMX'


class Django(models.Model):
    ��Ʒ���� = models.CharField(max_length=50, blank=True, null=True)
    ��Ʒ���� = models.CharField(max_length=50, blank=True, null=True)
    ��ɫ���� = models.CharField(max_length=50, blank=True, null=True)
    ��ɫ���� = models.CharField(max_length=50, blank=True, null=True)
    �ߴ���� = models.CharField(max_length=50, blank=True, null=True)
    �ߴ����� = models.CharField(max_length=50, blank=True, null=True)
    �ֿ���� = models.CharField(max_length=50, blank=True, null=True)
    �ֿ����� = models.CharField(max_length=50, blank=True, null=True)
    �ֿ����� = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_ˢ����Ʒ�������'


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class Efast365Oms(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sell_record_code = models.CharField(max_length=250, blank=True, null=True)
    order_status = models.CharField(max_length=250, blank=True, null=True)
    shipping_status = models.CharField(max_length=250, blank=True, null=True)
    pay_status = models.CharField(max_length=250, blank=True, null=True)
    deal_code_list = models.CharField(max_length=250, blank=True, null=True)
    sale_channel_code = models.CharField(max_length=250, blank=True, null=True)
    store_code = models.CharField(max_length=250, blank=True, null=True)
    shop_code = models.CharField(max_length=250, blank=True, null=True)
    customer_code = models.CharField(max_length=250, blank=True, null=True)
    buyer_name = models.CharField(max_length=250, blank=True, null=True)
    receiver_name = models.CharField(max_length=250, blank=True, null=True)
    receiver_country = models.CharField(max_length=250, blank=True, null=True)
    receiver_province = models.CharField(max_length=250, blank=True, null=True)
    receiver_city = models.CharField(max_length=250, blank=True, null=True)
    receiver_district = models.CharField(max_length=250, blank=True, null=True)
    receiver_street = models.CharField(max_length=250, blank=True, null=True)
    receiver_address = models.CharField(max_length=250, blank=True, null=True)
    receiver_addr = models.CharField(max_length=250, blank=True, null=True)
    receiver_zip_code = models.CharField(max_length=250, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=250, blank=True, null=True)
    receiver_phone = models.CharField(max_length=250, blank=True, null=True)
    receiver_email = models.CharField(max_length=250, blank=True, null=True)
    express_code = models.CharField(max_length=250, blank=True, null=True)
    express_no = models.CharField(max_length=250, blank=True, null=True)
    buyer_remark = models.TextField(blank=True, null=True)  # This field type is a guess.
    seller_remark = models.TextField(blank=True, null=True)  # This field type is a guess.
    order_remark = models.TextField(blank=True, null=True)  # This field type is a guess.
    store_remark = models.TextField(blank=True, null=True)  # This field type is a guess.
    change_record = models.CharField(max_length=250, blank=True, null=True)
    invoice_title = models.CharField(max_length=250, blank=True, null=True)
    invoice_content = models.CharField(max_length=250, blank=True, null=True)
    goods_num = models.CharField(max_length=250, blank=True, null=True)
    express_money = models.CharField(max_length=250, blank=True, null=True)
    payable_money = models.CharField(max_length=250, blank=True, null=True)
    paid_money = models.CharField(max_length=250, blank=True, null=True)
    fx_payable_money = models.CharField(max_length=250, blank=True, null=True)
    fx_express_money = models.CharField(max_length=250, blank=True, null=True)
    record_time = models.CharField(max_length=250, blank=True, null=True)
    pay_time = models.CharField(max_length=250, blank=True, null=True)
    delivery_time = models.CharField(max_length=250, blank=True, null=True)
    sign_time = models.CharField(max_length=250, blank=True, null=True)
    is_notice_time = models.CharField(max_length=250, blank=True, null=True)
    pay_type = models.CharField(max_length=250, blank=True, null=True)
    pay_code = models.CharField(max_length=250, blank=True, null=True)
    lastchanged = models.CharField(max_length=250, blank=True, null=True)
    real_weigh = models.CharField(max_length=250, blank=True, null=True)
    weigh_express_money = models.CharField(max_length=250, blank=True, null=True)
    receiver_province_code = models.CharField(max_length=250, blank=True, null=True)
    receiver_city_code = models.CharField(max_length=250, blank=True, null=True)
    receiver_district_code = models.CharField(max_length=250, blank=True, null=True)
    receiver_street_code = models.CharField(max_length=250, blank=True, null=True)
    discount_fee = models.IntegerField(blank=True, null=True)
    shop_name = models.CharField(max_length=250, blank=True, null=True)
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'efast365oms'


class Erp(models.Model):
    �������� = models.CharField(max_length=50)
    ���ݿ����� = models.CharField(max_length=50)
    �Ƿ�ͣ�� = models.BooleanField()
    �������� = models.DateTimeField()
    �Ƿ���� = models.BooleanField()
    ��� = models.CharField(max_length=20)
    ���� = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'erp_����'


class Hdid(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    wz = models.CharField(db_column='WZ', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdID'
