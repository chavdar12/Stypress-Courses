import tempfile
import unittest
from pathlib import Path

from manager import CollectionManager
from storage import TextFileStorage


class MemoryStorage:
    def __init__(self):
        self.saved = []

    def load(self):
        return []

    def save(self, items):
        self.saved = [dict(item) for item in items]


class CollectionManagerTests(unittest.TestCase):
    def setUp(self):
        self.storage = MemoryStorage()
        self.manager = CollectionManager(self.storage)
        self.dune = self.manager.create({"category": "Book", "title": "Dune", "author": "Frank Herbert", "year": "1965"})
        self.manager.create({"category": "Movie", "title": "Dune", "author": "Denis Villeneuve", "year": "2021"})

    def test_create_persists(self):
        self.assertEqual(len(self.storage.saved), 2)

    def test_search_by_text_and_category(self):
        self.assertEqual(len(self.manager.search("dune")), 2)
        self.assertEqual(self.manager.search("dune", "Book"), [self.dune])
        self.assertEqual(len(self.manager.search("2021")), 1)

    def test_update_and_delete(self):
        self.manager.update(self.dune["id"], {**self.dune, "year": "1966"})
        self.assertEqual(self.manager.get(self.dune["id"])["year"], "1966")
        self.manager.delete(self.dune["id"])
        self.assertEqual(len(self.storage.saved), 1)
        with self.assertRaises(KeyError):
            self.manager.get(self.dune["id"])

    def test_validation(self):
        with self.assertRaises(ValueError):
            self.manager.create({"category": "Song", "title": "x"})
        with self.assertRaises(ValueError):
            self.manager.create({"category": "Game", "title": " "})
        with self.assertRaises(ValueError):
            self.manager.create({"category": "Game", "title": "x", "year": "abc"})

    def test_text_file_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "collection.txt"
            CollectionManager(TextFileStorage(path)).create({"category": "Game", "title": "Тетрис"})
            reloaded = CollectionManager(TextFileStorage(path))
            self.assertEqual(reloaded.read()[0]["title"], "Тетрис")
            self.assertEqual(reloaded.create({"category": "Game", "title": "x"})["id"], 2)


if __name__ == "__main__":
    unittest.main()
