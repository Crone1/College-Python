def get_counts(words):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for word in words:
        counts[len(word)] += 1
    return counts