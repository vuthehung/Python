def minion_game(s):
    vowels = "AEIOU" #nguyen am
    str_length = len(s)
    kevin_score, stuart_score = 0, 0
    for i in range(str_length):
        if s[i] in vowels:
            kevin_score += (str_length - i)
        else:
            stuart_score += (str_length - i)
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)