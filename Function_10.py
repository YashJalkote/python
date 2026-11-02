def count_vowels(string):
    count = 0
    for ch in string:
        if ch.lower() in "aeiou":
            count += 1
    print("Total vowels =", count)

count_vowels("Python Programming")