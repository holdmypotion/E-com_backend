import uuid
from django.db import models
from django.utils.text import slugify


def get_image_filename(instance, filename):
    slug = instance.slug
    ext = filename.split('.')[-1]
    filename = f'{slug}-{uuid.uuid4()}.{ext}'

    return filename


class Section(models.Model):
    """Section Model"""
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to=get_image_filename,
        verbose_name='Image1',
        null=True,
        blank=True
    )

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
    image1 = models.ImageField(
        upload_to=get_image_filename,
        verbose_name='Image1',
        null=True,
        blank=True
    )
    image2 = models.ImageField(
        upload_to=get_image_filename,
        verbose_name='Image2',
        null=True,
        blank=True
    )
    image3 = models.ImageField(
        upload_to=get_image_filename,
        verbose_name='Image3',
        null=True,
        blank=True
    )
    image4 = models.ImageField(
        upload_to=get_image_filename,
        verbose_name='Image4',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)