def rabin_karp(text, pattern, d, q):
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    result = []

    #Preprocessing: Calculation of hash value for the pattern
    for i  in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s+m] == pattern:
                result.append(s)
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) +  ord(text[s + m])) % q

            if t<0:
                t += q
    
    return result

d = 256
q = 101

#User Input
text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

#Searching for the pattern provided by the user
matches = rabin_karp(text, pattern, d, q)

#display results
if matches:
    print(f"Pattern found at positions:, {matches} ")
else:
    print("Pattern not found")

        
