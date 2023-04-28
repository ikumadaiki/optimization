import pulp
import init_data
job_num = 13
p, w, r, J = init_data.init_data(job_num)

JK=[(j,k) for j in J for k in J]
M=1000
prob=pulp.LpProblem(name="prob", sense=pulp.LpMinimize)
s = pulp.LpVariable.dicts('s', J, lowBound=0, cat='Continuous')
C = pulp.LpVariable.dicts('C', J, lowBound=0, cat='Continuous')
x = pulp.LpVariable.dicts('x',JK ,  cat='Binary')
w_list, C_list = [], []
for j in J:
    w_list.append(w[j])
    C_list.append(C[j])
prob+=pulp.lpDot(C_list, w_list)
for j in range(1,len(J)+1):
    prob+= C[j]==s[j]+p[j]
    prob+=s[j]>=r[j]
    for k in range(1,len(J)+1):
        prob+=C[j]<=s[k]+M*(1-x[j,k])
        if j!=k:
            prob+=x[j,k]+x[k,j]==1

prob.solve()
print(pulp.LpStatus[prob.status])
for v in prob.variables():
    if "x" in v.name:
        print(v.name,"=",v.varValue) if v.varValue == 1 else None
    else:
        print(v.name,"=",v.varValue)
print("Optimal value=",prob.objective.value())