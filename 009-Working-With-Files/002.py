import re
import sys


def analyze(text):
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    words, bigrams = [], []
    for sentence in sentences:
        sentence_words = re.findall(r"\w+(?:['-]\w+)*", sentence.lower())
        words += [w for w in sentence_words if w not in words]
        bigrams += [f"{a} {b}" for a, b in zip(sentence_words, sentence_words[1:])]
    return words, sentences, bigrams


words, sentences, bigrams = analyze("The cat sat. The cat ran away!")
assert words == ["the", "cat", "sat", "ran", "away"]
assert sentences == ["The cat sat.", "The cat ran away!"]
assert bigrams == ["the cat", "cat sat", "the cat", "cat ran", "ran away"]  # no "sat the": crosses sentences

if __name__ == "__main__":
    source = sys.argv[1] if len(sys.argv) > 1 else input("Input file: ")
    with open(source, encoding="utf-8") as file:
        results = analyze(file.read())
    for name, lines in zip(("words.txt", "sentences.txt", "bigrams.txt"), results):
        with open(name, "w", encoding="utf-8") as file:
            file.write("\n".join(lines) + "\n")
        print("Written", name)
