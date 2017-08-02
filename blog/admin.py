from django.contrib import admin

from blog.models import Tb20170801

class Tbcontact(admin.ModelAdmin):
    list_display =('xuhao', 'banming', 'title')
    search_fields = ('banming',)


admin.site.register(Tb20170801, Tbcontact)