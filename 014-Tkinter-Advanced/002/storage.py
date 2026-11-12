import json
from pathlib import Path


class TextFileStorage:
    """Keeps the collection as one JSON object per line in a text file."""

    def __init__(self, path):
        self.path = Path(path)

    def load(self):
        if not self.path.exists():
            return []
        with self.path.open(encoding="utf-8") as file:
            return [json.loads(line) for line in file if line.strip()]

    def save(self, items):
        temp = self.path.with_suffix(".tmp")
        with temp.open("w", encoding="utf-8") as file:
            for item in items:
                file.write(json.dumps(item, ensure_ascii=False) + "\n")
        temp.replace(self.path)  # atomic swap, so a crash mid-write does not lose the collection
