# view question at the bottom
# soloLang discord server compiler-theory task4 active prep by wittyBit

"""
date : day.month, day.month.year

<digit>.<digit>  <digit>.<digit>.<digit>

url : http, ftp, .., page, 

http<char*1>://<chars>.<chars>

"""
import re

BEG_TAG = "<active>"
END_TAG = "</active>"

link="link"
date="date"
nonTarget = "non-target"
glob_tokens = []

def token(a,b): #named tuple better here or token from std lib current used for simplicity
    return (a,b)

def tokenise(text):
    global glob_tokens
    global link
    global date
    global nonTarget
    
    words = text.split()
    for word in words:
        dates = word.split(".")
        try:
            dates= [ int(x) for x in dates ]
        except:
            pass
        if("://" in word or re.search(r'\w+\.\w+$', word) or re.search(r'\w+\.\w+/\w+', word)):
            glob_tokens.append(token(link,word)) 
        elif(all(isinstance(item, int) for item in dates)==True):
            glob_tokens.append(token(date,word))
        else:
            glob_tokens.append(token(nonTarget,word))
            
def parse():
    global glob_tokens
    global link
    global date
    global nonTarget
    global BEG_TAG
    global END_TAG
    
    for token in glob_tokens:
        id=token[0]
        content=token[1]
        if (id==date or id==link):
            print(BEG_TAG,content,END_TAG, end=" ", sep="")
        else:
            print(content, end=" ")
            
    glob_tokens=[] #on pc, freeing up for next input
        

#while True: on pc + add indents for below
source = input("\n> ") #meet me at 2.2.2 etc
tokenise(source)
parse()
    



    #Today @appinv started making his own chat system and he wants users to see highlighted active text(with wich users can interact), but he doesn't knows how to do it.
    #Your task is to write a parser wich surrounds dates and urls with <active> tag:
    
    #Let's meet at <active>20.08</active>
    
    #Dates may be in the following formats:
    
    #day.month
    #day.month.year
    
    #urls may include connection type(http, ftp, ...), domain, page
    #Examples(not full list)
    #ftp://site.domain
    #site.com
    #site.domain/page
    #...
    #(edited)
    #@everyone should make the script we can run and post it as file in #exercises-submissions
    #August 11, 2017
    #WittyBit - Today at 8:39 AM
    #Input is provided as text in the standard stream. Use:
    #Console.ReadLine() in C#
    #input() in Python
    #prompt window in browser JS
    
    
    #Output should be written in standart output stream:
    #Console.Write... in C#
    #print() in Python
    #console.log() in JS
    #System.out.ptintln() in Java
    ##...
