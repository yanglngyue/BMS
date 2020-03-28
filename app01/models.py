from django.db import models

# Create your models here.

#
#
# class Book(models.Model):
#     nid=models.AutoField(primary_key=True)
#     title=models.CharField(max_length=32)
#     price=models.DecimalField(max_digits=8,decimal_places=2) # 999999.99
#     pub_date=models.DateTimeField()  # "2012-12-12"
#     publish=models.ForeignKey(to="Publish",on_delete=models.CASCADE)  # 级联删除
#     authors=models.ManyToManyField(to="Author")
#     def __str__(self):
#         return self.title
#
#
# class Publish(models.Model):
#     nid = models.AutoField(primary_key=True)
#     name=models.CharField(max_length=32)
#     email=models.CharField(max_length=32)
#     def __str__(self):
#         return self.name
#
# class Author(models.Model):
#     nid = models.AutoField(primary_key=True)
#     name=models.CharField(max_length=32)
#     age=models.IntegerField()
#     email=models.CharField(max_length=32)
#     ad=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
#
# class AuthorDetail(models.Model):
#     addr=models.CharField(max_length=32)
#     tel=models.IntegerField()
#     #author=models.OneToOneField("Author",on_delete=models.CASCADE)
#     def __str__(self):
#         return self.addr
#
# class UserInfo(models.Model):
#     uid=models.AutoField(primary_key=True)
#     user=models.CharField(max_length=32)
#     pwd=models.CharField(max_length=32)

############## 京城办CRM管理系统 #############

class Company(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.ForeignKey(to="ComDepart",on_delete=models.CASCADE,null=True)#公司名称
    phone = models.CharField(max_length=32)#公司联系人电话
    price_year=models.DecimalField(max_digits=8,decimal_places=2) # 999999.99 会计费年付应收金额
    cost_enddate=models.DateTimeField()  # "2012-12-12" 会计费截止日期
    state=models.ForeignKey(to="ComState",on_delete=models.CASCADE)  # 级联删除 企业存续情况
    newpay_year = models.DecimalField(max_digits=8, decimal_places=2)  # 999999.99 新的收费期间(1年)
    price_month = models.DecimalField(max_digits=8, decimal_places=2)  # 999999.99 本月应收费金额
    control_enddate = models.DateTimeField()  # "2012-12-12" 税控收费截止日期
    control_price = models.DecimalField(max_digits=8, decimal_places=2)  # 999999.99 税控收款
    com_mod = models.CharField(max_length=32)  # 公司规模
    kprice_start = models.DateTimeField()  # 999999.99 会计费收费期间(开始)
    kprice_end = models.DateTimeField()  # 999999.99 会计费收费期间(结束)
    remove_date = models.DateTimeField()  # 999999.99 交接日期
    # sole = models.CharField(max_length=32)#销售人员
    buss_price = models.DecimalField(max_digits=8, decimal_places=2)  # 999999.99 公司年报
    message = models.CharField(max_length=128)#备注
    soles=models.ManyToManyField(to="SoleUser")#销售人员
    kans =models.ManyToManyField(to="Kanter")#会计人员



class ComState(models.Model):
    nid=models.AutoField(primary_key=True)
    state=models.CharField(max_length=32,default='正常')#公司状态（注销、正常、撤户....）
    def __str__(self):
        return self.state


#会计人员表
class Kanter(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)#会计人员名称
    phone = models.CharField(max_length=32)#会计人员电话

    def __str__(self):
        return self.name

#销售人员表
class SoleUser(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)#销售人员名称
    phone = models.CharField(max_length=32)#销售人员电话
    def __str__(self):
        return self.name
# 客户公司表

class ComDepart(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)#客户公司名称
    phone = models.CharField(max_length=32)#客户公司电话
    message = models.CharField(max_length=128)  # 备注

    def __str__(self):
        return self.name