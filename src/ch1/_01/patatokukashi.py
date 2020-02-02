word = "パタトクカシーー"


def get_char_from_word(index: int) -> str:
    return word[index]


print(''.join(map(get_char_from_word, [1, 3, 5, 7])))
