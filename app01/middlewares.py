
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AutuMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        #获取请求的访问路径以拼接next url
        next_url = request.path_info

        # 白名单
        print(request.path)
        if request.path in ["/login/","/reg/"]:
            return None

        # print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            return redirect("/login/?next={}".format(next_url))
