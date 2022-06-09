from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

from django.utils.timezone import now


class Upload(models.Model):
    """上传文件使用的映射类"""
    # 访问页面次数
    download_count = models.IntegerField(verbose_name="访问次数", default=0)
    # 该字段为一个文件的唯一标识符
    code = models.CharField(verbose_name="code", max_length=8)
    # 文件上传时间
    file_upload_time = models.DateTimeField(verbose_name="上传时间", default=now())
    # 文件存储路径
    file_save_path = models.CharField(verbose_name="文件存储路径", max_length=64)
    # 文件名
    file_name = models.CharField(verbose_name="文件名", max_length=32)
    # 文件大小
    file_size = models.CharField(verbose_name="文件大小", max_length=8)
    # 上传文件的客户端IP地址
    customer_upload_ip = models.CharField(verbose_name="客户端上传的IP地址", max_length=16)


    # 该方法用于格式化类的实例的打印样式，便于测试
    def __str__(self):
        return self.file_name