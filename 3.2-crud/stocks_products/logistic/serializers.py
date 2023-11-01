from logistic.models import Product, Stock, StockProduct
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description"]

    def create(self, validated_data):
        return super().create(validated_data)


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ["product", "quantity", "price"]

    def create(self, validated_data):
        return super().create(validated_data)

    def validate(self, data):
        if data["quantity"] <= 0:
            raise ValidationError("Количество должно быть больше нуля")
        return data


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ["id", "address", "positions"]

    def create(self, validated_data):
        positions = validated_data.pop("positions")
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
        return stock

    def validate_positions(self, data):
        if len(data) == 0:
            raise ValidationError("Склад должен содержать хотя бы одну \
                                  единицу товара")
        return data

    def update(self, instance, validated_data):
        positions = validated_data.pop("positions")
        stock = super().update(instance, validated_data)

        for position in positions:
            product = position.get("product")
            quantity = position.get("quantity")
            price = position.get("price")

            stock_product, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=product,
                defaults={"quantity": quantity, "price": price},
            )

        return stock
