def analyze_strings(words):
    upperCase = []
    longWords = []
    starts_with_vowel = []
    length = []
    lambda_concat = []
    iterator_two_items = []
    vowels = ["a", "i", "u", "e", "o"]
    for word in words:
        upp = word.upper()
        upperCase.append(upp)
        length_word = len(word)
        if length_word > 5:
            longWords.append(word)
        length.append(length_word)
        if word[0].lower() in vowels:
            starts_with_vowel.append(word)
    return {
        "uppercase": upperCase,
        "long_words": longWords,
        "start_with_vowel": starts_with_vowel
    }

words = ["Hello", "world", "Python", "is", "great", "AI", "OpenAI"]
print(analyze_strings(words))