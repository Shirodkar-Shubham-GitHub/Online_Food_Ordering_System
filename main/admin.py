from django.contrib import admin
from .models import Item, CartItems
from .models import Contact

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Created By", {'fields': ["created_by"]}),
        ("Title", {'fields': ["title"]}),
        ("Image", {'fields': ["image"]}),
        ("Price", {'fields': ["price"]}),
        ("Plates", {'fields': ["plates"]}),
        ("Slug", {'fields': ["slug"]}),
    ]
    list_display = ('id','created_by','title','price')

class CartItemsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Order Status", {'fields' : ["status"]}),
        ("Delivery Date", {'fields' : ["delivery_date"]})

    ]
    list_display = ('id','user','item','quantity','ordered','ordered_date','delivery_date','status')
    list_filter = ('ordered','ordered_date','status')

admin.site.register(Item,ItemAdmin)
admin.site.register(CartItems,CartItemsAdmin)
admin.site.register(Contact)
