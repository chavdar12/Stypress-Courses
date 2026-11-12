CATEGORIES = ("Movie", "Game", "Book")
FIELDS = ("category", "title", "author", "year")


class CollectionManager:
    """CRUD + search over the collection. Knows nothing about the GUI;
    any object with load() and save(items) works as storage."""

    def __init__(self, storage):
        self.storage = storage
        self.items = storage.load()
        self.next_id = max((item["id"] for item in self.items), default=0) + 1

    @staticmethod
    def validate(data):
        if data.get("category") not in CATEGORIES:
            raise ValueError(f"Category must be one of {', '.join(CATEGORIES)}")
        if not str(data.get("title", "")).strip():
            raise ValueError("Title is required")
        year = str(data.get("year", "")).strip()
        if year and not year.isdigit():
            raise ValueError("Year must be a number")
        return {field: str(data.get(field, "")).strip() for field in FIELDS}

    def create(self, data):
        item = {"id": self.next_id, **self.validate(data)}
        self.next_id += 1
        self.items.append(item)
        self.storage.save(self.items)
        return item

    def read(self, category=None):
        return [item for item in self.items if category in (None, item["category"])]

    def get(self, item_id):
        for item in self.items:
            if item["id"] == item_id:
                return item
        raise KeyError(f"No item with id {item_id}")

    def update(self, item_id, data):
        item = self.get(item_id)
        item.update(self.validate(data))
        self.storage.save(self.items)
        return item

    def delete(self, item_id):
        self.items.remove(self.get(item_id))
        self.storage.save(self.items)

    def search(self, text, category=None):
        text = text.lower()
        return [item for item in self.read(category)
                if any(text in item[field].lower() for field in ("title", "author", "year"))]
