from functools import partial

def process_word(word: str) -> str:
    normal_vowels, cluster_vowels = 'aeiou', ['yt', 'xr']
    twos_prefix, threes_prefix = ['ch', 'qu', 'th'], ['thr', 'sch']
    pfn = partial(word.startswith)
    ayed = lambda t: t+'ay'

    if any(map(pfn, normal_vowels)) or any(map(pfn, cluster_vowels)):
        return ayed(word)
    elif any(map(pfn, threes_prefix)) or (word[1:].startswith('qu') and
                                        not any(map(pfn, normal_vowels))):
        return ayed(word[3:]+word[:3])
    elif any(map(pfn, twos_prefix)):
        return ayed(word[2:]+word[:2])
    else:
        return ayed(word[1:]+word[:1])

def translate(sentence: str) -> str:
    return ' '.join(process_word(word) for word in sentence.split(' '))
