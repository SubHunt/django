from django.db import models

# Create your models here.
# Функция создания пути к файлу путем имя пользователя(оно же название папки/ название файла)


def path_to_file(filename):
    user = User.login
    return f'{user}/{filename}'


class User(models.Model):
    login = models.CharField(
        max_length=20, primary_key=True, verbose_name='Логин')
    name = models.CharField(max_length=20, blank=False, verbose_name='Имя')
    password = models.CharField(max_length=50, verbose_name='Пароль')
    email = models.EmailField(max_length=50, verbose_name='Е-майл')
    is_admin = models.BooleanField(
        default=False, verbose_name='Администратор?')
    path_to_user = models.CharField(
        max_length=50, verbose_name='Путь к файлам пользователя')

    def __str__(self):
        return self.title


class Files(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=100, unique=True,
                             verbose_name='Название файла')
    description = models.TextField(blank=True, verbose_name='Описание')
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата создания')
    date_last_load = models.DateTimeField(
        auto_now=True, db_index=True, verbose_name='Дата последнего обновления')
    link_download = models.URLField(
        max_length=50, unique=True, blank=True, verbose_name="Прямая ссылка")
    path = models.FileField(upload_to=path_to_file,
                            verbose_name='Путь к файлу')

    def __str__(self):
        return self.title
