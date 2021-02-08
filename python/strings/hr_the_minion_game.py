def minion_game_one(s):
    stuart_count = 0
    kevin_count = 0
    vowels = ['a', 'e', 'i','o', 'u'] 
    for x in range(len(s)):
        if s[x].lower() in vowels:
            kevin_count += (len(s) - x)
        else:
            stuart_count += (len(s) - x)

    if kevin_count > stuart_count: 
        print("Kevin " + str(kevin_count))
    elif stuart_count > kevin_count:
        print("Stuart " + str(stuart_count))
    else:
        print("Draw")

# Not good for larger input but this way it allows your to output variants
def minion_game_two(s):
    vowels = ['a', 'e', 'i','o', 'u'] 
    mix_words = []
    for x in range(1,len(s) + 1):
        for y in range(0,len(s) + 1):
            if (y + x) <= len(s):
                mix_words.append(s[y:y + x])
    
    kevin_count = 0
    stuart_count = 0
  
    vowels = ['a', 'e', 'i','o', 'u'] 

    for x in mix_words:
        if x[0].lower() in vowels:
            kevin_count += 1
        else:
            stuart_count += 1
    
    if stuart_count > kevin_count:
        print("Stuart " + str(stuart_count))
    elif kevin_count > stuart_count:
        print("Kevin " + str(kevin_count))
    else:
        print("Draw")


s = input()
minion_game_one(s)
minion_game_two(s)
