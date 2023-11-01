from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class AdvertisementSerializer(serializers.ModelSerializer):
    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = (
            "id",
            "title",
            "description",
            "creator",
            "status",
            "created_at",
        )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        status = data.get("status")
        creator = self.context["request"].user

        if (
            status == AdvertisementStatusChoices.OPEN
            or self.context["request"].method == "POST"
        ):
            open_advertisements_counter = Advertisement.objects.filter(
                creator=creator, status=AdvertisementStatusChoices.OPEN
            ).count()
            print(open_advertisements_counter)
            if open_advertisements_counter >= 10:
                raise serializers.ValidationError(
                    "You can't create more than 10 open advertisements"
                )
        return data
