from random import randint
from statistics import mean

# 1 filter list of numbers:
numbers: list[int] = [randint(1, 100) for _ in range(50)]
print("origin:", numbers)
# a:
print("bigger than 50:", list(filter(lambda number: number > 50, numbers)))
print("dividable by 7:", list(filter(lambda number: number % 7 == 0, numbers)))
print("2 digits", list(filter(lambda number: 9 < number < 100, numbers)))
print("equal digits:", list(filter(lambda number: 9 < number < 100 and number % 10 == number // 10, numbers)))
print("sum digits equal to 9: ",
      list(filter(lambda number: number == 9 or number > 10 and number % 10 == number // 10, numbers)))
avg = mean(numbers)  # too spare calculate the avg every number
print("avg:", avg)
print("bigger than avg:", list(filter(lambda number: number > avg, numbers)))

print(
    f"bigger than half of the max value {max(numbers) / 2} :"
    f"{list(filter(lambda number: number > max(numbers) / 2, numbers))}")
# with calculate max on every number
print()
# 2. filter list of strings:
games: list[str] = ["Fortnite", "V Auto Theft Grand ", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
print("games:", games)
print("games with length bigger than 8 letters:", list(filter(lambda word: len(word) > 8, games)))
print("games starts with 'F':", list(filter(lambda word: word.upper().startswith('F'), games)))
print("games with 2 words exactly:", list(filter(lambda words: len(words.split(' ')) == 2, games)))
print("games contains the letter 'V':", list(filter(lambda word: 'V' in word.upper(), games)))
print()
# 3 map list of numbers:
numbers: list[int] = [randint(-50, 50) for _ in range(20)]
print("origin:", numbers)
print("power 3:", list(map(lambda number: number ** 3, numbers)))
print("first digit from the right:", list(map(lambda number: number if -1 < number < 10 else number % 10, numbers)))
print("to Fahrenheit:", list(map(lambda number: number * 1.8 + 32, numbers)))
print("positive/negative:", list(map(lambda num: "positive" if num > 0 else "negative", numbers)))
print()
# 4 map list of strings:
fruits = ["Strawberry", "Pineapple", "Grapes", "Watermelon", "Mango ", "Orange ", "Banana ", "Apple "]
print("origin fruits:", fruits)
print("fruit in reverse:", list(map(lambda fruit: fruit[::-1], fruits)))
print("first letter in fruit:", list(map(lambda fruit: fruit[0], fruits)))
print("fruit in capital letters:", list(map(lambda fruit: fruit.upper(), fruits)))
print("middle letter in fruit:", list(map(lambda fruit: fruit[len(fruit) // 2], fruits)))
print("fruit ends with 's':", list(map(lambda word: word + '!' if word.lower().endswith('s') else word, fruits)))

# 5 the word global, means that ONLY with this word the global constant parameter can be changed,
# without it the parameter is read only
# The disadvantage of this word, that you cannot know if the parameter is exist,
# and which functions changed it or got its value only,
# the code will fail, because you cannot change the value of a global parameter without the word 'global'.
