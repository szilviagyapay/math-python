part_perf = 1
part_all = 2
p_m = part_perf/part_all

k = 6
e = 4/13

part_perf = 1
part_all = 2
p_m = part_perf/part_all

e = 1/12345
a = 2 
k = 6

while (e <= p_m):
    a = a + 1
    pow_2_t = a + 1
    part_all += 1
    t = math.log(pow_2_t,2)
    if (t - math.floor(t) == 0):
            part_perf += 1
    #print("Partition is found: t = ", t, ", k = ", a*a + a)
    p_m = part_perf/part_all

print("Smallest m for wich P_m < e is ", a*a + a)
    