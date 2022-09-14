# Functions

Functions are isolated pieces of code that take input, perform some operation, and return a result. Functions we've used so far include `input()`, `print()`, `len()`, etc. Python provides many built-in functions for you to use. For all the built-in functions, check the [official docs](https://docs.python.org/3/library/functions.html)


- [Defining Functions](#defining-functions)
- [Parameters](#parameters)
  - [Passing by Position](#passing-by-position)
  - [Optional Arguments](#optional-arguments)
  - [Passing by Keyword](#passing-by-keyword)
  - [\*args & \*\*kwargs](#args--kwargs)
- [Returning](#returning)
  - [Implicit Return - None](#implicit-return---none)
  - [Returning Multiple Values](#returning-multiple-values)
- [Decorators](#decorators)
- [Recursion](#recursion)
- [Lambda Functions](#lambda-functions)



## Defining Functions

We can define our own functions using the `def` keyword. This allows us to execute sections of code repeatedly.


```python
def say_hello():
    print('hello!')
say_hello()
say_hello()
say_hello()
```
> hello!
> hello!
> hello!

## Parameters

You can specify parameters by listing variables in the parantheses of the function definition.

```python
def say_hello(first_name, last_name):
    print('Hello ' + first_name + ' ' + last_name)

fn = input('what is your first name? ')
ln = input('what is your last name? ')
say_hello(fn, ln)
```

Notice that the variable names outside the function don't have to match the variable names inside the function. When the values are passed as parameters, they take on new names, local only to the function.

### Passing by Position

Thus far, we’ve been passing arguments to functions **by position.** The values at the call site are bound to the variables in the function signature _in order._

```python
def subtract(a, b):
  return a - b
subtract(5, 8)  #> -3 (a=5, b=8)
```

### Optional Arguments

Most positional arguments are like the above, **required arguments.** But it’s also possible to have functions that take **optional arguments.** If they are specified when the function is called, then the caller’s value is used. Otherwise, the default value from the function definition is used.

```python
def subtract(a, b=1):
  return a - b
subtract(5)  #> 4 (a=5, b=1)
subtract(5, 8) # -3 (a=5, b=8)
```

### Passing by Keyword

Optional arguments may also be passed **by keyword** _in any order,_ as long as they come after all positional arguments.

```python
def subtract(a, b=1, c=0):
  return a - b - c
subtract(5, b=8) # -3 (a = 5, b = 8, c = 0)
subtract(5, c=9) # -5 (a=5, b=1, c=9)
subtract(5, c=9, b=8) # -12 (a=5, b=8, c=9)
```
### Passing other functions

Functions are first class citizens meaning they can be used anywhere as well as they can be passed as arguments to other functions!

```python

my_numbers = [1,2,3,4]

def double_nums(num):
    return num * 2

def iterate_numbers(my_numbers):
    for x in range(len(my_numbers)):
        print(my_numbers[x])
        my_numbers[x] = double_nums(my_numbers[x]) 

iterate_numbers(my_numbers)
print(my_numbers)

```

### Scope

Scope determines when resources such as variables can be accessed.

```python
statement = "I'd like to learn more about scope"

def print_statement():
    print(statement)


statement()


def another_function():
    statement = "I think scope is confusing"
    another_phrase = "I think that tomorrow will be sunny"
    print(statement)


another_function()
print(statement)
print(another_phrase)
```

If you need to create a global variable, but are stuck in the local scope, you can use the `global` keyword.

The global keyword makes the variable global.


```python

def a_function():
  global y
  y = 300

a_function()
## you'll need to call the function first

print(y)
## then this will work

```

### Closures

A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function’s scope from an inner function.

Requisites for a closure to exist:

- We must have a nested function (function inside a function).
- The nested function must refer to a value defined in the enclosing function.
- The enclosing function must return the nested function.

```python
def outer_function(msg):
    # This is the outer enclosing function

    def inner_function():
        # This is the nested function
        print(msg)

    return inner_function  # returns the nested function


# Now let's try calling this function.
# Output: Hello
my_variable = outer_function("Hello")
my_variable()
```

This is another more curios example:

```python

def adder(x):
    def inner(y):
        return x + y
    return inner


add5 = adder(5)
add10 = adder(10)

print(add5(2));  ## 7
print(add10(2)); ## 12
```

`add5` and `add10` are both closures. They share the same function body definition, but store different lexical environments. In add5's lexical environment, x is 5, while in the lexical environment for add10, x is 10.

### \*args & \*\*kwargs

Both args and kwargs are great for times when you aren't sure in advance what aruments your function will need to take. Args is used when you aren't sure how many arguments there will be; kwargs is a dictionary containing any unspecified keyword arguments to your function. Let's see this in action:

- Args

```python
blog_1 = "I don't like the Beatles"
blog_2 = "i'd like to travel more"
blog_3 = "this is super awesome"
lists = [1,2,3,4,5]
 
def blogs(*args):
    for x in args:
        print(x)
 
blogs(blog_1, blog_2)
```

- Kwargs

```python
def fav_music(**kwargs):
    for arg in kwargs:
        print(arg, kwargs[arg])
 
fav_music(alex = 'pop',  joe= 'rock', jack = 'classic' )
```

- Args and Kwargs

```python
blog_1 = 'first blog'
blog_2 = "second blog"
blog_3 = "third blog"
lists = [1,2,3,4,5]

def blogs(*args, **kwargs):
    for x in args:
        print(x)
    for x in kwargs:
        print(kwargs[x])
 
blogs(blog_1,blog_2, cat='black')
```
_Note: The special thing about these variable names isn’t `args` and `kwargs`. It’s the `*` and `**`. You can name these arguments anything that’s a legal variable name, but by convention they’re named `*args` and `**kwargs`._

You can find more information about both [here](http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/).



## Returning

We can also return values from a function, which is often the result of some computation or operation. The code below returns the lesser of two values. Notice we don't need an `else`, once a the interpreter reaches a `return`, it immediately exits a function.

```python
def min(a, b):
    if a < b:
        return a
    return b
x = min(5, 2)
print(x) # 2
```


### Implicit Return - None

If a function does not return anything, it implicitly returns `None`

```python
def say_hi():
    print('hi')
x = say_hi()
print(x) None
```


### Returning Multiple Values

You can return multiple values using **automatic tuple packing and unpacking**.

```python
def get_dimensions():
    return 500, 200
width, height = get_dimensions()
print(width)
print(height)
```
> 500
> 200



## Recursion

Functions can call other functions, producing a chain of invocation. Functions can even call themselves, this is called **recursion**. It's important to have a 'stop condition', otherwise this results in infinite recursion and you'll get a 'stack overflow'.

```python
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
```

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```

```python
 # this only works on sorted lists
def binary_search_recurse(num, nums, low, high):
    if low >= high:
        return None
    mid = (low + high) // 2
    if nums[mid] == num:
        return mid
    elif nums[mid] < num: # search in the upper half
        return binary_search_recurse(num, nums, mid+1, high)
    else: # search in the lower half
        return binary_search_recurse(num, nums, low, mid+1)

        
def binary_search(num, nums):
    return binary_search_recurse(num, nums, 0, len(nums)-1)
```

## Lambda Functions

Lambda is a reserved keyword that says : what follows is an anonymous function

```python
lambda x:x + 1
"as it is it won't work, so we assign it to a variable:"

g = lambda x:x + 1
print(g(2))
 
my_sum = lambda a, b, c: a + b + c
print(my_sum(1, 2, 3))

cube = lambda x: x**3
numbers = (1, 2, 3, 4)
 
print(list(map(cube, numbers)))
```
