#Striver's A2Z Sheet - DataTypes
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def dataTypeSize(self, str):
        # Code here
        datatypes = {
            'Character': 1,
            'Integer': 4,
            'Long': 8,
            'Float': 4,
            'Double': 8
        }
        
        output = datatypes.get(str, -1)
        return output

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)
# } Driver Code Ends
