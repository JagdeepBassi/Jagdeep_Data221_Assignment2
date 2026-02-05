#opens the file and splits the words up
file = open(file="sample-file.txt", mode="r")
words = file.read().lower().split()

cleaned = []

#strips punctuation and makes sure there is atleast 2 characters
for word in words:
    word = word.strip(".,!?;:'\"()[]{}<>")

    if sum(c.isalpha() for c in word) >= 2:
        cleaned.append(word)

bigrams = []

#turns the words into the bigrams
for i in range(len(cleaned) - 1):
    bigrams.append(cleaned[i] + " " + cleaned[i + 1])

counts = {}

for bigram in bigrams:
    counts[bigram] = counts.get(bigram, 0) + 1

#gets the top 5 bigrams
top_5 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]

#prints the bigram and frequency
for bigram, frequency in top_5:
    print(f"{bigram} -> {frequency}")

#closes the file
file.close()