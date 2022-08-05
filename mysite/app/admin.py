from django.contrib import admin
from app.models import sign 
from app.models import move
from app.models import jewel
from app.models import Itemcart
from app.models import adminsite
from app.models import orders

#models - DB
# Register your models here.

admin.site.register(sign)
admin.site.register(move)
admin.site.register(jewel)
admin.site.register(Itemcart)
admin.site.register(adminsite)
admin.site.register(orders)