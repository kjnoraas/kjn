from django.db import models
from django.urls import reverse

import uuid


class Genre(models.Model):
    """Model representing an item genre."""
    help_text = 'Enter an item genre (e.g. Decoration)'
    name = models.CharField(max_length=200, help_text=help_text)

    def __str__(self):
        """String for representing the Genre model."""
        return self.name


class Item(models.Model):
    """Model representing an Item (but not a specific instance)."""
    title = models.CharField(max_length=200)

    help_text = 'Describe the item.'
    description = models.TextField(max_length=1000, help_text=help_text)

    help_text = 'Select one or more genres for this item.'
    genre = models.ManyToManyField(Genre, help_text=help_text)

    def __str__(self):
        """String for representing the Item model."""
        return self.title

    def get_absolute_url(self):
        """Return the url to access a detail record for the item."""
        return reverse('item-detail', args=[str(self.id)])


class ItemInstance(models.Model):
    """Model representing a specific instance of an item."""
    help_text = 'Unique ID for this item instance.'
    id_item = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text=help_text)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=500)

    acquisition_date = models.DateField('Acquired', null=True, blank=True)
    dispossession_date = models.DateField('Dispossessed', null=True, blank=True)
    last_used = models.DateField('Last Used', null=True, blank=True)

    price = models.FloatField()

    STATUS = (
        ('g', 'Good'),
        ('l', 'Loaned'),
        ('a', 'Almost Out'),
        ('o', 'Out'),
        ('b', 'Broken'),
        ('d', 'Damaged'),
        ('t', 'Thrown Away'),
        ('m', 'Maintenance'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='g',
        help_text='Item Status',
    )

    class Meta:
        ordering = ['-last_used']

    def __str__(self):
        """String for representing the ItemInstance model."""
        return f'{self.id} ({self.book.title})'


class Location(models.Model):
    """Model representing a location."""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def get_absolute_url(self):
        """Return the URL to access a particular location."""

    def __str__(self):
        """String for representing the Location object."""
        return f'{self.name}'
