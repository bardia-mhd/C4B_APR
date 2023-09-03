def solution(word):
    if word.isupper():
        return word.lower()
    elif len(word) == 1: 
        return word.upper()
    elif len(word) > 1:
        if str(word[1:]).isupper():
            return str(word[0]).upper() + str(word[1:]).lower() 
        else:
            return word
word = input()
print(solution(word))