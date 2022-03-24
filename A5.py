#ADITYA GARG 102053015
def UC_Search(goal, start):

  global graph,cost
  ans = []

  # create a priority queue
  queue = []

  # set ans vector to max value
  for i in range(len(goal)):
    ans.append(10**8)
  
  # insert starting index
  queue.append([0, start])

  # store visited nodes
  visited = {}

  count = 0
  while (len(queue) > 0):
    queue = sorted(queue)
    p = queue[-1]

    # pop the element from queue
    del queue[-1]
    p[0] *= -1
    
    # check if the element is part of goal state
    if (p[1] in goal):
      index = goal.index(p[1])
      if (ans[index] == 10**8):
        count += 1
      if (ans[index] > p[0]):
        ans[index] = p[0]
      del queue[-1]
      queue = sorted(queue)
      if (count == len(goal)):
        return ans

    if (p[1] not in visited):
      for i in range(len(graph[p[1]])):
        queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])
      # mark as visited
      visited[p[1]] = 1
  return ans

if __name__ == '__main__':
  S=0
  A=1
  B=2
  C=3
  G=4

  # create graph
  graph,cost = [[] for i in range(6)],{}

  # add edge
  graph[S].append(B)
  graph[S].append(A)
  graph[S].append(C)
  graph[C].append(G)
  graph[B].append(G)
  graph[A].append(G)
  
  graph[B].append(S)
  graph[A].append(S)
  graph[C].append(S)
  graph[G].append(C)
  graph[G].append(B)
  graph[G].append(A)

  # add the cost
  cost[(S, C)] = 15
  cost[(S, B)] = 5
  cost[(S, A)] = 1
  cost[(C, G)] = 5
  cost[(B, G)] = 5
  cost[(A, G)] = 10
  cost[(C, S)] = 15
  cost[(B, S)] = 5
  cost[(A, S)] = 1
  cost[(G, C)] = 5
  cost[(G, B)] = 5
  cost[(G, A)] = 10

  # goal state
  goal = []

  # set G node as goal state
  goal.append(G)

  ans = UC_Search(goal, A)
  print("Minimum cost from A to G is = ",ans[0])