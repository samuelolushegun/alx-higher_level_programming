#!/usr/bin/python3
def multiple_returns(sentence):
    taille = len(sentence)
    if taille == 0:
        premier = None
    else:
        premier = sentence[0]
    return (taille, premier)
