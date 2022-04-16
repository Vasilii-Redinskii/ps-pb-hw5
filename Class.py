class LogRow:
    def __init__(self, row_id, client, item, amount):
        self.row_id = row_id
        self.client = client
        self.item = item
        self.amount = amount
    
    def __str__(self):
      return f'{self.row_id}'


class LogManager:
    def __init__(self, objects=None):
        self.objects = objects if objects else []
    
    def objects_count (self):
        objects_list=self.objects
        return len(objects_list)

    def total_amount (self):
        amount = 0
        for object_list in self.objects:
            amount += object_list.amount
        return amount

row1 = LogRow(1, 'Иванов Иван', 'iPhone', 1000)
row2 = LogRow(2, 'Иванова Мария', 'Бритва gillette fusion', 100)
row3 = LogRow(3, 'Петрова Ольга', 'Билет на Мальдивы', 3990)

log = LogManager([row1, row2, row3])

print('Всего объектов в логе:', log.objects_count())
print('Общая сумма всех покупок:', log.total_amount())