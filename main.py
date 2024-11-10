counter = 10


def inc_counter():
    global counter
    counter += 1


def dec_counter():
    global counter
    counter -= 1


def print_counter():
    print("counter:", counter)


def inc_local_counter():
    counter: int = 20


def is_negative(number: int) -> bool:
    return number < 0


is_negative_lambda = lambda number: number < 0
power_2_lambda = lambda x: x ** 2
is_positive = lambda x: x > 0


def main():
    # inc_counter()
    # inc_counter()
    # inc_counter()
    # dec_counter()
    # dec_counter()
    # print_counter()
    # inc_local_counter()
    # print_counter()
    # print(power_2_lambda(3))
    # for x in [-4,0,2,-1,2,9]:
    # results=[x  for x in [-4,0,2,-1,2,9] if is_positive (x)]
    # print(results)
    # l1=[-4,0,2,-1,3,9]
    # l2=list(filter(lambda x:x!=0,l1))
    # l3 = list(filter(lambda x: x %2==0, l1))
    # l4 = list(filter(lambda x: x %2== 0 and x>0, l1))
    # l5 = list(filter(lambda x: True == 0 and x > 0, l1))#all x in l1
    # print("origin:", l1)
    # print("not zero", l2)
    # print("evens", l3)
    # print("evens and positives", l4)
    # l_str1 = ["apple", "Anaconda", "banana", "pineapple", "coconut", "Am-Pm"]
    # l6 = list(filter(lambda word: len(word) > 6, l_str1))
    # l7 = list(filter(lambda word: '-' in word, l_str1))
    # print("strings with length>6:", l6)
    # print("strings with the char '-' in them:", l7)
    # l1 = [-4, 0, 2, -1, 3, 9]
    # l_inc1= list(map(lambda item:item+1,l1))
    # print(l_inc1)
    l_str=["zzzzz","b","abc","cccc","bb","t"]
    print(list(map(lambda word:len(word),l_str)))
    l2 = [54, 20, 12, 133, 83, 9989]
    print(list(map(lambda num:num%100//10,l2)))
    print(list(map(lambda num:"even" if num%2==0 else "odd",l2 )))

if __name__ == "__main__":
    main()
