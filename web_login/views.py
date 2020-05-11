from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
import hashlib #MD5解密
from web_login.models import Xtyh, WebLogin
import datetime
# Create your views here.


def login(request):
    if request.method == "get":
        return render(request, 'login.html')
    if request.method == "post":
        login_info = request.POST
        username = login_info.get('user', None)
        userpwd = login_info.get('pwd', None)
        userpwd = hashlib.md5(userpwd.encode("utf8")).hexdigest()
        userpwd = userpwd.upper()
        if username != "":
            if userpwd != "":
                try:
                   db_系统用户 = Xtyh.objects.get(用户编号=username)
                   if db_系统用户.密码 != userpwd:
                       return render(request, 'login.html', {'msg': "密码错误"})
                   else:
                       now_today = datetime.datetime.now()
                       now_today_day = datetime.date.today()
                       request.session['is_login'] = True
                       request.session['user_name'] = username
                       request.session.set_expiry(0)
                       weblogin = WebLogin(username=username, apppage='首页', appname='web_xx控制台', date=now_today,
                                           date2=now_today_day)
                       weblogin.save()
                       return HttpResponse("登录成功")
                except:
                    return render(request, "login.html", {'msg': "无此账号"})