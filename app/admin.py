from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import Status, Type, Category, Subcategory, CashFlow

admin.site.register(Status)
admin.site.register(Type)

class SubcategoryInline(admin.TabularInline): 
    model = Subcategory
    extra = 1  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]

@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'amount', 'status', 'subcategory', 'category', 'type', 'comment')
    list_filter = (
        ('status'),
        ('subcategory__category__type'),
        ('subcategory__category'),
        ('subcategory'),
        ('created_at', DateRangeFilter),
    )
    search_fields = (
        'comment',
        'subcategory__title',
        'subcategory__category__title',
        'subcategory__category__type__title',
        'status__title',
    )
    # date_hierarchy = 'created_at'  # Дополнительная иерархия дат

    def category(self, obj):
        return obj.subcategory.category.title

    def type(self, obj):
        return obj.subcategory.category.type.title
