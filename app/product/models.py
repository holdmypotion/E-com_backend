from django.db import models


class Section(models.Model):
    """Section Model"""
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    """Product Model"""

    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE,
        related_name='products', related_query_name='product'
    )

    # TODO: AddImage

    def __str__(self):
        """String representation"""
        return self.title
