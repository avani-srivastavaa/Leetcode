class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        x=[]
        i=1
        while i<=n:
            if i%3==0 and i%5==0:
                x.append('FizzBuzz')
            elif i%3==0:
                x.append('Fizz')
            elif i%5==0:
                x.append('Buzz')
            else:
                x.append(str(i))
            i+=1
        return x
