class Solution:
    def jobSequencing(self, deadline, profit):
        jobs=[]
        n=len(profit)
        for i in range(n):
            jobs.append((profit[i],deadline[i]))
        jobs.sort(reverse=True,key=lambda x:x[0])
        max_deadline=max(job[1] for job in jobs)
        parent=list(range(max_deadline+1))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(u,v):
            parent[u]=v
        total_profit=0
        count_job=0
        for profit,deadline in jobs:
            available_slots=find(deadline)
            if available_slots>0:
                union(available_slots,available_slots-1)
                total_profit+=profit
                count_job+=1
            sol=[count_job,total_profit]
        return sol 
    