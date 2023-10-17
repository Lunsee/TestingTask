from django.contrib import admin
from .models import MenuItem
from django.contrib import admin
from .models import MenuItem
#from .forms import MenuItemForm
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url', 'named_url')


admin.site.register(MenuItem, MenuItemAdmin) # связываем с models

