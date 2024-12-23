import json


def calculate_sum_of_products(json_data):
    total_sum = 0.0

    for item in json_data:
        # Умножаем значения score и weight и добавляем к общей сумме
        total_sum += item['score'] * item['weight']

    # Возвращаем округленное значение до 3 знаков после запятой
    return round(total_sum, 3)


# Пример данных в формате JSON
data = [
    {
        "score": 0.0009456152645028281,
        "weight": 1
    },
    {
        "score": 0.00020640167757499364,
        "weight": 1
    },
    {
        "score": 0,
        "weight": 1
    },
    {
        "score": 1.6557065217391307,
        "weight": 1
    },
    {
        "score": 0,
        "weight": 1
    },
    {
        "score": 0.6066065217391303,
        "weight": 1
    },
    {
        "score": 0.03126181644071977,
        "weight": 1
    },
    {
        "score": 0.001253973281817707,
        "weight": 1
    }
]

# Вызываем функцию и печатаем результат
result = calculate_sum_of_products(data)
print(result)

