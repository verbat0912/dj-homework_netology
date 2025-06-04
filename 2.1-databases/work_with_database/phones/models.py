from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name="название телефона")
    image = models.CharField(verbose_name="фото")  # ссылка на фото
    price = models.FloatField(verbose_name="цена")
    release_date = models.DateField(verbose_name="дата выпуска")
    lte_exists = models.BooleanField(default=False, verbose_name="наличие LTE")
    slug = models.SlugField(unique=True, verbose_name="слаг")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}: {self.price} рублей"
