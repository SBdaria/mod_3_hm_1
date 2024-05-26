def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower().find(i.lower()) != -1 or i.lower().find(root_word.lower()) != -1:
            same_words.append(i)
    print(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')