from django.contrib import admin

from .models import Genre, Item, ItemInstance, Location


admin.site.register(Genre)
admin.site.register(Item)
admin.site.register(ItemInstance)
admin.site.register(Location)
