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

### Movie Rental Scenario
In [35]: Mermaid = 3                                                                                                   

In [36]: Bear = 5                                                                                                   

In [37]: Hercules = 1                                                                                                   

In [38]: Days = 3                                                                                                   

In [39]: (Mermaid * Days) + (Bear * Days) + (Hercules * Days)                                                                             
Out[39]: 27

## Company Scenario
In [40]: Google = 400                                                                                                 

In [41]: Amazon = 380                                                                                                 

In [42]: Facebook = 350                                                                                                 

In [43]: FB_Hours = 10                                                                                                  

In [44]: G_Hours = 6                                                                                                   

In [45]: A_Hours = 4                                                                                                   

In [46]: (Facebook * FB_Hours) + (Google * G_Hours) + (Amazon * A_Hours)                                                                             
Out[46]: 7420

###Class enrollment scenario

In [47]: class_not_full = True                                                                                   

In [48]: no_schedule_conflict= True                                                                              

In [49]: can_enroll = class_not_full and no_schedule_conflict                                                    

In [50]: print(can_enroll)                                                                                       
True

###Coupon Scenario

In [51]: offer_good = True                                                                                  

In [52]: bought_two_items = True                                                                                 

In [53]: premium_member = False                                                                                  

In [54]: can_apply_offer = bought_two_items and (offer_good or premium_member)                              

In [55]: print(can_apply_offer)                                                                                  
True

## Password Scenario

In [70]: username = 'codeup'                                                                                     

In [71]: password = 'notastrongpassword'                                                                         

In [72]: len(password) > 5                                                                                       
Out[72]: True

In [73]: len(username) < 20                                                                                      
Out[73]: True

In [74]: username != password                                                                                    
Out[74]: True

### Final code for password verification
In [79]: is_valid = (len(password) > 5) and (len(username) < 20) and username != password                        

In [80]: print(is_valid)                                                                                         
True

## Bonus
In [82]: username.strip(' ')                                                                                     
Out[82]: 'codeup'

In [83]: password.strip(' ')                                                                                     
Out[83]: 'notastrongpassword'