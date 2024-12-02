if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_s = sorted(arr)
    #print(arr_s)
    ll = []
    for i in arr_s:
        if i not in ll:
            ll.append(i)
    #print(ll)
    runner = ll[-2]
    print(runner)
