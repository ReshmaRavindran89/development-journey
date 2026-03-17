
# lambda function:-

# defintion :-

# anonymous function with single expression.

# syntax:-

# var_name = lambda p1,p2:expression

# adding numbers:- 

add_number = lambda n1,n2:n1+n2
print(add_number(100,200))

# subtracting numbers:-

sub_number = lambda n1,n2:n1-n2
print(sub_number(100,20))

# finding cube of numbers:-

cube = lambda n:n**3
print(cube(3))

# even number:-

odd_even = lambda num: "even" if num%2==0 else "odd"
print(odd_even(10))

# create a lambda function is_positive return true if number is positive else return false.

is_positive = lambda num:num>0
print(is_positive(10)) 
print(is_positive(-20))




