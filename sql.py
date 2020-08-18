# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aa(models.Model):
    状态 = models.CharField(max_length=50)
    品牌 = models.CharField(max_length=50)
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    款号 = models.CharField(max_length=50)
    毛利 = models.CharField(max_length=50)
    加工费 = models.CharField(max_length=50)
    成本价 = models.CharField(max_length=50)
    含税价 = models.CharField(max_length=50)
    员工价 = models.CharField(max_length=50)
    推广成本价 = models.CharField(max_length=50)
    吊牌价 = models.CharField(max_length=50)
    网店标价 = models.CharField(max_length=50)
    旧网店卖价 = models.CharField(max_length=50)
    网店卖价 = models.CharField(max_length=50)
    leff网店标价 = models.IntegerField(db_column='LEFF网店标价')  # Field name made lowercase.
    leff网店卖价 = models.IntegerField(db_column='LEFF网店卖价')  # Field name made lowercase.
    日常活动价 = models.CharField(max_length=50)
    年终活动价 = models.CharField(max_length=50)
    厂家 = models.CharField(max_length=50)
    产品分类 = models.CharField(max_length=50)
    规格 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AA产品价格导入'


class A(models.Model):
    spdm = models.CharField(max_length=50, blank=True, null=True)
    pp = models.CharField(max_length=50, blank=True, null=True)
    spmc = models.CharField(max_length=50, blank=True, null=True)
    ml = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'A导入数据'


