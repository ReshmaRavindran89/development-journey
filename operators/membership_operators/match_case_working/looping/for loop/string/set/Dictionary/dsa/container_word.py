# company interview Question to find container word:-

# method 1:- 

source ="traviduxtechnology"

target = "vridautx"

class ContainerWord:

    def solution(self,source:str,target:str):

        present = True

        for ch in target:

            if ch not in source:

                present = False

                break


        return present
    
ContainerWord_instance = ContainerWord()

print(ContainerWord_instance.solution("traviduxtechnology","vridautx"))



# method 2 :- *******(using subset)*******

source ="traviduxtechnology"

target = "vridautx"

class ContainerWord:

    def solution(self,source:str,target:str):

        present = True

        present = set(target).issubset(set(source))

        
        return present
    
ContainerWord_instance = ContainerWord()

print(ContainerWord_instance.solution("traviduxtechnology","vridautx"))