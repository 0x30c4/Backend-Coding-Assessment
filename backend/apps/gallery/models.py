from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def biders_default():
    '''
    The default json template for biders.
    '''
    return {"biders": [
        {
            "bider_id": -1,
            "bid_amount": -1,
            "time_of_bid": "",
        }
    ]}


class Items(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    # product_image = models.ImageField(upload_to='images')
    minimum_bid_price = models.IntegerField()

    # The end of the auction.
    auction_end = models.DateTimeField()

    # is the item still bidable.
    is_bidable = models.BooleanField(default=False)

    # people who has bided on the item
    biders = models.JSONField("BiderData", default=biders_default)

    class Meta:
        ordering = ['created']