class Bsxlmx(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    品牌名称 = models.CharField(max_length=50, blank=True, null=True)
    年份 = models.CharField(max_length=50, blank=True, null=True)
    季节 = models.CharField(max_length=50, blank=True, null=True)
    季节名称 = models.CharField(max_length=50, blank=True, null=True)
    分类 = models.CharField(max_length=50, blank=True, null=True)
    分类名称 = models.CharField(max_length=50, blank=True, null=True)
    二级分类 = models.CharField(max_length=50, blank=True, null=True)
    款号 = models.CharField(max_length=50, blank=True, null=True)
    设计师 = models.CharField(max_length=50, blank=True, null=True)
    商品代码 = models.CharField(max_length=50, blank=True, null=True)
    商品名称 = models.CharField(max_length=50, blank=True, null=True)
    颜色代码 = models.CharField(max_length=50, blank=True, null=True)
    颜色名称 = models.CharField(max_length=50, blank=True, null=True)
    尺寸代码 = models.CharField(max_length=50, blank=True, null=True)
    尺寸名称 = models.CharField(max_length=50, blank=True, null=True)
    产品状态 = models.CharField(max_length=50, blank=True, null=True)
    数量 = models.IntegerField(blank=True, null=True)
    单价 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    金额 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    成本单价 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    成本金额 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    单据类型 = models.CharField(max_length=50, blank=True, null=True)
    单据编号 = models.CharField(max_length=50, blank=True, null=True)
    原单据号 = models.CharField(max_length=50, blank=True, null=True)
    销售日期 = models.DateTimeField(blank=True, null=True)
    客户代码 = models.CharField(max_length=50, blank=True, null=True)
    客户名称 = models.CharField(max_length=50, blank=True, null=True)
    仓库代码 = models.CharField(max_length=50, blank=True, null=True)
    仓库名称 = models.CharField(max_length=50, blank=True, null=True)
    年月日 = models.CharField(max_length=50, blank=True, null=True)
    年月 = models.CharField(max_length=50, blank=True, null=True)
    年 = models.CharField(max_length=50, blank=True, null=True)
    风格代码 = models.CharField(max_length=50, blank=True, null=True)
    风格名称 = models.CharField(max_length=50, blank=True, null=True)
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BSXLMX'


class Bs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    年 = models.CharField(max_length=50)
    年月 = models.CharField(max_length=50)
    年月日 = models.CharField(max_length=50)
    客户分类 = models.CharField(max_length=50)
    客户分类排序 = models.IntegerField()
    客户名称 = models.CharField(max_length=50)
    销售数量 = models.IntegerField()
    销售金额 = models.IntegerField()
    销售数量爆款 = models.IntegerField()
    销售金额爆款 = models.IntegerField()
    销售数量旺款 = models.IntegerField()
    销售金额旺款 = models.IntegerField()
    销售数量平销 = models.IntegerField()
    销售金额平销 = models.IntegerField()
    销售数量滞销 = models.IntegerField()
    销售金额滞销 = models.IntegerField()
    销售数量零销 = models.IntegerField()
    销售金额零销 = models.IntegerField()
    销售数量新品 = models.IntegerField()
    销售金额新品 = models.IntegerField()
    销售数量赠品 = models.IntegerField()
    销售金额赠品 = models.IntegerField()
    退货数量 = models.IntegerField()
    退货金额 = models.IntegerField()
    退货数量爆款 = models.IntegerField()
    退货金额爆款 = models.IntegerField()
    退货数量旺款 = models.IntegerField()
    退货金额旺款 = models.IntegerField()
    退货数量平销 = models.IntegerField()
    退货金额平销 = models.IntegerField()
    退货数量滞销 = models.IntegerField()
    退货金额滞销 = models.IntegerField()
    退货数量零销 = models.IntegerField()
    退货金额零销 = models.IntegerField()
    退货数量新品 = models.IntegerField()
    退货金额新品 = models.IntegerField()
    退货数量赠品 = models.IntegerField()
    退货金额赠品 = models.IntegerField()
    备注 = models.CharField(max_length=250)
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销售简报'


class Bs30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量30天'


class Bs30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量京东自营30天'


class Bs30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量唯品会30天'


class Bs17(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量唯品会第1个7天'


class Bs27(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量唯品会第2个7天'


class Bs37(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量唯品会第3个7天'


class Bs30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量非唯品会30天'


class Bs17(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量非唯品会第1个7天'


class Bs27(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量非唯品会第2个7天'


class Bs37(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    ts = models.DateTimeField(db_column='TS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS销量非唯品会第3个7天'


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
        db_table = 'EFAST上传单据'


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
    名称 = models.CharField(max_length=50, blank=True, null=True)
    数量 = models.IntegerField(blank=True, null=True)
    区域 = models.CharField(max_length=50, blank=True, null=True)
    备注 = models.CharField(max_length=100, blank=True, null=True)
    使用日期 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IT_资产耗材明细'


class It(models.Model):
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


class It(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    资产编号 = models.CharField(max_length=50)
    资产名称 = models.CharField(max_length=50)
    资产类型 = models.CharField(max_length=50)
    资产规格 = models.CharField(max_length=50)
    资产型号 = models.CharField(max_length=50)
    购买日期 = models.DateTimeField(blank=True, null=True)
    供应商名称 = models.CharField(max_length=50)
    出厂编号 = models.CharField(max_length=50)
    生产日期 = models.DateTimeField(blank=True, null=True)
    保修截止日期 = models.DateTimeField(blank=True, null=True)
    使用日期 = models.DateTimeField(blank=True, null=True)
    预计使用年限 = models.IntegerField(blank=True, null=True)
    预计报废日期 = models.DateTimeField(blank=True, null=True)
    原始价格 = models.DecimalField(max_digits=18, decimal_places=2)
    使用状态 = models.CharField(max_length=50)
    所在位置 = models.CharField(max_length=50)
    责任人 = models.CharField(max_length=50)
    责任人部门 = models.CharField(max_length=50)
    主板编号 = models.CharField(max_length=50)
    主板型号 = models.CharField(max_length=50)
    主板序号_sn = models.CharField(db_column='主板序号_SN', max_length=50)  # Field name made lowercase.
    cpu1编号 = models.CharField(db_column='CPU1编号', max_length=50)  # Field name made lowercase.
    cpu1型号 = models.CharField(db_column='CPU1型号', max_length=50)  # Field name made lowercase.
    cpu1序号_sn = models.CharField(db_column='CPU1序号_SN', max_length=50)  # Field name made lowercase.
    cpu1风扇编号 = models.CharField(db_column='CPU1风扇编号', max_length=50)  # Field name made lowercase.
    cpu1风扇 = models.CharField(db_column='CPU1风扇', max_length=50)  # Field name made lowercase.
    cpu1风扇序号_sn = models.CharField(db_column='CPU1风扇序号_SN', max_length=50)  # Field name made lowercase.
    cpu2编号 = models.CharField(db_column='CPU2编号', max_length=50)  # Field name made lowercase.
    cpu2型号 = models.CharField(db_column='CPU2型号', max_length=50)  # Field name made lowercase.
    cpu2序号_sn = models.CharField(db_column='CPU2序号_SN', max_length=50)  # Field name made lowercase.
    cpu2风扇编号 = models.CharField(db_column='CPU2风扇编号', max_length=50)  # Field name made lowercase.
    cpu2风扇 = models.CharField(db_column='CPU2风扇', max_length=50)  # Field name made lowercase.
    cpu2风扇序号_sn = models.CharField(db_column='CPU2风扇序号_SN', max_length=50)  # Field name made lowercase.
    cpu3编号 = models.CharField(db_column='CPU3编号', max_length=50)  # Field name made lowercase.
    cpu3型号 = models.CharField(db_column='CPU3型号', max_length=50)  # Field name made lowercase.
    cpu3序号_sn = models.CharField(db_column='CPU3序号_SN', max_length=50)  # Field name made lowercase.
    cpu3风扇编号 = models.CharField(db_column='CPU3风扇编号', max_length=50)  # Field name made lowercase.
    cpu3风扇 = models.CharField(db_column='CPU3风扇', max_length=50)  # Field name made lowercase.
    cpu3风扇序号_sn = models.CharField(db_column='CPU3风扇序号_SN', max_length=50)  # Field name made lowercase.
    cpu4编号 = models.CharField(db_column='CPU4编号', max_length=50)  # Field name made lowercase.
    cpu4型号 = models.CharField(db_column='CPU4型号', max_length=50)  # Field name made lowercase.
    cpu4序号_sn = models.CharField(db_column='CPU4序号_SN', max_length=50)  # Field name made lowercase.
    cpu4风扇编号 = models.CharField(db_column='CPU4风扇编号', max_length=50)  # Field name made lowercase.
    cpu4风扇 = models.CharField(db_column='CPU4风扇', max_length=50)  # Field name made lowercase.
    cpu4风扇序号_sn = models.CharField(db_column='CPU4风扇序号_SN', max_length=50)  # Field name made lowercase.
    机箱风扇1编号 = models.CharField(max_length=50)
    机箱风扇1 = models.CharField(max_length=50)
    机箱风扇1序号_sn = models.CharField(db_column='机箱风扇1序号_SN', max_length=50)  # Field name made lowercase.
    机箱风扇2编号 = models.CharField(max_length=50)
    机箱风扇2 = models.CharField(max_length=50)
    机箱风扇2序号_sn = models.CharField(db_column='机箱风扇2序号_SN', max_length=50)  # Field name made lowercase.
    网卡1编号 = models.CharField(max_length=50)
    网卡1型号 = models.CharField(max_length=50)
    网卡1序号_sn = models.CharField(db_column='网卡1序号_SN', max_length=50)  # Field name made lowercase.
    网卡2编号 = models.CharField(max_length=50)
    网卡2型号 = models.CharField(max_length=50)
    网卡2序号_sn = models.CharField(db_column='网卡2序号_SN', max_length=50)  # Field name made lowercase.
    网卡3编号 = models.CharField(max_length=50)
    网卡3型号 = models.CharField(max_length=50)
    网卡3序号_sn = models.CharField(db_column='网卡3序号_SN', max_length=50)  # Field name made lowercase.
    网卡4编号 = models.CharField(max_length=50)
    网卡4型号 = models.CharField(max_length=50)
    网卡4序号_sn = models.CharField(db_column='网卡4序号_SN', max_length=50)  # Field name made lowercase.
    声卡编号 = models.CharField(max_length=50)
    声卡型号 = models.CharField(max_length=50)
    声卡序号_sn = models.CharField(db_column='声卡序号_SN', max_length=50)  # Field name made lowercase.
    显卡编号 = models.CharField(max_length=50)
    显卡型号 = models.CharField(max_length=50)
    显卡序号sn = models.CharField(db_column='显卡序号SN', max_length=50)  # Field name made lowercase.
    显卡接口 = models.CharField(max_length=50)
    显卡容量 = models.CharField(max_length=50)
    电源编号 = models.CharField(max_length=50)
    电源型号 = models.CharField(max_length=50)
    电源序号_sn = models.CharField(db_column='电源序号_SN', max_length=50)  # Field name made lowercase.
    电源类型 = models.CharField(max_length=50)
    额定功率 = models.CharField(max_length=50)
    硬盘1编号 = models.CharField(max_length=50)
    硬盘1 = models.CharField(max_length=50)
    硬盘1序号_sn = models.CharField(db_column='硬盘1序号_SN', max_length=50)  # Field name made lowercase.
    硬盘1接口 = models.CharField(max_length=50)
    硬盘1容量 = models.CharField(max_length=50)
    硬盘2编号 = models.CharField(max_length=50)
    硬盘2 = models.CharField(max_length=50)
    硬盘2序号sn = models.CharField(db_column='硬盘2序号SN', max_length=50)  # Field name made lowercase.
    硬盘2接口 = models.CharField(max_length=50)
    硬盘2容量 = models.CharField(max_length=50)
    硬盘3编号 = models.CharField(max_length=50)
    硬盘3 = models.CharField(max_length=50)
    硬盘3序号_sn = models.CharField(db_column='硬盘3序号_SN', max_length=50)  # Field name made lowercase.
    硬盘3接口 = models.CharField(max_length=50)
    硬盘3容量 = models.CharField(max_length=50)
    硬盘4编号 = models.CharField(max_length=50)
    硬盘4 = models.CharField(max_length=50)
    硬盘4序号_sn = models.CharField(db_column='硬盘4序号_SN', max_length=50)  # Field name made lowercase.
    硬盘4接口 = models.CharField(max_length=50)
    硬盘4容量 = models.CharField(max_length=50)
    内存1编号 = models.CharField(max_length=50)
    内存1 = models.CharField(max_length=50)
    内存1序号_sn = models.CharField(db_column='内存1序号_SN', max_length=50)  # Field name made lowercase.
    内存1接口 = models.CharField(max_length=50)
    内存1容量 = models.CharField(max_length=50)
    内存2编号 = models.CharField(max_length=50)
    内存2 = models.CharField(max_length=50)
    内存2序号_sn = models.CharField(db_column='内存2序号_SN', max_length=50)  # Field name made lowercase.
    内存2接口 = models.CharField(max_length=50)
    内存2容量 = models.CharField(max_length=50)
    内存3编号 = models.CharField(max_length=50)
    内存3 = models.CharField(max_length=50)
    内存3序号_sn = models.CharField(db_column='内存3序号_SN', max_length=50)  # Field name made lowercase.
    内存3接口 = models.CharField(max_length=50)
    内存3容量 = models.CharField(max_length=50)
    内存4编号 = models.CharField(max_length=50)
    内存4 = models.CharField(max_length=50)
    内存4序号_sn = models.CharField(db_column='内存4序号_SN', max_length=50)  # Field name made lowercase.
    内存4接口 = models.CharField(max_length=50)
    内存4容量 = models.CharField(max_length=50)
    光驱1编号 = models.CharField(max_length=50)
    光驱1 = models.CharField(max_length=50)
    光驱1序号_sn = models.CharField(db_column='光驱1序号_SN', max_length=50)  # Field name made lowercase.
    光驱1接口 = models.CharField(max_length=50)
    光驱1类型 = models.CharField(max_length=50)
    光驱2编号 = models.CharField(max_length=50)
    光驱2 = models.CharField(max_length=50)
    光驱2序号_sn = models.CharField(db_column='光驱2序号_SN', max_length=50)  # Field name made lowercase.
    光驱2接口 = models.CharField(max_length=50)
    光驱2类型 = models.CharField(max_length=50)
    机箱编号 = models.CharField(max_length=50)
    机箱 = models.CharField(max_length=50)
    机箱序号_sn = models.CharField(db_column='机箱序号_SN', max_length=50)  # Field name made lowercase.
    显示器编号 = models.CharField(max_length=50)
    显示器型号 = models.CharField(max_length=50)
    显示器序号_sn = models.CharField(db_column='显示器序号_SN', max_length=50)  # Field name made lowercase.
    显示器类型 = models.CharField(max_length=50)
    显示器尺寸 = models.CharField(max_length=50)
    键盘编号 = models.CharField(max_length=50)
    键盘型号 = models.CharField(max_length=50)
    键盘序号_sn = models.CharField(db_column='键盘序号_SN', max_length=50)  # Field name made lowercase.
    键盘接口 = models.CharField(max_length=50)
    键盘类型 = models.CharField(max_length=50)
    鼠标编号 = models.CharField(max_length=50)
    鼠标型号 = models.CharField(max_length=50)
    鼠标序号_sn = models.CharField(db_column='鼠标序号_SN', max_length=50)  # Field name made lowercase.
    鼠标接口 = models.CharField(max_length=50)
    鼠标类型 = models.CharField(max_length=50)
    账号 = models.CharField(max_length=50)
    安全级别 = models.CharField(max_length=50)
    ip地址1 = models.CharField(db_column='IP地址1', max_length=50)  # Field name made lowercase.
    ip地址2 = models.CharField(db_column='IP地址2', max_length=50)  # Field name made lowercase.
    ip地址3 = models.CharField(db_column='IP地址3', max_length=50)  # Field name made lowercase.
    ip地址4 = models.CharField(db_column='IP地址4', max_length=50)  # Field name made lowercase.
    mac地址1 = models.CharField(db_column='MAC地址1', max_length=50)  # Field name made lowercase.
    mac地址2 = models.CharField(db_column='MAC地址2', max_length=50)  # Field name made lowercase.
    mac地址3 = models.CharField(db_column='MAC地址3', max_length=50)  # Field name made lowercase.
    mac地址4 = models.CharField(db_column='MAC地址4', max_length=50)  # Field name made lowercase.
    电话号码 = models.CharField(max_length=50)
    话费额度 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    自定义1 = models.CharField(max_length=100)
    自定义2 = models.CharField(max_length=100)
    自定义3 = models.CharField(max_length=100)
    自定义4 = models.CharField(max_length=100)
    自定义5 = models.CharField(max_length=100)
    自定义6 = models.CharField(max_length=100)
    自定义7 = models.CharField(max_length=100)
    自定义8 = models.CharField(max_length=100)
    自定义9 = models.CharField(max_length=100)
    自定义10 = models.CharField(max_length=100)
    自定义11 = models.CharField(max_length=100)
    自定义12 = models.CharField(max_length=100)
    自定义13 = models.CharField(max_length=100)
    自定义14 = models.CharField(max_length=100)
    自定义15 = models.CharField(max_length=100)
    自定义16 = models.CharField(max_length=100)
    自定义17 = models.CharField(max_length=100)
    自定义18 = models.CharField(max_length=100)
    自定义19 = models.CharField(max_length=100)
    自定义20 = models.CharField(max_length=100)
    自定义21 = models.CharField(max_length=100)
    自定义22 = models.CharField(max_length=100)
    自定义23 = models.CharField(max_length=100)
    自定义24 = models.CharField(max_length=100)
    自定义25 = models.CharField(max_length=100)
    自定义26 = models.CharField(max_length=100)
    自定义27 = models.CharField(max_length=100)
    自定义28 = models.CharField(max_length=100)
    自定义29 = models.CharField(max_length=100)
    自定义30 = models.CharField(max_length=100)
    备注 = models.CharField(max_length=100)
    制单人 = models.CharField(max_length=20)
    制单日期 = models.DateTimeField(blank=True, null=True)
    更新人 = models.CharField(max_length=20)
    更新日期 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IT资产管理'


class It(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    类型 = models.CharField(max_length=50)
    值 = models.CharField(max_length=50)
    备注 = models.CharField(max_length=100)
    制单人 = models.CharField(max_length=20)
    制单日期 = models.DateTimeField(blank=True, null=True)
    更新人 = models.CharField(max_length=20)
    更新日期 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IT资产管理基础资料设置'


class Leffspkcb(models.Model):
    关联仓库 = models.CharField(max_length=50)
    商品代码 = models.CharField(max_length=50)
    区域 = models.CharField(max_length=50)
    库位 = models.CharField(max_length=50)
    数量 = models.IntegerField()
    箱数 = models.IntegerField()
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
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    唯品会代码 = models.CharField(max_length=50, blank=True, null=True)
    唯品会商品名称 = models.CharField(max_length=50, blank=True, null=True)
    助记符 = models.CharField(max_length=50, blank=True, null=True)
    研发类型 = models.CharField(max_length=50, blank=True, null=True)
    品牌 = models.CharField(max_length=50, blank=True, null=True)
    产品状态 = models.CharField(max_length=50, blank=True, null=True)
    销量类型 = models.CharField(max_length=50, blank=True, null=True)
    现工厂 = models.CharField(max_length=50, blank=True, null=True)
    原工厂 = models.CharField(max_length=300, blank=True, null=True)
    迭代款 = models.CharField(max_length=50, blank=True, null=True)
    同尺寸带刺绣款 = models.CharField(max_length=50)
    同尺寸带丝印款 = models.CharField(max_length=50)
    主料相同款 = models.CharField(max_length=50)
    备注 = models.CharField(max_length=250)
    制单人 = models.CharField(max_length=50)
    制单日期 = models.DateTimeField(blank=True, null=True)
    更新人 = models.CharField(max_length=50)
    更新日期 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PR_XHJLB'


class PrXhjlbRz(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    操作字段名称 = models.CharField(max_length=50)
    操作说明 = models.CharField(max_length=250)
    商品代码 = models.CharField(max_length=50)
    备注 = models.CharField(max_length=250)
    制单人 = models.CharField(max_length=50)
    制单日期 = models.DateTimeField(blank=True, null=True)

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
    品牌 = models.CharField(max_length=50)
    属性 = models.CharField(max_length=50)
    销量 = models.IntegerField()
    销量占比 = models.CharField(max_length=50)
    金额 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sku = models.IntegerField(db_column='SKU')  # Field name made lowercase.
    sku占比 = models.CharField(db_column='SKU占比', max_length=50)  # Field name made lowercase.
    spu = models.IntegerField(db_column='SPU')  # Field name made lowercase.
    类别 = models.CharField(max_length=50)
    月份 = models.CharField(max_length=50)
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
    商品代码 = models.CharField(max_length=50)
    商品名称 = models.CharField(max_length=50)
    颜色代码 = models.CharField(max_length=50)
    颜色名称 = models.CharField(max_length=50)
    尺寸代码 = models.CharField(max_length=50)
    尺寸名称 = models.CharField(max_length=50)
    锁定库存 = models.IntegerField()
    主仓可用库存 = models.IntegerField()
    主仓锁定 = models.IntegerField()
    主仓缺货 = models.IntegerField()
    jit仓可用库存 = models.IntegerField(db_column='JIT仓可用库存')  # Field name made lowercase.
    jit仓锁定 = models.IntegerField(db_column='JIT仓锁定')  # Field name made lowercase.
    jit仓缺货 = models.IntegerField(db_column='JIT仓缺货')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'django_MC3锁定库存'


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
    名称 = models.CharField(max_length=50, blank=True, null=True)
    位置 = models.CharField(max_length=50, blank=True, null=True)
    账号1 = models.CharField(max_length=100, blank=True, null=True)
    密码1 = models.CharField(max_length=100, blank=True, null=True)
    账号2 = models.CharField(max_length=100, blank=True, null=True)
    密码2 = models.CharField(max_length=100, blank=True, null=True)
    明细1 = models.CharField(max_length=100, blank=True, null=True)
    明细2 = models.CharField(max_length=100, blank=True, null=True)
    明细3 = models.CharField(max_length=100, blank=True, null=True)
    明细4 = models.CharField(max_length=100, blank=True, null=True)
    明细5 = models.CharField(max_length=100, blank=True, null=True)
    明细6 = models.CharField(max_length=100, blank=True, null=True)
    明细7 = models.CharField(max_length=100, blank=True, null=True)
    明细8 = models.CharField(max_length=100, blank=True, null=True)
    卡片类型 = models.CharField(max_length=50, blank=True, null=True)
    卡片标识 = models.CharField(max_length=50, blank=True, null=True)
    费用 = models.CharField(max_length=50, blank=True, null=True)
    是否隐藏 = models.IntegerField(blank=True, null=True)
    备注 = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'django_web_公司网络地址'


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
    商品代码 = models.CharField(max_length=50, blank=True, null=True)
    商品名称 = models.CharField(max_length=50, blank=True, null=True)
    颜色代码 = models.CharField(max_length=50, blank=True, null=True)
    颜色名称 = models.CharField(max_length=50, blank=True, null=True)
    尺寸代码 = models.CharField(max_length=50, blank=True, null=True)
    尺寸名称 = models.CharField(max_length=50, blank=True, null=True)
    仓库代码 = models.CharField(max_length=50, blank=True, null=True)
    仓库名称 = models.CharField(max_length=50, blank=True, null=True)
    仓库数量 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_刷新商品需求库存表'


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
    套帐名称 = models.CharField(max_length=50)
    数据库名称 = models.CharField(max_length=50)
    是否停用 = models.BooleanField()
    创建日期 = models.DateTimeField()
    是否测试 = models.BooleanField()
    类别 = models.CharField(max_length=20)
    排序 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'erp_套帐'


class Hdid(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    wz = models.CharField(db_column='WZ', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdID'
