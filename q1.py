# Name:Girish Gupta
# Roll No:102003323
# Class:Coe-13

capacity=[4,3]
jug1=capacity[0]
jug2=capacity[1]
states=[]
def get_all_states(state):
    s1=state[0]
    s2=state[1]
    if(s1==2):
        states.append(state)
        return True
    if(s1==0 and s2==0):
        if(get_all_states((0,s1+3))):
            states.append(state)
            return True
    if(s1==0 and s2>0):
        if(get_all_states((s1+s2,0))):
            states.append(state)
            return True
    if(s1==3 and s2==0):
        if(get_all_states((s1,s2+3))):
            states.append(state)
            return True
    if(s1==3 and s2==3):
        if(get_all_states((s1+1,s1-1))):
            states.append(state)
            return True
    if(s1>3):
        if(get_all_states((0,s2))):
            states.append(state)
            return True
initial_state=[0,0]
get_all_states(initial_state)
states.reverse()
for i in states:
    print(i)