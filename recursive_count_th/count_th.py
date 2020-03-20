'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    counter = 0
    # print(word)
    if str(word) == "":
        return counter
    if str(word)[:2] == "th":
        counter+=1
    counter += count_th(str(word)[1:])

    return counter

# print(count_th("th"))
