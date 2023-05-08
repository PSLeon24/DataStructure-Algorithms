def palindrome(s: str) -> bool:
    que = [] # define queue
    stx = [] # define stack

    # Step 1. insert characters to the queue and stack
    for x in s:
        if x.isalpha():
        # if x == alphabets except for blanks, numbers, exclamation marks
            que.append(x.lower()) # insert to queue, lower()
            stx.append(x.lower()) # insert to stack, lower()

    # Step 2. compare to each characters in queue and stack
    while len(que) > 0 : # if Queue == 0 then break
        if que.pop(0) != stx.pop():
            return False

    return True

if __name__ == '__main__':
    print(palindrome("WoW")) # True
    print(palindrome("Madam, I'm Adam.")) # True
    print(palindrome("Madam, I am Adam.")) # False