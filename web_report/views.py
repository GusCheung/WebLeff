from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
import hashlib  # MD5解密
from web_IT_info.models import it资产
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.contrib import messages
from django.db import connection  # 自定义查询语句
import xlwt
from io import BytesIO
import re
# 销售数据分析
@csrf_exempt
def xxsj_report(request):
    lc = ['Windows', 'iPhone', 'Linux', 'Android', 'BlackBerry', 'Macintosh', 'Ubuntu']
    userAgent = request.META['HTTP_USER_AGENT']
    for lc1 in lc:
        if re.findall(lc1, userAgent):
            lce = re.findall(lc1, userAgent)
    if lce[0] == 'Windows' or lce[0] == 'Macintosh':
        lc设备 = '电脑端'
    else:
        lc设备 = '手机端'
    lc查询 = False

    if request.method == "POST":
        lc商品代码 = request.POST.get('data[lc商品代码]')
        lc商品名称 = request.POST.get('data[lc商品名称]')
        lc开始日期 = request.POST.get('data[lc开始日期]')
        lc结束日期 = request.POST.get('data[lc结束日期]')
        lc店铺 = request.POST.get('data[lc店铺]')
        lc客户 = request.POST.get('data[lc客户]')
        cursor = connection.cursor()
        # cursor.execute("select  *  from LEFF.dbo.vBS零售批发渠道  where  销售日期 between '2020-07-20' and '2020-07-21'")
        cursor.execute("select TOP 3 * from LEFF.dbo.vBS零售批发渠道")
        XSSJ_fx = cursor.fetchall()
        print(type(XSSJ_fx))
        print(XSSJ_fx[1])
        lc查询 = True
        # cursor.execute("SELECT COLUMN_NAME as 字段名 from leff.information_schema.columns where TABLE_NAME = 'vBS零售批发渠道'")
        # XSSJ_filed = cursor.fetchall()
        # cursor.close()  # 关闭游标
        return render(request, 'Sale_data_analysis_report.html', {
                                                                'lc设备': lc设备,
                                                                'lc查询': lc查询,
                                                                'XSSJ_fx_lists': XSSJ_fx
                                                                })

    return render(request, 'Sale_data_analysis_report.html', {
                                                              'lc设备': lc设备,
                                                              'lc查询': lc查询
                                                              })


