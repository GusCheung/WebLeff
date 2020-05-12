from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
import hashlib  # MD5解密

from django.views.decorators.csrf import csrf_exempt

from web_login.models import Xtyh, WebLogin
import datetime
from django.contrib import messages
import requests

# Create your views here.


# *----------------------登录函数----------------------*
def login(request):
        if request.method == 'GET':
            try:
                code = request.Get.get('code',)
                state = request.Get.get('state',)
                appId = 'dingoaebcajmgx7n5zqbym'
                appSecret = 'LY149e6_fDQRthXGziFA2Z9WwU5dIFFJwfq1BdUxbikkNlgkzS8h7WD_F-kSijqj'

                token = requests.get(f'https://oapi.dingtalk.com/sns/gettoken?appid={appId}&appsecret={appSecret}')
                access_token = token.json()["access_token"]
                tmp_auth_code = requests.post(f"https://oapi.dingtalk.com/sns/get_persistent_code?access_token={access_token}",
                                              json={
                                                  "tmp_auth_code": code
                                              })
                tmp_code = tmp_auth_code.json()
                print(tmp_code)
                openid = tmp_code['openid']
                persistent_code = tmp_code['persistent_code']

                sns_token_request = requests.post(f"https://oapi.dingtalk.com/sns/get_sns_token?access_token={access_token}",
                                                  json={
                                                      "openid": openid,
                                                      "persistent_code": persistent_code
                                                  })
                # userAgent = request.META['HTTP_USER_AGENT']  # 访问的设备信息
                sns_token = sns_token_request.json()['sns_token']

                user_info_request = requests.get(f'https://oapi.dingtalk.com/sns/getuserinfo?sns_token={sns_token}')

                user_info = user_info_request.json()['user_info']
                print(user_info)
                return redirect('../index')
            except:  # 异常报错 没有找用户
                return render(request, 'login.html')

        if request.method == 'POST':
            login_info = request.POST
            userName = login_info.get('user', None)  # 用户
            userPwd = login_info.get('pwd', None)  # 用户密码
            userPwd = hashlib.md5(userPwd.encode("utf8")).hexdigest()  # 将密码加密
            userPwd = userPwd.upper()  # 字符串小写字母转换大写字母
            if userName != "":  # 判断用户不是空值
                if userPwd != "":  # 判断密码不是空值
                    try:  # 异常处理 类似IF 不过只有再程序出现异常才会执行
                        db_系统用户 = Xtyh.objects.get(用户编号=userName)  # 查询数据库用户的资料并写入db_系统用户的列表里
                        print(db_系统用户)
                        if db_系统用户.密码 != userPwd:  # 判断密码是否和输入的一样
                            messages.success(request, '密码错误')
                            return render(request, 'login.html')
                        else:
                            now_today = datetime.datetime.now()  # 时间
                            now_today_day = datetime.date.today()  # 日期
                            request.session['is_login'] = True
                            request.session['user_name'] = userName
                            request.session.set_expiry(0)
                            # 会话控制 { 上面以request.session 开头的都是记入session值 防止账号多次登录 可以在webleff文件夹下的settings.py设置时间 }
                            weblogin = WebLogin(username=userName, apppage='首页', appname='web_xx控制台', date=now_today,
                                                date2=now_today_day)
                            weblogin.save()
                            # 保存登录记录
                            return redirect("../index")
                            # 返回登录成功页面
                    except:  # 异常报错 没有找用户
                        messages.success(request, '用户不存在')
                        return render(request, 'login.html')

@csrf_exempt
# *----------------------主页函数----------------------*
def index(request):
    return render(request, 'index.html')


# *----------------------注销----------------------*
def user_logout(request):
    request.session.flush()  # 清除seesion
    return redirect("..")
