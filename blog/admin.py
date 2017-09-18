from django.contrib import admin

from blog.models import News

class Tbcontact(admin.ModelAdmin):
    list_display =('xuhao', 'banming', 'title')
    search_fields = ('banming',)


admin.site.register(News, Tbcontact)