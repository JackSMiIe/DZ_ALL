class IntegerSet:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

    def maximum(self):
        return max(self.numbers) if self.numbers else None

    def minimum(self):
        return min(self.numbers) if self.numbers else None


if __name__ == "__main__":
    int_set = IntegerSet([1, 2, 3, 4, 5])
    print(f"Сумма: {int_set.sum()}")
    print(f"Среднеарифметическое: {int_set.average()}")
    print(f"Максимум: {int_set.maximum()}")
    print(f"Минимум: {int_set.minimum()}")
