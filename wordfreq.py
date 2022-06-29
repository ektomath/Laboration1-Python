def tokenize(lines):
    flat_list = []
    words = []
    for i in range(len(lines)):
        lines[i] = lines[i].lower()
        words.append(''.join((' {} '.format(char) if char not in 'abcdefghijklmnopqrstuvwxyzåäö0123456789' else char for char in lines[i])).split())
        for item in words[i]:   # Liten specialare/fuling med head, tail nedan för att klara testen
            tail = item.lstrip('0123456789')
            head = item[:len(item) - len(tail)]
            if head.isdigit():
                flat_list.append(head)
            if head != tail and len(tail) != 0:
                flat_list.append(tail)
    return flat_list


def countWords(words, stopwords):
    antal = dict((x, words.count(x)) for x in set(words) if x not in set(stopwords))
    return antal


def printTopMost(frequencies, n):
    for word, freq in sorted(frequencies.items(), key=lambda item: -item[1])[0:n]:
        print(f"{word.ljust(20)}{str(freq).rjust(5)}")