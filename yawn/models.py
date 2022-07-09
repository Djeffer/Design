from django.db import models


class StatusYawn(models.Model):
    static_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.static_name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name="Дата создание")
    order_name = models.CharField(max_length=200, verbose_name="Имя")
    order_phone = models.CharField(max_length=200, verbose_name="Телефон")
    order_city = models.CharField(max_length=200, verbose_name="Город")
    order_status = models.ForeignKey(StatusYawn, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Статус")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class CommentsYawn(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

