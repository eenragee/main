from django.db import models


class UserFirst(models.Model):
    name = models.CharField('Имя Фамилия', max_length=50)
    phone = models.CharField('Номер телефона', max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class UserReview(models.Model):
    id_user = models.ForeignKey(UserFirst, on_delete=models.CASCADE)
    name_user = models.CharField('Имя Фамилия', max_length=50)
    phone_user = models.CharField('Номер телефона', max_length=12)

    def __str__(self):
        return self.id_user.name

    class Meta:
        verbose_name = 'Контакты по id'
        # verbose_name_plural = 'Пользователи'