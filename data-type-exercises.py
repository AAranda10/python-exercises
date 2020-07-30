In [1]: type(99.9)                                                                                               
Out[1]: float

In [2]: type("False")                                                                                            
Out[2]: str

In [3]: type(False)                                                                                              
Out[3]: bool

In [4]: type('0')                                                                                                
Out[4]: str

In [5]: type(0)                                                                                                  
Out[5]: int

In [6]: type(True)                                                                                               
Out[6]: bool

In [7]: type('True')                                                                                             
Out[7]: str

In [8]: type({})                                                                                                 
Out[8]: dict

In [9]: type({'a':[]})                                                                                           
Out[9]: dict

## What data type would best represent:
## - String
## - Boolean
## - Float
## - Boolean
## - Dictionary
## - Float
## - Dictionary
## - Dictionary
## - Dictionary

n [10]: '1' + 2                                                                                                 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-20b2518fe802> in <module>
----> 1 '1' + 2

TypeError: can only concatenate str (not "int") to str

In [11]: 6 % 4                                                                                                   
Out[11]: 2

In [12]: type(6 % 4)                                                                                             
Out[12]: int

In [13]: type(type(6 % 4))                                                                                       
Out[13]: type

In [14]: '3 + 4 is ' + 3 + 4                                                                                     
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-d779031f2239> in <module>
----> 1 '3 + 4 is ' + 3 + 4

TypeError: can only concatenate str (not "int") to str

In [15]: 0 < 0                                                                                                   
Out[15]: False

In [16]: 'False' == False                                                                                        
Out[16]: False

In [17]: True == 'True'                                                                                          
Out[17]: False

In [18]: 5 >= -5                                                                                                 
Out[18]: True

In [19]: !False or False                                                                                         

In [20]: True or "42"                                                                                            
Out[20]: True

In [21]: !True && !False                                                                                         
zsh:1: command not found: !False

In [22]: 6 % 5                                                                                                   
Out[22]: 1

In [23]: 5 < 4 and 1 == 1                                                                                        
Out[23]: False

In [24]: 'codeup' == 'codeup' and 'codeup' == 'Codeup'                                                           
Out[24]: False

In [25]: 4 >= 0 and 1 !== '1'                                                                                    
  File "<ipython-input-25-28fe0c9082c3>", line 1
    4 >= 0 and 1 !== '1'
                   ^
SyntaxError: invalid syntax


In [26]: 6 % 3  == 0                                                                                             
Out[26]: True

In [27]: 5 % 2 != 0                                                                                              
Out[27]: True

In [28]: [1] + 2                                                                                                 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-28-54324b7054ad> in <module>
----> 1 [1] + 2

TypeError: can only concatenate list (not "int") to list

In [29]: [1] + [2]                                                                                               
Out[29]: [1, 2]

In [30]: [1] * 2                                                                                                 
Out[30]: [1, 1]

In [31]: [1] * [2]                                                                                               
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-887f6473eaff> in <module>
----> 1 [1] * [2]

TypeError: can't multiply sequence by non-int of type 'list'

In [32]: [] + [] == []                                                                                           
Out[32]: True

In [33]: {} + {}                                                                                                 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-33-03eea6c7a00d> in <module>
----> 1 {} + {}

TypeError: unsupported operand type(s) for +: 'dict' and 'dict'