class BoxIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def has_next(self):
        return self._index < len(self._items)

    def next(self):
        if self.has_next():
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


class Box:
    def __init__(self, items):
        self._items = items

    def get_iterator(self):
        return BoxIterator(self._items)


# استفاده از iterator برای پیمایش عناصر در جعبه
box = Box(["Toy", "Book", "Pen", "Notebook"])
iterator = box.get_iterator()

while iterator.has_next():
    item = iterator.next()
    print(item)