# 经营简报
def push_run(requnest):
    # select *
    # from leff.dbo.vBS批发销货单_不含大进大出类数据_近两年  WHERE
    # 销售日期 >= '2019-01-01 00:00:00'
    #
    # select *
    # from leff.dbo.vBS零售退货单_近两年
    # select *
    # from leff.dbo.vBS批发退货单_不含大进大出类数据_近两年
    #
    # SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. *
    # FROM
    # leff.dbo.vBS零售销货单
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    # WHERE
    # a.销售日期 >= '2019-01-01 00:00:00'
    #
    # SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. *
    # FROM
    # leff.dbo.vBS批发销货单_不含大进大出类数据_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    # WHERE
    # a.销售日期 >= '2019-01-01 00:00:00'
    #
    # SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. *
    # FROM
    # leff.dbo.vBS零售退货单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    #
    # SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. *
    # FROM
    # leff.dbo.vBS批发退货单_不含大进大出类数据_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    #
    # SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. *
    # FROM
    # leff.dbo.vBS批发销货单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    #
    # SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. *
    # FROM
    # leff.dbo.vBS批发退货单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    #
    # SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. *
    # FROM
    # leff.dbo.vBS渠道调拔单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    # SPACE(5)
    #
    # SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. *
    # FROM
    # leff.dbo.vBS渠道退货单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    #
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 数量 as F肇庆唯品会数量, 金额 as F肇庆唯品会金额
    # , 0000000000 as F成都仓唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 0000000000 as F北京唯品会数量, 0000000000 as F北京唯品会金额
    # , 0000000000 as F上海唯品会仓数量, 0000000000 as F上海唯品会仓金额
    # , 0000000000 as F武汉唯品会数量, 0000000000 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # from
    # (SELECT  ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS零售销货单
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    # WHERE
    # a.销售日期 >= '2019-01-01 00:00:00') a
    # where
    # 客户代码 = 'WPH01'
    # UNION
    # ALL
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 数量 as F肇庆唯品会数量, 金额 as F肇庆唯品会金额
    # , 0000000000 as F成都仓唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 0000000000 as F北京唯品会数量, 0000000000 as F北京唯品会金额
    # , 0000000000 as F上海唯品会仓数量, 0000000000 as F上海唯品会仓金额
    # , 0000000000 as F武汉唯品会数量, 0000000000 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # FROM(SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS批发销货单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码) b
    # where
    # 客户代码 = 'WPH01'
    # UNION
    # ALL
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 0000000000 as F肇庆唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 数量 as F成都仓唯品会数量, 金额 as F成都仓唯品会金额
    # , 0000000000 as F北京唯品会数量, 0000000000 as F北京唯品会金额
    # , 0000000000 as F上海唯品会仓数量, 0000000000 as F上海唯品会仓金额
    # , 0000000000 as F武汉唯品会数量, 0000000000 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # from
    # (SELECT  ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS零售销货单
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    # WHERE
    # a.销售日期 >= '2019-01-01 00:00:00') a
    # where
    # 客户代码 = 'WPH03'
    # UNION
    # ALL
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 0000000000 as F肇庆唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 数量 as F成都仓唯品会数量, 金额 as F成都仓唯品会金额
    # , 0000000000 as F北京唯品会数量, 0000000000 as F北京唯品会金额
    # , 0000000000 as F上海唯品会仓数量, 0000000000 as F上海唯品会仓金额
    # , 0000000000 as F武汉唯品会数量, 0000000000 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # FROM(SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS批发销货单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码) b
    # where
    # 客户代码 = 'WPH03'
    # UNION
    # ALL
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 0000000000 as F肇庆唯品会数量, 0000000000 as F肇庆唯品会金额
    # , 0000000000 as F成都仓唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 数量 as F北京唯品会数量, 金额 as F北京唯品会金额
    # , 0000000000 as F上海唯品会仓数量, 0000000000 as F上海唯品会仓金额
    # , 0000000000 as F武汉唯品会数量, 0000000000 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # from
    # (SELECT  ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS零售销货单
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    # WHERE
    # a.销售日期 >= '2019-01-01 00:00:00') a
    # where
    # 客户代码 = 'WPH04'
    # UNION
    # ALL
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 0000000000 as F肇庆唯品会数量, 0000000000 as F肇庆唯品会金额
    # , 0000000000 as F成都仓唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 数量 as F北京唯品会数量, 金额 as F北京唯品会金额
    # , 0000000000 as F上海唯品会仓数量, 0000000000 as F上海唯品会仓金额
    # , 0000000000 as F武汉唯品会数量, 0000000000 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # FROM(SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS批发销货单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码) b
    # where
    # 客户代码 = 'WPH04'
    # UNION
    # ALL
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 0000000000 as F肇庆唯品会数量, 0000000000 as F肇庆唯品会金额
    # , 0000000000 as F成都仓唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 0000000000 as F北京唯品会数量, 0000000000 as F北京唯品会金额
    # , 数量 as F上海唯品会仓数量, 金额 as F上海唯品会仓金额
    # , 0000000000 as F武汉唯品会数量, 0000000000 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # from
    # (SELECT  ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS零售销货单
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    # WHERE
    # a.销售日期 >= '2019-01-01 00:00:00') a
    # where
    # 客户代码 = 'WPH05'
    # UNION
    # ALL
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 0000000000 as F肇庆唯品会数量, 0000000000 as F肇庆唯品会金额
    # , 0000000000 as F成都仓唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 0000000000 as F北京唯品会数量, 0000000000 as F北京唯品会金额
    # , 数量 as F上海唯品会仓数量, 金额 as F上海唯品会仓金额
    # , 0000000000 as F武汉唯品会数量, 0000000000 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # FROM(SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS批发销货单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码) b
    # where
    # 客户代码 = 'WPH05'
    # UNION
    # ALL
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 0000000000 as F肇庆唯品会数量, 0000000000 as F肇庆唯品会金额
    # , 0000000000 as F成都仓唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 0000000000 as F北京唯品会数量, 0000000000 as F北京唯品会金额
    # , 0000000000 as F上海唯品会仓数量, 0000000000 as F上海唯品会仓金额
    # , 数量 as F武汉唯品会数量, 金额 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # from
    # (SELECT  ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS零售销货单
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码
    # WHERE
    # a.销售日期 >= '2019-01-01 00:00:00') a
    # where
    # 客户代码 = 'WPH06'
    # UNION
    # ALL
    # SELECT
    # 品牌名称, 分类, 分类名称, 款号, 设计师, 商品代码, 商品名称, 颜色代码, 颜色名称, 尺寸代码, 尺寸名称, 产品状态, 销量类型
    # , 单据编号, 原单据号, 客户代码, 客户名称, 仓库代码, 仓库名称, 年月日, 年月, 年
    # , 0000000000 as F肇庆唯品会数量, 0000000000 as F肇庆唯品会金额
    # , 0000000000 as F成都仓唯品会数量, 0000000000 as F成都仓唯品会金额
    # , 0000000000 as F北京唯品会数量, 0000000000 as F北京唯品会金额
    # , 0000000000 as F上海唯品会仓数量, 0000000000 as F上海唯品会仓金额
    # , 数量 as F武汉唯品会数量, 金额 as F武汉唯品会金额
    # , 0000000000 as F天猫旗舰店数量, 0000000000 as F天猫旗舰店金额
    # , 0000000000 as F天猫酷舟店数量, 0000000000 as F天猫酷舟店金额
    # , 0000000000 as F淘宝女包店数量, 0000000000 as F淘宝女包店金额
    # , 0000000000 as F淘宝企业店数量, 0000000000 as F淘宝企业店金额
    # , 0000000000 as F京东1店数量, 0000000000 as F京东1店金额
    # , 0000000000 as F京东2店数量, 0000000000 as F京东2店金额
    # , 0000000000 as F淘宝分销店数量, 0000000000 as F淘宝分销店金额
    # , 0000000000 as F阿里巴巴店数量, 0000000000 as F阿里巴巴店金额
    # , 0000000000 as F飞牛网店数量, 0000000000 as F飞牛网店金额
    # , 0000000000 as F小红书店数量, 0000000000 as F小红书店金额
    # , 0000000000 as F亚马逊店数量, 0000000000 as F亚马逊店金额
    # , 0000000000 as F速卖通店数量, 0000000000 as F速卖通店金额
    # , 0000000000 as S天猫旗舰店数量, 0000000000 as S天猫旗舰店金额
    # , 0000000000 as S京东店数量, 0000000000 as S京东店金额
    # , 0000000000 as S融E购店数量, 0000000000 as S融E购店金额
    # , 0000000000 as S淘宝企业店数量, 0000000000 as S淘宝企业店金额
    # , 0000000000 as S淘宝分销店数量, 0000000000 as S淘宝分销店金额
    # , 0000000000 as L天猫旗舰店数量, 0000000000 as L天猫旗舰店金额
    # , 0000000000 as 中华百货数量, 0000000000 as 中华百货金额
    # , 0000000000 as 王府井百货数量, 0000000000 as 王府井百货金额
    # , 0000000000 as 新光三楼数量, 0000000000 as 新光三楼金额
    # , 0000000000 as 新光一楼数量, 0000000000 as 新光一楼金额
    # , 0000000000 as 中港展厅仓零售数量, 0000000000 as 中港展厅仓零售金额
    # , 0000000000 as 线下批发数量, 0000000000 as 线下批发金额
    # , 0000000000 as 其它销货数量, 0000000000 as 其它销货金额
    # , 0000000000 as 包退货数量, 0000000000 as 包退货金额
    # , 0000000000 as LEFF退货数量, 0000000000 as LEFF退货金额
    # , 0000000000 as 发货至唯品会大进大出数量
    # , 0000000000 as 发货至京东自营大进大出数量
    # , 0000000000 as F当当网数量, 0000000000 as F当当网金额
    # , 0000000000 as 金沙洲大润发店数量, 0000000000 as 金沙洲大润发店金额
    # , 0000000000 as L京东旗舰店数量, 0000000000 as  L京东旗舰店金额
    # , 0000000000 as F沈阳唯品会数量, 0000000000 as F沈阳唯品会金额
    # , 0000000000 as F唯品会MP数量, 0000000000 as F唯品会MP金额
    # , 0000000000 as F唯品会JITX数量, 0000000000 as F唯品会JITX金额
    # , 0000000000 as F西安唯品会数量, 0000000000 as F西安唯品会金额
    # FROM(SELECT
    # ISNULL(b.销量类型, '零销') as 销量类型, a. * FROM
    # leff.dbo.vBS批发销货单_近两年
    # a
    # LEFT
    # JOIN
    # leff.dbo.vBS零售批发渠道_近30天按SKU汇总
    # b
    # ON
    # a.商品代码 = b.商品代码) b
    # where
    # 客户代码 = 'WPH06'


    return HttpResponse('经营简报')

