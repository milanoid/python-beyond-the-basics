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

## Assignment 3

In this assignment we're going to leverage the convenience of a dictionary to power a configuration file, which is simply a file of key-value pairs.  

The structure of a config file could take many forms, and one of them is a simple key=value syntax, with one key/value pair per line.  This is simple and straightforward, so we'll use it.  

What's great about using a built-in structure like a dictionary as the interface to the configuration file is that any Python programmer will immediately know how to use it.  The instructions are so simple you almost don't need documentation:  "create a new ConfigDict object, then read and write keys and values as desired" -- that's it

Our config file should looks like this:
```
sql_query=SELECT this FROM that WHERE condition
email_to=me@mydomain.com
num_retries=5
```
