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
from django.db.models import Q
import re
from django.db import connection  # 自定义查询语句


@csrf_exempt
def IT_info(request):
    if request.method == "POST":
        lc资产编号 = request.POST.get('data[a]')
        if lc资产编号 != '':
            try:
                seek_itzc = it资产.objects.get(资产编号=lc资产编号.strip())
                if seek_itzc != '':
                    status = True
                return JsonResponse({"status": status,
                                     'lc资产编号': seek_itzc.贴纸编码.strip()
                                     })
            except:
                status = False
                return JsonResponse({"status": status,
                                     'lc资产编号': '未搜素到"' + lc资产编号.strip() + '"资产编号,请重新输入'
                                     })
        else:
            status = False
            return JsonResponse({"status": status,
                                 'lc资产编号': '关键词不能为空！'
                                 })
    lc提示 = '请在搜索框中输入资产编号！'
    lc = ['Windows', 'iPhone', 'Linux', 'Android', 'BlackBerry', 'Macintosh', 'Ubuntu']
    userAgent = request.META['HTTP_USER_AGENT']
    for lc1 in lc:
        if re.findall(lc1, userAgent):
            lce = re.findall(lc1, userAgent)
    if lce[0] == 'Windows' or lce[0] == 'Macintosh':
        lc设备 = '电脑端'
    else:
        lc设备 = '手机端'
    return render(request, 'IT_info.html', {'lc提示': lc提示,
                                            'lc设备': lc设备
                                            })


# def IT_info(request):
#     return render(request, 'graph_chartjs.html')

@csrf_exempt
def IT_info_lctzbm(request, lctzbm):
    try:
        seek_itzc = it资产.objects.get(Q(贴纸编码=lctzbm.strip()) & Q(删除标记='0'))
        seek_itzc_使用人 = it资产.objects.filter(Q(使用人=seek_itzc.使用人) & ~Q(贴纸编码=lctzbm.strip()) & Q(删除标记='0'))
        cursor = connection.cursor()
        cursor.execute("  select  "
                       "(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='花都总部' and 资产类型='台式主机') as "
                       "台式主机数量 "
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='花都总部'and 资产类型='显示器') as 显示器数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='花都总部'and 资产类型='打印机') as 打印机数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='花都总部'and 资产类型='服务器') as 服务器数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='花都总部'and 资产类型='网络设备') as "
                       "网络设备数量 "
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='花都总部'and 资产类型='其它设备') as "
                       "其它设备数量 "
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='花都总部'and 资产类型='摄像头') as 摄像头数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='花都总部'and 资产类型='笔记本') as 笔记本数量"
                       )
        itzc_zb = cursor.fetchall()  # 读取全部
        cursor.execute("  select  "
                       "(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='白云运营' and 资产类型='台式主机') as "
                       "台式主机数量 "
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='白云运营'and 资产类型='显示器') as 显示器数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='白云运营'and 资产类型='打印机') as 打印机数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='白云运营'and 资产类型='服务器') as 服务器数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='白云运营'and 资产类型='网络设备') as "
                       "网络设备数量 "
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='白云运营'and 资产类型='其它设备') as "
                       "其它设备数量 "
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='白云运营'and 资产类型='摄像头') as 摄像头数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='白云运营'and 资产类型='笔记本') as 笔记本数量"
                       )
        itzc_by = cursor.fetchall()
        cursor.execute("  select  "
                       "(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='总部机房' and 资产类型='台式主机') as "
                       "台式主机数量 "
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='总部机房'and 资产类型='显示器') as 显示器数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='总部机房'and 资产类型='打印机') as 打印机数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='总部机房'and 资产类型='服务器') as 服务器数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='总部机房'and 资产类型='网络设备') as "
                       "网络设备数量 "
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='总部机房'and 资产类型='其它设备') as "
                       "其它设备数量 "
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='总部机房'and 资产类型='摄像头') as 摄像头数量"
                       ",(select COUNT(资产类型) as 台式主机数量 FROM [LEFF].[dbo].[IT资产] where 区域='总部机房'and 资产类型='笔记本') as 笔记本数量"
                       )
        itzc_jf = cursor.fetchall()
        cursor.close()  # 关闭游标
        biaoti_list = ['台式主机', '显示器', '打印机', '服务器', '网络设备', '其它设备', '摄像头', '笔记本']
        itzc_zb_list = []
        itzc_by_list = []
        itzc_jf_list = []

        for a in itzc_zb[0]:
            itzc_zb_list.append(a)
        itzc_zb = itzc_zb_list


        for a in itzc_by[0]:
            itzc_by_list.append(a)
        itzc_by = itzc_by_list


        for a in itzc_jf[0]:
            itzc_jf_list.append(a)
        itzc_jf = itzc_jf_list

        # Ajax
        if request.method == "POST":
            lc资产编号 = request.POST.get('data[a]')
            zhmodel = re.compile(u'[\u4e00-\u9fa5]')  # 检查中文
            match = zhmodel.search(lc资产编号)
            if match:
                print('是中文')
            else:
                print('不是中文')
            if lc资产编号 != '':
                try:
                    seek_itzc = it资产.objects.get(Q(资产编号=lc资产编号.strip()) & Q(删除标记='0'))
                    if seek_itzc != '':
                        status = True
                    return JsonResponse({"status": status,
                                         'lc资产编号': seek_itzc.贴纸编码
                                         })
                except:
                    status = False
                    return JsonResponse({"status": status,
                                         'lc资产编号': '未搜素到"' + lc资产编号.strip() + '"资产编号,请重新输入'
                                         })
            else:
                status = False
                return JsonResponse({"status": status,
                                     'lc资产编号': '关键词不能为空！'
                                     })
        lc = ['Windows', 'iPhone', 'Linux', 'Android', 'BlackBerry', 'Macintosh', 'Ubuntu']
        userAgent = request.META['HTTP_USER_AGENT']
        for lc1 in lc:
            if re.findall(lc1, userAgent):
                lce = re.findall(lc1, userAgent)
        if lce[0] == 'Windows' or lce[0] == 'Macintosh':
            lc设备 = '电脑端'
        else:
            lc设备 = '手机端'
        return render(request, 'IT_info.html', {'seek_itzc': seek_itzc,
                                                'seek_itzc_使用人': seek_itzc_使用人,
                                                'lc错误': False,
                                                'itzc_zb': itzc_zb,
                                                'itzc_by': itzc_by,
                                                'itzc_jf': itzc_jf,
                                                'biaoti_list': biaoti_list,
                                                'lc设备': lc设备
                                                })
    except:
        return render(request, 'IT_info.html', {'lc错误': True})
