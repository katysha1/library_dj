from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    published_year = models.PositiveIntegerField(verbose_name="Год издания", null=True, blank=True)
    cover = models.ImageField(upload_to='book_covers/', verbose_name="Обложка", null=True, blank=True)

    def __str__(self):
        return self.title