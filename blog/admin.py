from django.contrib import admin
from blog.models import Test,Contact,Tag

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
#    fields = ('name','email')   #类仅有此行只显示 name 和 email 部分
    list_display = ('name','age','email')
    inlines = [TagInline]  #内联
    search_fields = ('name',)
    fieldsets = (
        [
            'Main',
            {
                'fields':('name','email'),
            }
        ],
        [
            'Advance',
            {
                'classes':('collapse',), #css
                'fields':('age',),
            }
        ]

    )

admin.site.register(Contact,ContactAdmin)
admin.site.register([Test,Tag])

