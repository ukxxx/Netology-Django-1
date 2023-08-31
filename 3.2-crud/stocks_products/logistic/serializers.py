from logistic.models import Product, Stock, StockProduct
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = '__all__'
    
    # def create(self, data):
    #     print('Криэйт вызван!!!')
    #     address = self.context['request'].get('address')
    #     print(address)

    #     try:
    #         stock = Stock.objects.get(address=address)
    #         print
    #     except Stock.DoesNotExist:
    #         raise serializers.ValidationError('Такой склад не найден')
        
    #     data['stock'] = stock
    #     print(data)
        
    #     return super().create(data)


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(stock= positions[0][stock], **validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            position['stock'] = stock.id
            StockProduct.objects.create(**position)
        return stock
    
    def validate(self, data):
        raise ValidationError('Такой склада уже существует')
        return data

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            product = position.get('product')
            quantity = position.get('quantity')
            price = position.get('price')

            stock_product, created = StockProduct.objects.get_or_create(
                stock=stock,
                product=product,
                defaults={'quantity': quantity, 'price': price}
            )
            if not created:
                stock_product.quantity=quantity
                stock_product.price=price
                stock_product.save()

        return stock