from tastypie.resources import ModelResource
from shop.models import Category, Course


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        # Пользователям доступно только чтение ресурсов/категорий...метод GET
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        # Пользователям доступно чтение, запись и удаление ресурсов/курсов...метод GET, POST, DELETE
        allowed_methods = ['get', 'post', 'delete']
