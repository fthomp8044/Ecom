from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Order
        fields = ('user')

        # todo: add product and quantitfrom
