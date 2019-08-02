
# User related queries
GET_USER = "SELECT * FROM users WHERE username = '{0}'"

INSERT_USER = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"


#  Word related queries
INSERT_WORD = "INSERT INTO words (word, category, stems, shortdef, xdef) VALUES (%s, %s, %s, %s, %s)"
