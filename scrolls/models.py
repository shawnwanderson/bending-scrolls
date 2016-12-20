from django.db import models
from django_markdown.models import MarkdownField

# Create your models here.
BOOK_CHOICES = (
        ('WATER', 'Book 1: Water'),
        ('EARTH', 'Book 2: Earth'),
        ('FIRE', 'Book 3: Fire'),

        ('AIR', 'Book 4: Air'),
        ('SPIR', 'Book 5: Spirits'),
        ('CHANG', 'Book 6: Change'),
        ('BALA', 'Book 7: Balance'),
        )
ELEMENT_CHOICES = (
        ('WATER', 'WATER'),
        ('EARTH', 'EARTH'),
        ('FIRE', 'FIRE'),
        ('AIR', 'AIR'),
        )

class Episode(models.Model):
    title = models.CharField(max_length=30)
    description = MarkdownField(blank=True)
    book = models.CharField(max_length=5, choices=BOOK_CHOICES, blank=True)

class Bender(models.Model):
    name = models.CharField(max_length=30)
    element = models.CharField(max_length=5, choices=ELEMENT_CHOICES)
    image = models.ImageField()

class Scroll(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=30)
    description = MarkdownField(blank=True)
    inspirations = MarkdownField(blank=True)
    element = models.CharField(max_length=5, choices=ELEMENT_CHOICES)
    book = models.CharField(max_length=5, choices=BOOK_CHOICES, blank=True)
    image = models.ImageField()

    episode = models.ForeignKey(Episode, blank=True)
    benders = models.ManyToManyField(Bender, blank=True)
    related_scrolls = models.ManyToManyField('self', blank=True, null=True)


