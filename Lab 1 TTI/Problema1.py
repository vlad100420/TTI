def numara_caractere(text: str) -> dict:
    new_text = text.lower()
    D = {}
    for i in range(len(new_text)):
        count = 0
        for j in range(len(new_text)):
            if new_text[i] == new_text[j]:
                count += 1
        D[new_text[i]] = count
    return D
