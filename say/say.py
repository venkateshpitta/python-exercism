import num2words ## needs pip install num2words
## still debating over this and writing out one all by myself
## Learning libraries vs learning to do things by hand,
## or is it a different question

def say(n: int) -> str:
    if n<0 or n>10**12-1: raise AttributeError
    return num2words.num2words(n, lang='en').replace(',', '')
