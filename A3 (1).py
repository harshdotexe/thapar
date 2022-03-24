#ADITYA GARG 102053015
from copy import deepcopy
class Puzzel:
    def __init__(self, initial_state):
        self.initial = initial_state
        self.queue = []
        self.visited = []

    def _find_pos(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def _right(self, state, pos):
        i, j = pos

        if j != 2:
            t = deepcopy(state)
            t[i][j], t[i][j+1] = t[i][j+1], t[i][j]
            return t
        else:
            return state

    def _left(self, state, pos):
        i, j = pos

        if j != 0:
            t = deepcopy(state)
            t[i][j], t[i][j-1] = t[i][j-1], t[i][j]
            return t
        else:
            return state

    def _up(self, state, pos):
        i, j = pos

        if i != 0:
            t = deepcopy(state)
            t[i][j], t[i-1][j] = t[i-1][j], t[i][j]
            return t
        else:
            return state

    def _down(self, state, pos):
        i, j = pos

        if i != 2:
            t = deepcopy(state)
            t[i][j], t[i+1][j] = t[i+1][j], t[i][j]
            return t
        else:
            return state

    def _enque(self, new_state):

        x = self._heu_mok(new_state)

        if len(self.queue) == 0:
            self.queue.append(new_state)

        elif x < self._heu_mok(self.queue[0]):
            self.queue.insert(0, new_state)
        else:
            for i in range(1, len(self.queue)):
                if self._heu_mok(self.queue[i]) > x:
                    self.queue.insert(i-1, new_state)

    def _deque(self):
  
        self.visited.append(self.queue[0])

        ele = self.queue.pop(0)

        return ele

    def _heu_mok(self, state):
        val = 0

        for x in range(3):
            for i in range(3):
                q = state[x][i]

                for j in range(3):
                    for k in range(3):
                        if q == self.goal[j][k] and not (x == j and i == k):
                            val += pow(abs(x-j)+abs(i-k),3)
                            break
        return pow(val,1/3)

    def _print(self, vis):
        for k in range(len(vis)-1):
            x = vis[k]
            for i in range(3):
                for j in range(3):
                    print(x[i][j], end=" ")
                print("\n")
            print("  |")
            print("  |")
            print("  V")
        x = vis[-1]
        for i in range(3):
            for j in range(3):
                print(x[i][j], end=" ")
            print("\n")

    def Solve(self, goal_state):

        current_state = deepcopy(self.initial)
        self.goal = goal_state
        if current_state == goal_state:
            return

        while 1:
            pos = self._find_pos(current_state)
      
            new_state = self._down(current_state, pos)
        
            if new_state != current_state:
                if new_state == goal_state:
                    print("Goal State Reached!!")
                    self.visited.append(new_state)

                    
                    self._print(self.visited)
                    return
                else:
                    if new_state not in self.visited:
                        self._enque(new_state)

            new_state = self._left(current_state, pos)
            if new_state != current_state:
                if new_state == goal_state:
                    print("Goal State Reached!!")
                    self.visited.append(new_state)

                    
                    self._print(self.visited)
                    return
                else:
                    if new_state not in self.visited:
                        self._enque(new_state)

            new_state = self._right(current_state, pos)
            if new_state != current_state:
                if new_state == goal_state:
                    print("Goal State Reached!!")
                    self.visited.append(new_state)

             
                    self._print(self.visited)
                    return
                else:
                    if new_state not in self.visited:
                        self._enque(new_state)

            new_state = self._up(current_state, pos)
            if new_state != current_state:
                if new_state == goal_state:
                    print("Goal State Reached!!")
                    self.visited.append(new_state)

                  
                    self._print(self.visited)
                    return
                else:
                    if new_state not in self.visited:
                        self._enque(new_state)



            if len(self.queue) > 0:
                current_state = self._deque()
            else:
                print("Not Found!")
                return


if __name__ == '__main__':
    P = Puzzel([[2, 0, 3], [1, 8, 4], [7, 6, 5]])
    P.Solve([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
