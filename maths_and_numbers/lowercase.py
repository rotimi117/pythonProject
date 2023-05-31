def lowercase_index(word):
    for index, char in enumerate(word):
        if char.islower():
            print(f"Index {index}: '{char}' is a lowercase letter.")


word = "EsTheR"
lowercase_index(word)


