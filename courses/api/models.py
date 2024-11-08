from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


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
        excludes = ['reviews_qty', 'created_at']
        authentication = CustomAuthentication()
        authorization = Authorization()

    # Добавляет category_id в таблицу course при создании новой записи
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    # Добавляет category_id в таблицу course ко всем записям
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
