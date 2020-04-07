import re
from collections import Counter


def retrieveMostFrequentlyUsedWords(helpText, wordsToExclude):
    wordsToExclude = [word.lower() for word in wordsToExclude]
    wordsToExclude = set(wordsToExclude)
    regex = r"\b\w+\b"
    words = re.findall(regex, helpText)
    words = [word.lower() for word in words]
    words = [word for word in words if word not in wordsToExclude]
    if len(words) == 0:
        return []
    counter = Counter(words)
    result = counter.most_common()
    n = result[0][1]
    result = [x[0] for x in result if x[1] == n]
    return result
