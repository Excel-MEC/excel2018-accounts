from django.db import models

class userinfo(models.Model):

    class Meta:
        verbose_name = "userinfo"
        verbose_name_plural = "userinfos"

    excelid = models.CharField(max_length=10,primary_key=True,default='excel',null=False)
    name = models.CharField(max_length=100,null=True)
    college = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=50,null=True)
    phone = models.CharField(max_length=10,null=True)
    present = models.BooleanField(default=False)
    stay = models.BooleanField(default=False)
    printed = models.BooleanField(default=False)
    participated_events = models.CharField(max_length=100,blank=True)

    
    def __str__(self):
        k = self.excelid+":  "+self.name
        return str(k)
  
    # def save(self,*args,**kwargs):
    # 	code=uniqueid()
    # 	self.excelid=code
    # 	super(userinfo,self).save(*args,**kwargs)
