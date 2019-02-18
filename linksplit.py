'''
Script by SirSnowHorn
Usage is to take a list of links and make them github friendly.
'''

#Past your single line links below and close them with the triple paren/bracket.
items = ["""

"""]

#Now we need to separate this blob up into all the urls.
sep = items[0].split("\n") 

#Get us our alias and the url in proper github format [](). 
#The alias is just a 14 character chop. 
#If you want to be precise, you can filter out http ones and do 7: then https ones and do 8:.

for i in sep:
    print("[{}]({})\n".format(i[7:21], i))
    
#Copy the output into github.
