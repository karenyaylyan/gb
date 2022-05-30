from random import choice


def get_jokes(n=1, flag_repeat=True):
    """
    Generate n random jokes

    Keyword arguments:
    n -- number of jokes (default 1)
    flag_repeat -- flag for repeating words in jokes (default True)
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = []

    if flag_repeat:
        for i in range(n):
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    else:
        n = min(n, len(nouns), len(adverbs), len(adjectives))

        for i in range(n):
            noun = choice(nouns)
            adverb = choice(adverbs)
            adjective = choice(adjectives)

            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
            jokes.append(f'{noun} {adverb} {adjective}')

    return jokes
