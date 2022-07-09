from django.db import models


class PriceCard(models.Model):
    pc_title = models.CharField(max_length=200, verbose_name="Название")
    pc_value = models.CharField(max_length=20, verbose_name="Цена")
    pc_description = models.TextField(verbose_name="Описание")
    pc_img = models.ImageField(upload_to='price_img')

    def __str__(self):
        return self.pc_title

    class Meta:
        verbose_name = "Название"
        verbose_name_plural = "Цены"



