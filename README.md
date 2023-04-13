# Yoinktxt
Yoinktxt is a *simplified* version of **python-env** for beginners.  
Instead of using .env files, it uses txt files.

## Functions

| **Function**            | **Description**                                                        | **Usage**                                | **Notes**                    |
|-------------------------|------------------------------------------------------------------------|------------------------------------------|------------------------------|
| (class) Yoinktxt        |                                                                        | yk = yktxt.Yoinktxt()                    | Use before anything          |
| data_file(filename)     | Sets the txt file that you want to use                                 | data_file("mydata.txt")                  |                              |
| data_line(lineSplitter) | Sets the character(s) that you want to use to signify the next value   | data_line("\n")                          | Use before "data_spl"!       |
| data_spl(splitter)      | Sets the character(s) that you want to use to split the name and value | data_spl("==")                           |                              |
| yoink_text()            | Returns the exact text in the txt file                                 | yoink_text()                             |                              |
| yoink_list()            | Returns every name and value as 1 object in a list                     | yoink_list()                             |                              |
| yoink_dict()            | Returns dictionary of names and values                                 | yoink_dict()                             |                              |
| yoink(name)             | Gives you the value specified by the name                              | yoink("USERNAME")                        |                              |
| edit_value(name, value) | Edits the value specified by the name                                  | edit_value("USERNAME", "NewUsername123") | Also works to add new values |
| delete_value(name)      | Deletes the value specified by the name                                | delete_value("USERNAME")                 |                              |

## Simple setup file
mydata.txt:
```
_USERNAME==myuser150
_PASSWORD==mypass888
```

Python:
```py
import yktxt

yk = yktxt.Yoinktxt()

myFile = "mydata.txt"
myLine = "\n"
mySpl = "=="

yk.data_file(myFile)
yk.data_line(myLine)
yk.data_spl(mySpl)
```

After this code, the current data stores in the dictionary *(that you can see with yoink_dict())* is:
```
{"_USERNAME": "myuser150", "_PASSWORD": "mypass888"}
```

If we change the `mySpl` variable to `"+"` and `myLine` to `!!`, then the `mydata.txt` file should look like this:
```
_USERNAME+myuser150!!_PASSWORD+mypass888
```
