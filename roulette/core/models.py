from django.db import models
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):
    title = models.CharField(_('title'), max_length=30)
    image = models.ImageField(_('image'), upload_to='img/items/')
    number = models.PositiveIntegerField(_('number'))
    visible = models.BooleanField(_('visible'), default=True)

    def __str__(self):
        return self.title