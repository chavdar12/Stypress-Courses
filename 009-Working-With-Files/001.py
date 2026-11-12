import sys


def sort_file(source, destination):
    with open(source, encoding="utf-8") as file:
        lines = file.read().splitlines()
    with open(destination, "w", encoding="utf-8") as file:
        file.write("\n".join(sorted(lines)) + "\n")


if __name__ == "__main__":
    source = sys.argv[1] if len(sys.argv) > 1 else input("Input file: ")
    destination = sys.argv[2] if len(sys.argv) > 2 else "sorted.txt"
    sort_file(source, destination)
    print("Written", destination)
