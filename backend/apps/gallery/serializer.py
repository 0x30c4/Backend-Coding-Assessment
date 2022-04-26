from rest_framework import serializers
from apps.gallery.models import Items


class ItemsSerializer(serializers.Serializer):

    '''
    The `Items` modle serializer
    '''

    id = serializers.IntegerField(read_only=True)
    author = serializers.HiddenField(default='')
    product_name = serializers.CharField(max_length=100)
    product_description = serializers.CharField()
    # product_image = serializers.ImageField()
    minimum_bid_price = serializers.IntegerField()
    auction_end = serializers.DateTimeField()
    is_bidable = serializers.BooleanField(default=False)

    biders = serializers.JSONField()


    def create(self, validated_data):
        """
        Create and return a new `Image` instance, given the validated data.
        """
        return Items.objects.create(**validated_data)
