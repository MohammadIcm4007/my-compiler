# Token Types
TT_INT = "INT"  # TOKEN INTEGER
TT_FLOAT = "FLOAT"  # TOKEN DECIMAL
TT_PLUS = "PLUS"  # TOKEN +
TT_DIV = "DIV"  # TOKEN /
TT_MIN = "MIN"  # TOKEN -
TT_MUL = "MUL"  # TOKEN *
TT_OPEN = "OPEN"  # TOKEN (
TT_CLOSE = "CLOSE"  # TOKEN )


# Number
DIGITS = "0123456789"


# Custom Error
class Error:
    def __init__(self, error_name, detalis, index):
        self.error_name = error_name
        self.detalis = detalis
        self.index = index

    def as_string(self):
        return f"{self.error_name} : [{self.index}] {self.detalis}"


class IllegalCharError(Error):
    def __init__(self, detalis, index):
        super().__init__("IllegalCharError", detalis, index)


class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        if self.value == None:
            return f"{self.token_type}"
        return f"{self.token_type}:{self.value}"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.index = -1
        self.cursor_char = None
        self.tokens = []
        self.move()

    def move(self):
        self.index += 1
        self.cursor_char = (
            self.text[self.index] if self.index < len(self.text) else None
        )

    def make_tokens(self):

        while not self.cursor_char == None:
            if self.cursor_char in " \t":
                self.move()
            elif self.cursor_char in DIGITS:
                self.make_number()
            elif self.cursor_char == "(":
                self.tokens.append(Token(TT_OPEN))
                self.move()
            elif self.cursor_char == ")":
                self.tokens.append(Token(TT_CLOSE))
                self.move()
            elif self.cursor_char == "+":
                self.tokens.append(Token(TT_PLUS))
                self.move()
            elif self.cursor_char == "-":
                self.tokens.append(Token(TT_MIN))
                self.move()
            elif self.cursor_char == "*":
                self.tokens.append(Token(TT_MUL))
                self.move()
            elif self.cursor_char == "/":
                self.tokens.append(Token(TT_DIV))
                self.move()
            else:
                print(
                    IllegalCharError(
                        f"'{self.cursor_char}' is not defined", self.index
                    ).as_string()
                )
                self.move()
        return self.tokens

    def make_number(self):
        number_of_dot = 0
        number = ""
        while self.cursor_char != None and self.cursor_char in DIGITS + ".":
            if self.cursor_char == ".":
                number_of_dot += 1
                number += self.cursor_char
                self.move()
            elif self.cursor_char in DIGITS:
                number += self.cursor_char
                self.move()
        if number_of_dot == 1:
            self.tokens.append(Token(TT_FLOAT, float(number)))
        elif number_of_dot == 0:
            self.tokens.append(Token(TT_INT, int(number)))


def run(text):
    lexer = Lexer(text)
    tokens = lexer.make_tokens()
    return tokens
