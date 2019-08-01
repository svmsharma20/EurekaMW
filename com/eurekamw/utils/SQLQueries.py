
# User related queries
GET_USER = "SELECT * FROM users WHERE username = '%s'"

#  Word related queries
INSERT_WORD = "INSERT INTO words (word, category, stems, shortdef, xdef) VALUES (%s, %s, %s, %s, %s)"