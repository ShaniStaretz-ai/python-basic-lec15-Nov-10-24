# python-basic-lec15-Nov-10-24

## subjects learned:
* functions- continue:
  * how to write documentation: after """""", click on 'enter' in the middle, if the function receive parameter, the ide will add automatically:
  for example:
    ```
    def my_headline(str1: str="") -> str:
      """
      :param str1: 
      :return: 
      """
      ....
    ```
  * Scopes
  * global parameters - it is not recommended to use it at all. but if used and need to change it, send it to the function as a parameter and return it back, updated.
  * lambda functions - part of annonimus functions subject a way to short it to smaller function:
    * must be 1 line
    * must return something
    * examples:
      ```
      def is_negative(number: int) -> bool:
        return number < 0
      is_negative_lambda=lambda  number:number<0
      is_negative_lambda=lambda  number:True if number<0 else False
      print(is_negative_lambda(-5)) # same as print(is_negative(-5))
      ```
      
    * filter functions- (like in js) :a function that receive a lambda function and a list and return a filtered list by the condition in the lambda function
      ```
      l_str1 = ["apple", "Anaconda", "banana", "pineapple", "coconut", "Am-Pm"]
      l6 = list(filter(lambda word: len(word) > 6, l_str1))
      ```
    * map function:( like in js)- a way to create a new value for each item in the received list and returns a new list with the new values.
      ```
       l1 = [-4, 0, 2, -1, 3, 9]
      l_same=list(map(lambda x:x,l1))
      ```
      
## extra subjects:
