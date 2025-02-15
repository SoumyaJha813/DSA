class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n==0:
                return True
            #first plot is empty and can be filled
            if flowerbed[i]==0 and i==0 and i == len(flowerbed)-1:
                flowerbed[i]=1
                n-=1
                #print("flowerbed: ", flowerbed)
                #print("n: ", n)
            elif flowerbed[i]==0 and i==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
                #print("flowerbed: ", flowerbed)
                #print("n: ", n)
            # in between plots are empty
            elif flowerbed[i]==0 and i>0 and i<len(flowerbed)-1:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
                    #print("flowerbed: ", flowerbed)
                    #print("n: ", n)
            #end plot is empty
            elif flowerbed[i]==0 and i==len(flowerbed)-1 and flowerbed[i-1]==0:
                flowerbed[i]=1
                n-=1
                #print("flowerbed: ", flowerbed)
                #print("n: ", n)
        if n==0:
            return True
        if n!=0:
            return False
            
