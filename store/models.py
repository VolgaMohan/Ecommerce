from django.db import models
from django.conf import settings

# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    image = models.ImageField(null=True)
    slug=models.SlugField()
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return self.title
        
class OrderItem(models.Model):
    # item=models.ForeignKey(Item,on_delete=models.CASCADE)
    # active = models.BooleanField(default=True)
    def add_to_cart(self, item_id):
        user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
        item = Item.objects.get(pk=item_id)
        try:
            preexisting_order = OrderItem.objects.get(item=item, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except OrderItem.DoesNotExist:
            new_order = OrderItem.objects.create(
                item=item,
                cart=self,
                quantity=1
                )
            new_order.save()

    # def __str__(self):
    #     return self.title

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.title