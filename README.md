# Python Beyond the Basics - OOP

Assignments for [Udemy course](https://www.udemy.com/python-beyond-the-basics-object-oriented-programming).

## Assignment 1

Create a simple class, `MaxSizeList`, that acts a little bit like a list, with a pre-configured limit on its size. Here some test calling code that imports the completed `MaxSizeList` and then uses it to create two new `MaxSizeList` objects.

```
a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())

# ['hi', "let's", 'go']
# ['go']
```

## Assignment 2

Create a very simple inheritance hierarchy of three classes that write to text files.  

- `LogFile(WriteFile)`:  its instance writes a date and message to a log file:  
```
2015-01-21 18:35   this is a log message
```

- `DelimFile (WriteFile)`:  its instance writes values separated by a delimeter:   
```
a,b,c,d
```

- ```WriteFile(object)```:  the parent class to both LogFile and DelimFile, does 1work that is common between them.   Not intended to be instantiated.
