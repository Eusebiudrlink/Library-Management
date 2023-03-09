'''
Created on Dec 15, 2021

@author: Eusebiu
'''

class Sorter():
    def sort(self,list,*,key=lambda x:x,reverse=False):
        pass
    
    
class Insertion_Sort(Sorter):
    
    
    
    def __negatie(self,x):
        return not x
    
    
    def __identitate(self,x):
        return x
    
    
    def insertion_sort(self,list,*,key=lambda x:x, cmp = lambda x,y: x<y, reverse=False):
        if reverse:
            operatie = self.__negatie
        else:
            operatie = self.__identitate
        self.insertion_sort_method(list,key,cmp,operatie)
    
    
        #insertion sort method
    def insertion_sort_method(self,list, key,cmp,operatie):
        
        leng=len(list)
        for i in range(1,leng):
            a=list[i]
            ind=i-1
            while ind>=0 and operatie(cmp( key(a) , key(list[ind]) )):
                list[ind+1]=list[ind]
                ind=ind-1
                
            list[ind+1]=a            
                
        return list 
    

"""def sel_sort(list,key,cmp,operatie):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if operatie(cmp(key(list[i]),key(list[j]))):
                list[i],list[j]=list[j],list[i]"""

        
class Comb_Sort(Sorter):
    
    def __negatie(self,x):
        return not x
    
    
    def __identitate(self,x):
        return x
    
    def CombSort(self,lista,*,key = lambda x:x,cmp= lambda x,y : x<y, reverse = False):
        
        if reverse:
            operatie = self.__negatie
        else:
            operatie = self.__identitate
        
        self.__comb_sort(lista,key,cmp,operatie)
            
    def __comb_sort(self,lista,key,cmp,operatie):
        leng=len(lista)
        shrink=1.3
        _gap=leng
        sorted=False
        while not sorted:
            _gap/=shrink
            gap=int(_gap)
            if gap<=1:
                sorted=True
                gap = 1
            
                for i in range(leng-gap):
                    sm=gap+i
                    if operatie(key(lista[i])>key(lista[sm])):
                        lista[i],lista[sm] = lista[sm], lista[i]
                        sorted = False