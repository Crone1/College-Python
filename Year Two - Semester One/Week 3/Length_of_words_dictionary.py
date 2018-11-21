def get_counts_dict(words):
    word_count = {}
    for w in words:
        if len(w) in word_count:
            word_count[len(w)] += 1
            
        else:
            word_count[len(w)] = 1
            
    return word_count