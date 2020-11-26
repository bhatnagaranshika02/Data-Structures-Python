
def TSP(graph , S, i):
	if len(S) == 1:
		return graph[i][0]
	else:
		costs=[]
		for j in S:
			if j!=0 and j!=i:
				costs.append(TSP(graph,S-{i},j)+graph[j][i])
		return min(costs)



n  =int(input())
graph=[]
for i in range(n):
	edges = list(map(int,input().split()))
	graph.append(edges)

# print(graph,sep=' ')
cost = TSP(graph,{i for i in range(n)} , 0)

print('\n',cost)