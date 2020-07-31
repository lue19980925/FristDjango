from django.contrib import admin
from .models import Book,Hero
class HeroInine(admin.StackedInline):
    model = Hero
    extra = 2
class BookAdmin(admin.ModelAdmin):
    #list_display：显示字段，可以点击列头进行排序
    #list_filter：过滤字段，过滤框会出现在右侧
    #search_fields：搜索字段，搜索框会出现在上侧
    #list_per_page：分页，分页框会出现在下侧
    list_display = ['id','title','pub_date']
    list_filter = ['title','pub_date']
    search_fields = ['title']
    list_per_page = 3
    inlines = [HeroInine]
    #fields：属性的先后顺序
    #fieldsets ：属性分组， 注意: fields和fieldsets 只能设置一个.
class HeroAdmin(admin.ModelAdmin):
    list_display = ['id','name','sex','content']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 3
    #fields：属性的先后顺序
    #fields = ['pub_date', 'title']
    #fieldsets ：属性分组， 注意: fields和fieldsets只能设置一个.
    fieldsets = [('基础信息', {'fields': ['title']}),
                 ('详细信息', {'fields': ['pub_date']}), ]
# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin)
