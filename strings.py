from collections import Counter
import heapq


s = 'aaaabbb'

s = list(s);

freqeuncies = Counter(s);
high_freq = 0;
high_key = '';

for key in freqeuncies:
    if freqeuncies[key] > high_freq:
        high_freq = freqeuncies[key]
        high_key = key

res = [high_key];

while True:
    found_update = False
    
    for key in freqeuncies:
        if key != res[-1] and freqeuncies[key] > 0:
            found_update = True;
            freqeuncies[key] -= 1;
            res.append(key);
    if found_update == False:
        break;
    
    # removes keys with frequency 0
    remove_list = []
    for key in freqeuncies:
        if freqeuncies[key] == 0:
            remove_list.append(key);

    for e in remove_list:
        del freqeuncies[e];
    
    #break if no more keys to try
    if not freqeuncies:
        break;
        
if len(res) != len(s):
    print('');
else:
    print(res);