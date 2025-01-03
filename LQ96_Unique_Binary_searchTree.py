class Solution:
    def numTrees(self, n: int) -> int:
        uniq_tree = [1]*(n+1)
        print(uniq_tree)
        for node in range(2,n+1):
            total = 0
            for root in range(1,node+1):
                total += uniq_tree[root-1]*uniq_tree[node-root]
            uniq_tree[node]= total
        return uniq_tree[n]
        
