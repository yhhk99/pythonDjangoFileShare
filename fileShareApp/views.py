import string


from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from random import sample
# Create your views here.

#创建视图类需要基础视图基类
# 例如TemplateView 就是用于展示页面的模板视图基类
# 该类仅提供get方法，用于处理get请求
# 当然也可自定义其他方法，例如post方法
from fileShareApp.models import Upload


class HomeView(TemplateView):
    """
    用于展示主页的视图类
    """
    # 展示主页的话，只需提供模板文件的名字即可
    # 当客户端发起get请求时，由父类的get方法处理请求
    # 当属性用于提供模板文件，在父类的方法中被调用
    # template_name = 'home_page.html'
    # template_name = 'base/base.html'
    template_name = 'fileShareContent.html'

    def post(self, request):
        # 如果表单中有文件
        if request.FILES:
            file = request.FILES.get('choose_files_info')
            name = file.name
            size = int(file.size)
            path = 'djangoFileShareSystem/statics/uploadFiles/' + name
            with open(path, 'wb') as f:
                f.write(file.read())

            code = ''.join(sample(string.digits, 8))
            upload = Upload(file_save_path=path, file_name=name, file_size=size, code=code,customer_upload_ip=str(request.META['REMOTE_ADDR']))
            upload.save()
            return HttpResponsePermanentRedirect("/s/" + code)


class DisplayView(ListView):
    """展示文件的视图类"""
    template_name = 'base/base.html'

    def get(self, request, code):
        uploads = Upload.objects.filter(code=code)
        if uploads:
            for upload in uploads:
                upload.download_count += 1
                upload.save()
        return render(request, 'fileShareContent.html', {'content': uploads, 'host': request.get_host()})


class MyView(ListView):
    """用户管理视图类，就是用户管理文件的那个页面的视图类"""

    def get(self, request):
        ip = request.META["REMOTE_ADDR"]
        print("ip is : ", ip)
        uploads = Upload.objects.filter(customer_upload_ip=ip)
        for upload in uploads:
            upload.download_count += 1
        upload.save()

        return render(request, 'fileShareContent.html', {'content': uploads})
