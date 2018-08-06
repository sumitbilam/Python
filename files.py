#assuming "rainbow.txt" file exists 

#opening the the "rainbow.txt" file with read only mode
rainbow = open('rainbow.txt', 'r')

#first readlines without using .strip() method
color = rainbow.readline()

while color:
    print(color)
    color = rainbow.readline()

#closing file
rainbow.close()


#now open the file again, this time we will strip "*" and newline ('\n')
rainbow = open('rainbow.txt', 'r')

color = rainbow.readline().strip('*\n')

while color:
    print(color)
    color = rainbow.readline().strip('*\n')

rainbow.close()



