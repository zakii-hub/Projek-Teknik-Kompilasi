
DIGITS = '0123456789'

##############################
#EROR

class Error:
    def __init__(self, post_start, post_end, error_name, details):
        self.post_start = post_start
        self.post_end = post_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Karakter Ilegal', details)

#########################
#POSITION
#########################

class Position:
    def __init__(self,idx,lr,col,fn,ftxt):
        self.idx=idx
        self.ln=ln
        self.col=col
        self.fn = fn
        self.ftxt=ftxt
    
    def advance (self,current_char):
        self.idx +=1
        self.col +=1

        if current_char =='\n':
            self.ln += 1
            self.col = 0
            
            return self
    
    def copy(self):
        returnPosition(self.idx, self.ln, self.col, self.fn, self.ftxt)

##############################
#TOKEN#######################

TT_INT      = 'TT_INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'

class Token: 
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#############################
#LEXER
#############################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1,0,-1) 
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.ps += 1
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None
    
    def make_tokens(self):
        token = []

        while self.current_char != None:
            if self current_char in '\t':
                self.advnce ()
            elif self.current char in DIGITS:
                token.append(self.make_number())
            elif self.current _char=='+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current _char=='-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current _char=='*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current _char=='\':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current _char=='(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current _char==')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                post_start = self.post.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(post_start, self_pos, "'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if sel.curret char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))
    
###################
#RUN
###############

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer. make _tokens()

    return tokens, error