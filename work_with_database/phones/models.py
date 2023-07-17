from django.db import models
from datetime import date


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    #name = models.CharField(max_length=254)
    # price = models.IntegerField
    # image = models.ImageField
    #
    # release_date = models.DateField
    # lte_exists = models.BooleanField
    # slug = models.SlugField(max_length = 200)
    id = models.PositiveIntegerField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=100, verbose_name='name')
    price = models.PositiveIntegerField(verbose_name='price',default=0)
    image = models.URLField(max_length=200, verbose_name='image', default="default url")
    release_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='release_date',default=date.today)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=150, unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    #pass
