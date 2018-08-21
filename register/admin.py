from django.contrib import admin
from register.models import userinfo,winners,paid_userinfo,paid_winners
from controlroom.models import venue,event
# Register your models here.

admin.site.register(userinfo)
admin.site.register(winners)
admin.site.register(venue)
admin.site.register(event)
admin.site.register(paid_userinfo)
admin.site.register(paid_winners)
