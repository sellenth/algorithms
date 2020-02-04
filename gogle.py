c1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
c1_bounds = ['9:00', '20:00']
c2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
c2_bounds = ['10:00', '8:30']
m_time = 30;

#convert string to int
#create big sorted list of both times
#merge blocks
#find spaces between end time and beginnings > 30 mins
#enforce bounds
#return

def str_to_int(s):
    first, second = s.split(':');
    return int(first) + (int(second) / 60);

def gte(t1, t2):
    t1 = str_to_int(t1);
    t2 = str_to_int(t2);
    if t1 > t2:
        return 1;
    if t1 == t2:
        return 0;
    if t1 < t2:
        return -1;

def merge(l1, l2):
    i = 0;
    j = 0;
    merged = []

    while i < len(l1) or j < len(l2):
        if i >= len(l1):
            for e in l2[j:]:
                merged.append(e);
            break;
        if j >= len(l2):
            for e in l1[i:]:
                merged.append(e);
            break;

        if gte(l1[i][0], l2[j][0]) == -1:
            merged.append(l1[i]);
            i+= 1;
        else:
            merged.append(l2[j]);
            j+= 1;

    return merged;

def find_slots(l):
    avail = []
    for i in range(len(l) - 1):
        end = str_to_int(l[i][1]);
        start = str_to_int(l[i+1][0]);

        if start - end >= .5:
            avail.append([end, start]);
    return avail;
            


merged = merge(c1, c2);
print(find_slots(merged));
    

