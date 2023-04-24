import pulp

# 定式化3
J = [1, 2, 3]
p, w, r = dict(), dict(), dict()
ps = [2, 2, 3]
ws = [3, 2, 1]
rs = [1, 0, 0]
for j, p_value, w_value, r_value in zip(J, ps, ws, rs):
    p[j] = p_value
    w[j] = w_value
    r[j] = r_value
    
Ts = max(rs) + sum(ps)
T = [t for t in range(Ts+1)]
JT = [(j,t) for j in J for t in T]
prob=pulp.LpProblem(name="prob", sense=pulp.LpMinimize)
z = pulp.LpVariable.dicts('z', JT,  cat='Binary')
w_list, z_list = [], []

for j in J:
    w_list.append(w[j])
    # C_list.append(C[j])
    z_list.append(pulp.lpSum(t*z[j,t] for t in T) + p[j])
dot_product = sum([x * y for x, y in zip(w_list, z_list)])
prob += dot_product
for j in J:
    prob += pulp.lpSum(z[j,t] for t in range(r[j], Ts - p[j] +1)) == 1
for t in T:
    prob += pulp.lpSum(pulp.lpSum(z[j,t_] for t_ in range(max(0, t - p[j] + 1), t + 1)) for j in J) <= 1
# print(prob)

prob.solve()
print(pulp.LpStatus[prob.status])
for v in prob.variables():
    if "z" in v.name:
        print(v.name,"=",v.varValue) if v.varValue == 1 else None
    else:
        print(v.name,"=",v.varValue)
print("Optimal value=",prob.objective.value())