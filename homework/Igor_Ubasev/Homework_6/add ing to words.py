word = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel." \
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = word.split()
modified_words = []
for word in words:
    if word.endswith(','):
        clean_word = word[:-1]  # слово без запятой
        modified_word = clean_word + 'ing' + ','
    elif word.endswith('.'):
        clean_word = word[:-1]  # слово без точки
        modified_word = clean_word + 'ing' + '.'
    else:
        modified_word = word + 'ing'
    modified_words.append(modified_word)
result = ' '.join(modified_words)
print(result)
