from django.contrib import admin
from .models import Category, Course

admin.site.site_header = "Course Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin area"


# Свзяваем и добавляем Таблицу с курсами в Раздел категории
class CoursesInLine(admin.TabularInline):
    model = Course
    # Скрываем поле
    exclude = ['created_at']
    # Количество пустых полей для добавления новых курсов
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    # Добавляем таблицу с курсами в соответсвующую категорию
    inlines = [CoursesInLine]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
