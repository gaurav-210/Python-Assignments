# **GIT & GITHUB COMMANDS..**

* **Designed By - [Gaurav Chauhan](https://github.com/gaurav-210)**



# What is Git ??
Git is Created by **_Linus Trovaldus_**.(responsible for the linux kernel.)
Git is a version control system (VCS). Git is a tool/software like your IDE or VLC player. It is not a programming language.It is a general tool.Chances For Hiring In a Company will be increased When u Mentioned Git ON ur Resumes.

# What Git Does ??
There are two main Reasons to Learn GIT.
1. Track changes to your code .
2. Save your code to the cloud .

# What is GitHub ??
Github is not the same as git. Github is a website/platform while git is a tool.
For Ex:- Git or Camera is just the tool, But Instagram or GitHub is the website.
**Github allows you to safely store your code in the cloud. And Also U can Share Your Code With Others.** Other websites such as gitlab, bitbucket which are similar to Github also exists . **Companies love it when you have a github profile and they can see your work before even calling you for an interview.**
* Now the Question Arises We Can do the same from Google Drive or DropBox, But the Solution is It Is Designed for special purpose(It even Track the record of code that u wrote 5 years ago. And what is it.)


# A quick Revision of the used commands.
* `git init` - Create an empty git repository
* `git add .` - Add all files to the next commit/version
* `git status` - Gives the status for thr files which are tracked,untracked and modified.
* `git commit -m "Your meaningful message here"` - Create a commit/version of the proejct
* `git log` - See commit/version history of the project
* `git remote add origin 'Paste your link for remote repo here'` to add the link btw remote repo and local repo.
* `git push origin master` - To push your code ,your project project file to Remote repo from local repo.






















<!-- ---------------------------------------------------------------------------------------------- -->
dubey ji ki assignment on pending mode 
# **Problems Related to Lists in Python **   [.](https://www.tutorialspoint.com/python/python_interview_questions.htm)
* Designed by [Gaurav Chauhan](https://github.com/gaurav-210)

## Dear Students, these `Python Programming Language Interview Questions` have been designed _specially for u_ to get you acquainted with the nature of questions you may encounter during your interview for the subject of Python Programming Language.

* `Note:-` **_The Following Questions Covers the concepts which are discussed in class. You all students have to submit it as a assignment for ur practice._**


# What is Python?
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.

 
# Name some of the features of Python.

*A variety of basic data types are available: numbers (floating point, complex, and unlimited-length long integers), strings (both ASCII and Unicode), lists, and dictionaries.

*Python supports object-oriented programming with classes and multiple inheritance.
Code can be grouped into modules and packages.

*The language supports raising and catching exceptions, resulting in cleaner error handling.
Data types are strongly and dynamically typed. Mixing incompatible types (e.g. attempting to add a string and a number) causes an exception to be raised, so errors are caught sooner.

*Python contains advanced programming features such as generators and list comprehensions.

*Python's automatic memory management frees you from having to manually allocate and free memory in your code.


# What is the purpose of PYTHONPATH environment variable?
It has a role similar to PATH. This variable tells the Python interpreter where to locate the module files imported into a program. It should include the Python source library directory and the directories containing Python source code. PYTHONPATH is sometimes preset by the Python installer.


# Is python a case sensitive language?
Yes, Like most of the widely used programming languages like Java, C, C++, etc, Python is also a case sensitive language.

Languages like Pascal, Basic, Fortran, SQL, Lisp, etc are case in-sensitive.



# What are the supported data types in Python?
The modules described in this chapter provide a variety of specialized data types such as dates and times, fixed-type arrays, heap queues, synchronized queues, and sets.

Python also provides some built-in data types, in particular, dict, list, set and frozenset, and tuple. The str class is used to hold Unicode strings, and the bytes class is used to hold binary data.


# What is the output of print str if str = 'Hello World!'?
Hello World!

# What is the output of print str[0] if str = 'Hello World!'?
str ='Hello world!'
print(str[0])
output :- H

# What is the output of print str[2:5] if str = 'Hello World!'?
str ='Hello world!'
print(str[2:5])
output :- llo


# What is the output of print str[2:] if str = 'Hello World!'?
str ='Hello world!'
print(str[2:])
output :- llo world!

# What is the output of print str * 2 if str = 'Hello World!'?
str ='Hello world!'
print(str*2)
output :- Hello world!Hello world!

# What is the output of print str + "TEST" if str = 'Hello World!'?
str ='Hello world!'
print(str+"Test")
output :- Hello world!Test

# What is the output of print list if list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]?
It will print concatenated lists. Output would be [ 'abcd', 786 , 2.23, 'john', 70.2 ].

# What is the output of print list[0] if list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]?
It will print first element of the list. Output would be abcd.

# What is the output of print list[1:3] if list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]?
It will print elements starting from 2nd till 3rd. Output would be [786, 2.23].

# What is the output of print list[2:] if list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]?
It will print elements starting from 3rd element. Output would be [2.23, 'john', 70.200000000000003].

# What is the output of print tinylist * 2 if tinylist = [123, 'john']?
It will print list two times. Output would be [123, 'john', 123, 'john'].


# What is the output of print list + tinylist * 2 if list = [ 'abcd', 786 , 2.23, 'john', 70.2 ] and tinylist = [123, 'john']?
It will print concatenated lists. Output would be ['abcd', 786, 2.23, 'john', 70.2, 123, 'john', 123, 'john'].

# What are tuples in Python?
A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

# What is the difference between tuples and lists in Python?
The main differences between lists and tuples are − Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.

# What is the output of print tuple if tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )?
It will print complete tuple. Output would be ('abcd', 786, 2.23, 'john', 70.200000000000003).

# What is the output of print tuple[0] if tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )?
It will print first element of the tuple. Output would be abcd.

# What is the output of print tuple[1:3] if tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )?
It will print elements starting from 2nd till 3rd. Output would be (786, 2.23).

# What is the output of print tuple[2:] if tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )?
It will print elements starting from 3rd element. Output would be (2.23, 'john', 70.200000000000003).

# What is the output of print tinytuple * 2 if tinytuple = (123, 'john')?
It will print tuple two times. Output would be (123, 'john', 123, 'john').

# What is the output of print tuple + tinytuple if tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 ) and tinytuple = (123, 'john')?
It will print concatenated tuples. Output would be ('abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john').

# What are Python's dictionaries?
Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

# How will you create a dictionary in python?
Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

# How will you get all the keys from the dictionary?
Using dictionary.keys() function, we can get all the keys from the dictionary object.

print dict.keys()   # Prints all the keys

# How will you get all the values from the dictionary?
Using dictionary.values() function, we can get all the values from the dictionary object.

print dict.values()   # Prints all the values

# How will you convert a string to an int in python?
int(x [,base]) − Converts x to an integer. base specifies the base if x is a string.

# How will you convert a string to a long in python?
long(x [,base] ) − Converts x to a long integer. base specifies the base if x is a string.

# How will you convert a string to a float in python?
float(x) − Converts x to a floating-point number.

# How will you convert a object to a string in python?
str(x) − Converts object x to a string representation.

# How will you convert a String to an object in python?
eval(str) − Evaluates a string and returns an object.

# How will you convert a string to a list in python?
list(s) − Converts s to a list.

# How will you convert a string to a set in python?
set(s) − Converts s to a set.

# How will you create a dictionary using tuples in python?
dict(d) − Creates a dictionary. d must be a sequence of (key,value) tuples.

# How will you convert an integer to a character in python?
chr(x) − Converts an integer to a character.

# What is the purpose of ** operator ?
** Exponent − Performs exponential (power) calculation on operators. a**b = 10 to the power 20 if a = 10 and b = 20.

# What is the purpose of // operator?
// Floor Division` − The division of operands where the result is the quotient in which the digits after the decimal point are removed.

# What is the purpose of is operator?
is − Evaluates to true if the variables on either side of the operator point to the same object and false otherwise. x is y, here is results in 1 if id(x) equals id(y).

# What is the purpose of not in operator?
not in − Evaluates to true if it does not finds a variable in the specified sequence and false otherwise. x not in y, here not in results in a 1 if x is not a member of sequence y.

# What is the purpose break statement in python?
break statement − Terminates the loop statement and transfers execution to the statement immediately following the loop.

# What is the purpose continue statement in python?
continue statement − Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.

# What is the purpose pass statement in python?
pass statement − The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

# How will you capitalizes first letter of string?
capitalize() − Capitalizes first letter of string.

# How will you check in a string that all characters are alphanumeric?
isalnum() − Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

# How will you check in a string that all characters are digits?
isdigit() − Returns true if string contains only digits and false otherwise.

# How will you check in a string that all characters are in lowercase?
islower() − Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.

# How will you check in a string that all characters are numerics?
isnumeric() − Returns true if a unicode string contains only numeric characters and false otherwise.

# How will you check in a string that all characters are whitespaces?
isspace() − Returns true if string contains only whitespace characters and false otherwise.

# How will you check in a string that it is properly titlecased?
istitle() − Returns true if string is properly "titlecased" and false otherwise

# How will you check in a string that all characters are in uppercase?
isupper() − Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

* ### How will you get the length of the string?

* ### How will you convert a string to all lowercase?

* ### How will you remove all leading whitespace in string?

* ### How will you get the max alphabetical character from the string?

* ### How will you get the min alphabetical character from the string?

* ### How will you change case for all letters in string?

* ### How will you convert a string to all uppercase?

* ### What is the difference between del() and remove() methods of list?

* ### What is the output of len([1, 2, 3])?

* ### What is the output of [1, 2, 3] + [4, 5, 6]?

* ### What is the output of ['Hi!'] * 4?

* ### What is the output of 3 in [1, 2, 3]?

* ### What is the output of for x in [1, 2, 3]: print x?

* ### What is the output of L[2] if L = [1,2,3]?

* ### What is the output of L[-2] if L = [1,2,3]?

* ### What is the output of L[1:] if L = [1,2,3]?

* ### How will you compare two lists?

* ### How will you get the length of a list?

* ### How will you get the max valued item of a list?

* ### How will you get the min valued item of a list?

* ### How will you get the index of an object in a list?

* ### How will you insert an object at given index in a list?

* ### How will you remove last object from a list?

* ### How will you remove an object from a list?

* ### How will you reverse a list?

* ### How will you sort a list?
