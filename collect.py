def reverse_word(sentence):
    result = []
    word = ""
    for char in sentence:
        if char == " ":
            result.append(word[::-1])
            result.append(" ")
            print(word)
            word = ""
        else:
            word += char
            print(word)
    result.append(word[::-1])
    return "".join(result)
sentence = "Future Focus Academy"
print(reverse_word(sentence))
