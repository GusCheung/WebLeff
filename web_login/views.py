from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
import hashlib #MD5解密
from web_login.models import Xtyh, WebLogin
import datetime
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == 'GET':
        # userAgent = request.META['HTTP_USER_AGENT']  # 访问的设备信息

        return render(request, 'login.html')
    if request.method == 'POST':
        login_info = request.POST
        userName = login_info.get('user', None)
        userPwd = login_info.get('pwd', None)
        userPwd = hashlib.md5(userPwd.encode("utf8")).hexdigest()
        userPwd = userPwd.upper()
        if userName != "":
            if userPwd != "":
                try:
                    db_系统用户 = Xtyh.objects.get(用户编号=userName)
                    if db_系统用户.密码 != userPwd:
                        messages.success(request, '密码错误')
                        return render(request, 'login.html')
                    else:
                        now_today = datetime.datetime.now()
                        now_today_day = datetime.date.today()
                        request.session['is_login'] = True
                        request.session['user_name'] = userName
                        request.session.set_expiry(0)
                        weblogin = WebLogin(username=userName, apppage='首页', appname='web_xx控制台', date=now_today,
                                            date2=now_today_day)
                        weblogin.save()
                        return HttpResponse('登录成功')
                # 录入weblogin
                # now_time = datetime.datetime.now()
                # weblogin = WebLogin(username=userName, apppage='首页', appname='web_xx控制台', date=now_time)
                # weblogin.save()
                # cursor = connection.cursor()
                # cursor.execute("insert into web_login记录(date, appname, apppage, Host, username) values (now_time,'web_云控制','首页','1.1.1',userName)")
                except:
                    messages.success(request, '用户不存在')
                    return render(request, 'login.html')
