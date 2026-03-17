
# Factorial:-

class Factorial:

    def solution(self,num):

        fact=1

        for i in range(1,num+1):   

            fact = fact * i

        return fact

Factorial_instance = Factorial()
print(Factorial_instance.solution(4))