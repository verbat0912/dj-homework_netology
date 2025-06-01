from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100, verbose_name="название телефона")
    slug = models.SlugField(unique=True, verbose_name="слаг")
    price = models.FloatField(verbose_name="цена")
    image = models.CharField(verbose_name="фото")  # ссылка на фото
    release_date = models.DateField(verbose_name="дата выпуска")
    lte_exists = models.BooleanField(default=False, verbose_name="наличие LTE")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}: {self.price} рублей"
