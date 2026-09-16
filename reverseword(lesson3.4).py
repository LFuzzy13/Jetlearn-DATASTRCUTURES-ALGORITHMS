def reverse_word(word):

    if word =="":
        return ""
    return reverse_word(word[1:]) + word[0]


print(reverse_word("retpocileh"))