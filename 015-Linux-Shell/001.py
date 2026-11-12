# The shell exercises (mkdir, touch, mv, cp, rm -r) done with Python's pathlib/shutil.
import shutil
from pathlib import Path


def run(home):
    play = home / "playground"                                  # mkdir ~/playground
    for folder in ("docs", "music", "old/nested"):
        (play / folder).mkdir(parents=True, exist_ok=True)     # mkdir -p
    for file in ("docs/notes.txt", "docs/todo.txt", "music/song.txt", "old/a.txt", "old/nested/b.txt"):
        (play / file).write_text(f"{file}\n")                  # touch / echo > file

    (play / "music").rename(play / "audio")                    # mv music audio
    (play / "docs/todo.txt").rename(play / "docs/tasks.txt")   # mv todo.txt tasks.txt
    shutil.rmtree(play / "old")                                # rm -r old

    shutil.copy(play / "docs/notes.txt", play / "notes_copy.txt")  # from ~: cp playground/docs/notes.txt playground/

    docs = play / "docs"                                       # cd playground/docs
    (docs / "notes.txt").rename(docs / "notes.md")             # rename several files
    (docs / "tasks.txt").rename(docs / "tasks.md")
    (play / "audio/song.txt").rename(docs / "lyrics.txt")      # move and rename in one step
    return sorted(str(p.relative_to(play)) for p in play.rglob("*"))


if __name__ == "__main__":
    for path in run(Path.home()):
        print(path)
