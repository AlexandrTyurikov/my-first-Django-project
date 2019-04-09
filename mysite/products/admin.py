from django.contrib import admin
from . import models
from django.utils.html import format_html


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
#        'image_tag',
        'creation_date',
        'update_date',
    )

#    def image_tag(self, obj):
#        return format_html('<img src="{}" width="100" />'.format(obj.image.url))
#
#    image_tag.short_description = 'изображение'


#    class Meta:
#        model = models.Products


admin.site.register(models.Products, ProductsAdmin)
admin.site.register(models.Author)
admin.site.register(models.Genre)
