file = open(file="sample-file.txt", mode="r")
lines=file.readlines()

groups = {}

for i in range(len(lines)):
    original = lines[i].strip()

    #lowercase + remove whitespace & punctuation
    key = "".join(c for c in original.lower() if c.isalnum())

    if key != "":
        groups.setdefault(key, []).append((i + 1, original))

#keep only duplicate sets
duplicates = [g for g in groups.values() if len(g) > 1]

print("Number of near-duplicate sets:", len(duplicates))

for i in range(min(2, len(duplicates))):
    print("\nSet", i + 1)
    for line_num, text in duplicates[i]:
        print(f"{line_num}: {text}")