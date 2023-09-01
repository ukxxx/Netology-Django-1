validated_data = {
  "address": "ленина, 1",
  "positions": [
    {
      "product": 2,
      "quantity": 250,
      "price": 120.50
    },
    {
      "product": 3,
      "quantity": 100,
      "price": 180
    }
  ]
}

for item in validated_data['positions']:
    item['stock'] = validated_data['address']


print(validated_data)