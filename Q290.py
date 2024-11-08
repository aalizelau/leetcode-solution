def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False  # Length mismatch, so no bijection is possible

    # Create two dictionaries to map pattern -> word and word -> pattern
    pattern_to_word = {}
    word_to_pattern = {}

    for p, w in zip(pattern, words):
        # Check if the pattern letter is already mapped to a word
        if p in pattern_to_word:
            if pattern_to_word[p] != w:
                return False  # Mismatch in mapping
        else:
            pattern_to_word[p] = w

        # Check if the word is already mapped to a pattern letter
        if w in word_to_pattern:
            if word_to_pattern[w] != p:
                return False  # Mismatch in mapping
        else:
            word_to_pattern[w] = p

    return True