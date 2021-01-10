from django.conf import settings
from django.db import models
from django.utils import timezone

class dataxx(models.Model):
    name = models.CharField(max_length =200)
    number = models.IntegerField(default = 0)
    password = models.CharField(max_length = 200, default = " ")
    
    def __str__(self):
        return self.name

class admin_account(models.Model):
    name = models.CharField(max_length =200)
    idd = models.CharField(max_length =200)
    password = models.CharField(max_length =200)
    
    def __str__(self):
        return self.name


class 제8기동사단(models.Model):
    name = models.CharField(max_length =20, default = " ")
    number = models.IntegerField(default = 0)
    password = models.CharField(max_length = 200, default = " ")
    
    def __str__(self):
        return str(self.number)+".  "+self.name

# ================================사단직할대=====================================
class 정보통신대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 직할공병대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 직할군수지원대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 기갑수색대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 보충중대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 의무대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 군사경찰대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 본부대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name    

class 화생방지원대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 정보대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 사단직할대(models.Model):
    batta1 = models.ForeignKey(정보통신대대, on_delete = models.PROTECT)
    batta2 = models.ForeignKey(직할공병대대, on_delete = models.PROTECT)
    batta3 = models.ForeignKey(직할군수지원대대, on_delete = models.PROTECT)
    batta4 = models.ForeignKey(기갑수색대대, on_delete = models.PROTECT)
    batta5 = models.ForeignKey(보충중대, on_delete = models.PROTECT)
    batta6 = models.ForeignKey(의무대, on_delete = models.PROTECT)
    batta7 = models.ForeignKey(군사경찰대 , on_delete = models.PROTECT)
    batta8 = models.ForeignKey(본부대, on_delete = models.PROTECT)
    batta9 = models.ForeignKey(화생방지원대대, on_delete = models.PROTECT)
    batta10 = models.ForeignKey(정보대대, on_delete = models.PROTECT)

    def get_batta_list(self):
        return [batta1, batta2, batta3, batta4, batta5, batta6, batta7, batta8, batta9, batta10]

    def __str__(self):
        return ''.join(self.get_batta_list())

# ================================제 1기갑여단=====================================
class 제101기보대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 제122기보대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 제137기보대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 기갑군수지원대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 기갑참모부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name
        
class 기갑직할대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 기갑여단(models.Model):
    batta1 = models.ForeignKey(제101기보대대, on_delete = models.PROTECT)
    batta2 = models.ForeignKey(제122기보대대, on_delete = models.PROTECT)
    batta3 = models.ForeignKey(제137기보대대, on_delete = models.PROTECT)
    batta4 = models.ForeignKey(기갑군수지원대대, on_delete = models.PROTECT)
    batta5 = models.ForeignKey(기갑참모부, on_delete = models.PROTECT)
    batta6 = models.ForeignKey(기갑직할대, on_delete = models.PROTECT)
    
    def get_batta_list(self):
        return [batta1, batta2, batta3, batta4, batta5, batta6]

    def __str__(self):
        return ''.join(self.get_batta_list())
