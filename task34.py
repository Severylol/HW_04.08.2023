import os
os.system('cls')
def check_rhythm(poem):
    lines = poem.split(" ")
    syllables = []
    
    for line in lines:
        words = line.split("-")
        syllables.append(sum([count_vowels(word) for word in words]))
    
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_vowels(word):
    vowels = "aeiouаеёиоуыэюя"
    count = 0
    
    for char in word:
        if char.lower() in vowels:
            count += 1
    
    return count

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)

print(result)
