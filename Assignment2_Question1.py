#opens the files and splits it into words
file = open(file="sample-file.txt", mode="r")
words = file.read().lower().split()

cleaned = []

#strips punctuation and makes sure the word has atleast 2 characters
for word in words:
    word = word.strip(".,!?;:'\"()[]{}<>")

    if sum(c.isalpha() for c in word) >= 2:
        cleaned.append(word)

counts = {}

#gets the count for words
for word in cleaned:
    counts[word] = counts.get(word, 0) + 1

#gets the top 10 frequencies of words
top_10 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

#prints the word with frequence
for word, frequency in top_10:
    print(f"{word} -> {frequency}")

#closes the file
file.close()