# ================================ 참모처 =====================================
class 인사처(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 정보처(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 작전처(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 군수처(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 화력실(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 교훈처(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 지통처(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 군종부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 공보정훈부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 재정부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 지휘부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 작계처(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 감찰부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 법무부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 참모처(models.Model): 
    batta1 = models.ForeignKey(인사처, on_delete = models.PROTECT)
    batta2 = models.ForeignKey(정보처, on_delete = models.PROTECT)
    batta3 = models.ForeignKey(작전처, on_delete = models.PROTECT)
    batta4 = models.ForeignKey(군수처, on_delete = models.PROTECT)
    batta5 = models.ForeignKey(화력실, on_delete = models.PROTECT)
    batta6 = models.ForeignKey(지통처, on_delete = models.PROTECT)
    batta7 = models.ForeignKey(군종부, on_delete = models.PROTECT)
    batta8 = models.ForeignKey(공보정훈부, on_delete = models.PROTECT)
    batta9 = models.ForeignKey(재정부, on_delete = models.PROTECT)
    batta10 = models.ForeignKey(지휘부, on_delete = models.PROTECT)
    batta11 = models.ForeignKey(작계처, on_delete = models.PROTECT)
    batta12 = models.ForeignKey(교훈처, on_delete = models.PROTECT)
    batta13 = models.ForeignKey(감찰부, on_delete = models.PROTECT)
    batta14 = models.ForeignKey(법무부, on_delete = models.PROTECT)
    def get_batta_list(self):
        return [batta1, batta2, batta3, batta4, batta5, batta6, batta7, batta8, batta9, batta10, batta11, batta12, batta13, batta14]

    def __str__(self):
        return ''.join(self.get_batta_list())

# =================================제 60여단=====================================
class 제107기보대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제26전차대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제32전차대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제60군수지원대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제60직할대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제60참모부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제60여단(models.Model):
    batta1 = models.ForeignKey(제107기보대대, on_delete = models.PROTECT)
    batta2 = models.ForeignKey(제26전차대대, on_delete = models.PROTECT)
    batta3 = models.ForeignKey(제32전차대대, on_delete = models.PROTECT)
    batta4 = models.ForeignKey(제60군수지원대대, on_delete = models.PROTECT)
    batta5 = models.ForeignKey(제60직할대, on_delete = models.PROTECT)
    batta6 = models.ForeignKey(제60참모부, on_delete = models.PROTECT)

    def get_batta_list(self):
        return [batta1, batta2, batta3, batta4, batta5, batta6]

    def __str__(self):
        return ''.join(self.get_batta_list())
# =================================제 73여단=====================================
class 제123기보대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제125기보대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제57전차대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제73군수지원대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제73직할대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제73참모부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제73여단(models.Model):
    batta1 = models.ForeignKey(제123기보대대, on_delete = models.PROTECT)
    batta2 = models.ForeignKey(제125기보대대, on_delete = models.PROTECT)
    batta3 = models.ForeignKey(제57전차대대, on_delete = models.PROTECT)
    batta4 = models.ForeignKey(제73군수지원대대, on_delete = models.PROTECT)
    batta4 = models.ForeignKey(제73직할대, on_delete = models.PROTECT)
    batta4 = models.ForeignKey(제73참모부, on_delete = models.PROTECT)

    def get_batta_list(self):
        return [batta1, batta2, batta3, batta4, batta5, batta6]

    def __str__(self):
        return ''.join(self.get_batta_list())
# ================================포병여단=====================================
class 제50포병대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 제95포병대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number)+".  " + self.tet.name

class 제228포병대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 제231포병대대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 포병직할대(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 포병참모부(models.Model):
    tet = models.ForeignKey(제8기동사단, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.tet.number) + ".  " + self.tet.name

class 포병여단(models.Model):
    batta1 = models.ForeignKey(제50포병대대, on_delete = models.PROTECT)
    batta2 = models.ForeignKey(제95포병대대, on_delete = models.PROTECT)
    batta3 = models.ForeignKey(제228포병대대, on_delete = models.PROTECT)
    batta4 = models.ForeignKey(제231포병대대, on_delete = models.PROTECT)
    batta5 = models.ForeignKey(포병직할대, on_delete = models.PROTECT)
    batta6 = models.ForeignKey(포병참모부, on_delete = models.PROTECT)

    def get_batta_list(self):
        return [batta1, batta2, batta3, batta4, batta5, batta6]

    def __str__(self):
        return ''.join(self.get_batta_list())
#< +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ >
class 질문지(models.Model):
    부대명 = models.CharField(max_length=200)
    Q1 = models.CharField(max_length=200)
    Q2 = models.CharField(max_length=200)
    Q3 = models.CharField(max_length=200)
    Q4 = models.CharField(max_length=200)
    Q5 = models.CharField(max_length=200)
    Q6 = models.CharField(max_length=200)
    Q7 = models.CharField(max_length=200)
    Q8 = models.CharField(max_length=200)
    Q9 = models.CharField(max_length=200)
    Q10 = models.CharField(max_length=200)

    def __str__(self):
        return self.부대명

    def get_all_qs(self):
        return [self.Q1,self.Q2,self.Q3,self.Q4,self.Q5,self.Q6,self.Q7,self.Q8,self.Q9]