def indianJob(g, arr):
    totalSum = sum(arr)
    #if the sum // 2 > g it means there is no possible subset possible
    if totalSum // 2 > g:
        return "NO"
    N = len(arr)
    #create subset DP array with size g and  N+1
    subsetDP =[]
    for i in range(N+1):
        subsetDP.append([0] * (g+1))
    for robber in range(N+1):
        for time in range(g+1):
            #at time 0 the sum is 0 and if no robber is considered then sum = 0
            if robber == 0 or time == 0:
                subsetDP[robber][time] = 0
            #if the time taken by robber is greater than current time we dont consider
            # that robber and assign time same as not previous robber
            elif arr[robber-1] > time:
                subsetDP[robber][time] = subsetDP[robber-1][time]
            # It means robber can rob within time and hence take max of considering the robber or
            # don't consider him in this time
            else:
                considerRobber = subsetDP[robber-1][time-arr[robber-1]] + arr[robber-1]
                notConsiderRobber = subsetDP[robber-1][time]
                subsetDP[robber][time] = max(considerRobber, notConsiderRobber)
    maxSum = subsetDP[N][g]
    if totalSum - maxSum <= g:
        return "YES"
    return "NO"


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        ng = input().split()
        n = int(ng[0])
        g = int(ng[1])
        arr = list(map(int, input().rstrip().split()))
        result = indianJob(g,arr)
        print(result)