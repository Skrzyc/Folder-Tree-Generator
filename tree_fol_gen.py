import os
import math

def run():

    def get_data():
        """ Function returns array contains number of folders in each level """

        def check(st):
            """ Checks if entered data is correct """
           
            for x in range (len(st)):
                try:
                    anything = int(st[x])
                except:
                    print('\n You need to enter a number - try again')
                    get_data()
                    
                try:
                    anything = math.sqrt(int(st[x]))
                except:
                    print('\n Structure should be positive - try again')
                    get_data()
                
            return print('\n Your structure is correct \n')

        st = []
        
        a = input("\n Enter folder structure : ")     # for example : 1_10_2
        st = a.strip().split('_')
        check(st)
        st = [int(x) for x in st] 
        return st


    def get_l_names(st):
        """ Function return array contains name of each level """
        
        names = []
        for x in range(len(st)):
            names.append(input(' Enter a name of ' + str(x+1) + ' level : '))
            if names[x] == '' : names[x] = 'NoName'
        return names        


    def calculations(st):
        """ Function return array containts number of folders in each level,
            the last element is a number of all folders """

        x, summ, product = 0, 0, 1
        sumup = []
        
        while (x < len(st)):
            product = 1
       
            for y in range(x+1):
                product = product * tab_st[y]
                
            summ = summ + product
            sumup.append(product)
            x += 1
            
        sumup.append(summ)
        return sumup


    def get_f_names(tab_names,tab_st,
                    tab_noff,i):
        """ Function return array contains names of all folders wihch will
            be create in order level by level"""

        f_names = []
        cl, j = 0, 0    # cl - current level , j - no. of curent folder

        while(j < tab_noff[-1]):                        
             for x in range(tab_noff[cl]):       
                f_names.append(tab_names[cl])   
                j += 1
             cl += 1
        j = 0

        for x in range(i):                      
            if x == 0:
                for y in range(tab_noff[x]):
                    f_names[j]=f_names[j] + '_' + str(y+1)
                    j += 1
            else :
                w = 0
                for y in range(tab_noff[x]): 
                    if (w == tab_st[x]) : w = 0
                    f_names[j]=f_names[j] + '_' + str(w+1)
                    j += 1
                    w += 1
        return f_names


    def get_paths(tab_names, tab_st, tab_noff):
        """ Return an array contains a relative path to every folder """

        def calc_m(tab_noff,x,j):
            p = 0
            for z in range(x):
                p = p + tab_noff[x-1-z] 
            m = math.ceil((j-p)/tab_st[x])
            p = 0
            for z in range(x-1):
                p = p + tab_noff[x-2-z]
            m = m + p
            return m
        
        rel_path = []
        j = 1                   # current folder
        tab_names.append('')     # needed an extra index
        
        for x in range(len(tab_st)): #level
            if x == 0 :
                for y in range(tab_noff[x]):
                    rel_path.append('')     # the first lvl has no rel path
                    j = j + 1
            else:                               #for another levels
                for y in range(tab_noff[x]):    
                    m = calc_m(tab_noff,x,j)    
                    if x == 1:
                        rel_path.append(tab_names[m-1])
                    else:
                        rel_path.append(rel_path[m-1] + '\\' + tab_names[m-1])
                    j = j + 1
        return rel_path
        

    def create_f(tab_names,
                 tab_rel_paths,
                 tab_noff):
        """ Create Folders """
        a_path = os.getcwd()    #gets absolute path    
        for x in range(tab_noff[-1]):
            if x < tab_noff[0]:
                path =  a_path
            else:
                path = a_path + '\\' + tab_rel_paths[x]
            os.chdir(path)
            os.mkdir(tab_names[x])

        
      
    tab_st = get_data()
  
    tab_names = get_l_names(tab_st)
    
    tab_noff = calculations(tab_st)
    
    tab_names = get_f_names(
        tab_names, tab_st,
        tab_noff, len(tab_st))

    tab_rel_paths = get_paths(
        tab_names, tab_st, tab_noff)

    create_f(tab_names,
             tab_rel_paths,
             tab_noff)    
    

run()


