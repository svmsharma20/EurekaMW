def generate_list(words):

    # Create a list from the input by splitting based on comma and trimming the whitespaces
    wordList = [word.strip().lower() for word in words.split(',')]
    #return the wordlist
    return wordList