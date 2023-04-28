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
for j in J:
    prob+= C[j]==s[j]+p[j]
    prob+=s[j]>=r[j]
    for k in J:
        prob+= s[j] >= r[k]*x[k,j] + pulp.lpSum(p[i]*(x[i,j] - x[i,k]) for i in J)
        if j!=k:
            prob+=x[j,k]+x[k,j]==1
        for i in J:
            prob += x[j,k] + x[k,i] +x[i,j] <= 2
# print(prob)

prob.solve()
print(pulp.LpStatus[prob.status])
for v in prob.variables():
    if "x" in v.name:
        print(v.name,"=",v.varValue) if v.varValue == 1 else None
    else:
        print(v.name,"=",v.varValue)
print("Optimal value=",prob.objective.value())