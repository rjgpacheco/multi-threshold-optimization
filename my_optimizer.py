

def calc_df(f, u, step=float(1e-6)):
    d = []
    for i, _ in enumerate(u):
        v = [x for x in u]
        v[i] = v[i] + step
        derivative = f(v) - f(u)
        derivative = derivative / step
        d.append(derivative)        
    return d
    
    

def calc_diff(u,v):
    if len(u) == 1:
        return abs(u-v)
    acc = 0
    for x in zip(u,v):
        acc = acc + (x[1] - x[0])**2
    return acc ** (1/2)


def find_minimum(f, x0, learning_rate=0.1, max_iterations=10000, tol=1e-6):
    import math
    x  = []
    df = []

    x.append(x0)
    df.append(math.inf)
    loop_counter = 0
    diff = math.inf
    while diff > tol:
        loop_counter = loop_counter + 1
        if loop_counter > 10000:
            break

        new_df = calc_df(f, x[-1])
        new_x  = [x[-1][i] - learning_rate*new_df[i] for i in range(len(x[-1]))]

        df.append(new_df)
        x.append(new_x)

        diff = calc_diff(x[-2], x[-1])
    
    return {
        "x": x,
        "df": df,
        "loop_counter": loop_counter
    }