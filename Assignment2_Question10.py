def find_lines_containing(filename, keyword):
    results = []
    keyword_lower = keyword.lower()

    with open(filename, "r", encoding="utf-8") as file:
        for i, line in enumerate(file, start=1):
            if keyword_lower in line.lower():
                results.append((i, line.rstrip()))

    return results

matches = find_lines_containing("sample-file.txt", "lorem")

print(f"Number of matching lines: {len(matches)}")

print("First 3 matching lines:")
for line_number, line_text in matches[:3]:
    print(f"{line_number}: {line_text}")