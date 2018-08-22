from django.db import models


class venue(models.Model):

	class Meta:
		verbose_name = "venue"
		verbose_name_plural = "venues"

	venue_id=models.CharField(max_length=20,primary_key=True,null=False)
	occupied=models.BooleanField(default=False)
	vm_1=models.CharField(max_length=1000,null=False)
	vm_2=models.CharField(max_length=1000,default='nil')
	vm_num_1=models.CharField(max_length=10,null=True)
	vm_num_2=models.CharField(max_length=10,default='nil')
	power=models.CharField(max_length=1000,null=False)
	power_num=models.CharField(max_length=10,null=False)
	current_event=models.CharField(max_length=15,default='nil')
	next_event=models.CharField(max_length=15,default="nil")

	def __str__(self):
		return (self.venue_id)


class event(models.Model):

	class Meta:
		verbose_name = "event"
		verbose_name_plural = "events"


	event_id=models.CharField(max_length=15,primary_key=True)
	event_name=models.CharField(max_length=100,null=False,default="")
	venue_id=models.CharField(max_length=20,null=False)
	em=models.CharField(max_length=1000,null=False)
	em_num=models.CharField(max_length=1000,null=False)
	day=models.DateField(null=False)
	time=models.TimeField(null=False)
	endtime=models.TimeField(null=False)
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
