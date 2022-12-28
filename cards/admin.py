from django.contrib import admin
from .models import *
# Register your models here.


# class ReviewInline(admin.TabularInline):
#     fields = ('author', 'text')
#     model = Review
#     max_num = 15
#     min_num = 1


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    # inlines = [ReviewInline, ]
    pass


admin.site.register(Type)
admin.site.register(Genre)
admin.site.register(Review)