# 商品部推送
def push_commodity(requnest):
    return HttpResponse('商品部推送')

# 生产部推送
def push_production(requnest):
    return HttpResponse('生产部推送')

# 导出
def export(requert):
    cursor = connection.cursor()
    # cursor.execute("select  *  from LEFF.dbo.vBS零售批发渠道  where  销售日期 between '2019-01-01' and '2020-07-25'")
    cursor.execute("select * from leff.dbo.it资产_耗材及设备")
    XSSJ_fx = cursor.fetchall()

    cursor.execute("SELECT COLUMN_NAME as 字段名 from leff.information_schema.columns where TABLE_NAME = 'it资产_耗材及设备';")
    XSSJ_filed = cursor.fetchall()
    cursor.close()  # 关闭游标
    # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=xe.xls'
    # 创建文件对象
    wb = xlwt.Workbook(encoding='utf-9')
    # 创建sheet对象,第一个表明
    sheet = wb.add_sheet('IT资产耗材')
    first_co5 = sheet.col(5)
    first_co1 = sheet.col(1)
    first_co5.width = 256 * 20
    first_co5.width = 256 * 20
    first_co1.width = 256 * 20

    # 设置文件头的样式
    style_heading = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index white,
                    bold on,
                    height 0xA0;
                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour 0x19;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """)

    INTX = 0
    for a in range(len(XSSJ_filed)):
        sheet.write(0, INTX, ''.join(XSSJ_filed[a]), style_heading)
        INTX += 1
    # 写入数据
    data_row = 1
    # UserTable.objects.all()这个是查询条件,可以根据自己的实际需求做调整.
    for i in XSSJ_fx:
        # 格式化datetime
        sheet.write(data_row, 0, i[0])
        sheet.write(data_row, 1, i[1])
        sheet.write(data_row, 2, i[2])
        sheet.write(data_row, 3, i[3])
        # pri_time = i[5].strftime('%Y-%m-%d')
        # oper_time = i.operating_time.strftime('%Y-%m-%d')
        sheet.write(data_row, 4, i[4])
        sheet.write(data_row, 5, i[5])
        data_row = data_row + 1
        # 写出到IO
    output = BytesIO()
    wb.save(output)
    # 重新定位到开始
    output.seek(0)
    response.write(output.getvalue())
    return response
