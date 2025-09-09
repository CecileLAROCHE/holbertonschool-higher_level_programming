#!/usr/bin/python3

def multiple_returns(sentence):

    lenght = len(sentence)
    if lenght == 0:
        return (0, None)
    else:
        return (lenght, sentence[0])
