Given t targets at 1-meter intervals & p pumpkins to be thrown via trebuchet, what is the worst-case minimum number of throws necessary to determine the max. distance a pumpkin can be thron without shattering on impact

Recurrence Relation:
    T(p, t) = 1 + min (max([T(p-1, x-1), T(p, t-x)]))

    Base Cases:
        T(p, 0) = 0
        T(p, 1) = 1
        T(1, t) = t

Deliverables:
    Recursive algo. to solve problem for p = 3, t = 16.
    How many calls are made to the func.?

    Provide a table or plot of growth in runtime as p/t increases

