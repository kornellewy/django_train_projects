from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.
CATEGORY_CHOICES = (
    ('S','Shirt'),
    ('SW','Sport wear'),
    ('OW','Outwear')
)

LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger')
)

class Item(models.Model):
    added_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    catergory = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    def __str__(self):
        return '{}'.format(self.title)
    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug': self.slug
        })
    def get_add_to_cart_url(self):
        return reverse('core:add_to_cart', kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse('core:remove_from_cart', kwargs={
            'slug': self.slug
        })

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    ordered_date = models.DateField()
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.user.username)
