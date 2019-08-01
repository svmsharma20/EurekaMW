"""import requests

from com.eurekamw.model import SearchConstants

searchURL = SearchConstants.URL+"abate"+SearchConstants.KEY_DICTIONARY_1
print(searchURL)

resp = requests.get(searchURL)

print(resp.json())"""

from com.eurekamw.utils.WordUtils import generate_list


# Get the words from the user as a string
words = input("Enter the list of words(comma separated)")
wordList = generate_list(words)

for word in wordList:
    print(word)