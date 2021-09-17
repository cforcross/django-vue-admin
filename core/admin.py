from django.contrib import admin
from .models import User,Product,Link,Order,OrderItem
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class SuperUserAdmin(UserAdmin):
    ordering =["-id"]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        
    )
    


admin.site.register(User, SuperUserAdmin)

admin.site.register(Product)
admin.site.register(Link)
admin.site.register(Order)
admin.site.register(OrderItem)