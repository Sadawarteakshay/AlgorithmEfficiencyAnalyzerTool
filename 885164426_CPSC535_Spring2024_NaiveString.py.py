def naive_string_matcher(text, pattern):

    n = len(text)
    m = len(pattern)
    matches = []

    for s in range(n-m+1):
        if text[s:s+m] == pattern:
            matches.append(s)

    return matches
text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

matches = naive_string_matcher(text, pattern)

if matches:
    print(f"Pattern found at positions: {matches}")
else:
    print(f"Pattern not found in the text.")