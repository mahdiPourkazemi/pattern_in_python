class BoxIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


class Box:
    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return BoxIterator(self._items)

if __name__=="__main__":
# استفاده از iterator برای پیمایش عناصر در جعبه
    box = Box(["Toy", "Book", "Pen", "Notebook"])
    for item in box:
         print(item)