def init_data(job_num):
    p, w, r = dict(), dict(), dict()
    ps = [1, 93, 26, 30, 93, 76, 48, 90, 98, 27, 78, 42, 75, 79, 79, 43, 95, 80, 83, 10]
    ws = [1, 3, 3, 5, 9, 7, 3, 9, 10, 4, 8, 7, 9, 2, 10, 9, 5, 4, 1, 9]
    rs = [63,4,63,99,73,20,37,40,77,112,62,36,52,22,9,6,51,76,219,118]
    J = [i+1 for i in range(len(ps))]
    ps, ws, rs, J = ps[:job_num], ws[:job_num], rs[:job_num], J[:job_num]
    for j, p_value, w_value, r_value in zip(J, ps, ws, rs):
        p[j] = p_value
        w[j] = w_value
        r[j] = r_value
    Ts = max(rs) + sum(ps)
    T = [t for t in range(Ts+1)]
    return p, w, r, J, Ts, T