def print_rangoli(size):

    #Print Top
    init = []
    fin = []
    full = []
    
    #padding = 4(size)-3
    spacing = (size + (size-1) + (size+size-1-1))
    
    #for every value within total size
    for i in range(size, 0, -1):
        #add alpha to list 
        init.append(chr(96+i))
        
        #create a copy of reversed list
        if i != 0:
            fin = init[-2::-1]
        #and append them
        full = init + fin
        #print each value in full list
        print(("-".join(full)).center(spacing,"-"), end="")
        print()
    
    #Print Bottom
    #For every val starting from the end
    for i in range(size, 1, -1):
        
        #shrink the list by two
        init = init[:-1]
        fin = fin[1:]
        #and combine the them
        full = init+fin
        
        #print each value in full list
        print(("-".join(full)).center(spacing,"-"), end="")
        #continue on next line
        print()
   
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)