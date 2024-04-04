import time

# KMP Algorithm for finding multiple instances
def kmp_search(text, pattern):
    # Function to compute the Longest Prefix Suffix (LPS) array
    def compute_lps_array(pat, lps):
        length = 0
        lps[0] = 0
        i = 1
        while i < len(pat):
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    lps = [0] * len(pattern)
    compute_lps_array(pattern, lps)
    i = j = 0
    occurrences = []
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences

# BMH Algorithm for finding multiple instances
def bmh_search(text, pattern):
    skip = [len(pattern)] * 256
    for k in range(len(pattern) - 1):
        skip[ord(pattern[k])] = len(pattern) - k - 1
    skip = tuple(skip)

    occurrences = []
    i = 0
    while i + len(pattern) <= len(text):
        j = len(pattern) - 1
        k = i + j
        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1
        if j == -1:
            occurrences.append(i)
            i += len(pattern)
        else:
            i += skip[ord(text[i + len(pattern) - 1])]
    return occurrences

def main():
    filepath = input("Please enter the local path to the text file: ")

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print('File not found! Please make sure that you entered a valid file path.')
        return

    pattern = input("Enter the desired pattern to search for: ")

    # KMP Algorithm
    start_time_kmp = time.time()
    kmp_result = kmp_search(text, pattern)
    end_time_kmp = time.time()
    kmp_duration = end_time_kmp - start_time_kmp

    # BMH Algorithm
    start_time_bmh = time.time()
    bmh_result = bmh_search(text, pattern)
    end_time_bmh = time.time()
    bmh_duration = end_time_bmh - start_time_bmh

    print(f"KMP Search Results: {kmp_result}")
    print(f"KMP Execution Time: {kmp_duration} seconds")
    print(f"BMH Search Results: {bmh_result}")
    print(f"BMH Execution Time: {bmh_duration} seconds")

if __name__ == "__main__":
    main()
