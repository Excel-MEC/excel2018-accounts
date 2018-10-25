from django.db import models

class event(models.Model):

	class Meta:
		verbose_name = "event"
		verbose_name_plural = "events"


	event_id=models.CharField(max_length=15,primary_key=True)
	event_name=models.CharField(max_length=100,null=False,default="")
	status=models.IntegerField(null=False,default=0)
	paid=models.BooleanField(default=False)
	short_list=models.CharField(max_length=200,blank=True,null=True,default="nil")
	winner1=models.CharField(max_length=60,blank=True,default="nil")
	winner2=models.CharField(max_length=60,blank=True,default="nil")
	winner3=models.CharField(max_length=60,blank=True,default="nil")
	participants=models.CharField(max_length=10000,blank=True,default="nil")

	def __str__(self):
		return (self.event_id)

	def get_absolute_url(self):
		return reverse("controlroom", kwargs={"pk": self.pk})
