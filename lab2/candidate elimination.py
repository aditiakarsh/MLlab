import numpy as np 
import pandas as pd

d = pd.read_csv("data.csv")
att = np.array(d)[:,:-1]
print("\nInstances are:\n",att)
tar = np.array(d)[:,-1]
print("\nTarget Values are: ",tar)
def candi(att, tar): 
    sh= att[0].copy()
   
    print("\nSpecific Boundary: ",sh)
    gh = [["?" for i in range(len(sh))] for i in range(len(sh))]
    print("\nGeneric Boundary: ",gh)  

    for i, h in enumerate(att):
        print(i+1 , "is ", h)
        if tar[i] == "yes":
            print("=Positive ")
            for x in range(len(sh)): 
                if h[x]!= sh[x]:                    
                    sh[x] ='?'                     
                    gh[x][x] ='?'
                   
        if tar[i] == "no":            
            print("= Negative ")
            for x in range(len(sh)): 
                if h[x]!= sh[x]:                    
                    gh[x][x] = sh[x]                
                else:                    
                    gh[x][x] = '?'        
        
        print("Specific Boundary after ", i+1, " is ", sh)         
        print("Generic Boundary after ", i+1, "is ", gh)
        print("\n")

    indices = [i for i, val in enumerate(gh) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:   
        gh.remove(['?', '?', '?', '?', '?', '?']) 
    return sh, gh 
print(candi(att,tar))
