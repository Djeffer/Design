from django.db import models


class DesignSlid(models.Model):
    design_img = models.ImageField(upload_to='slid_img/')
    design_title = models.CharField(max_length=200, verbose_name='Загаловок')
    design_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')
    design_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.design_title

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио img"


