scores = open("test-total.txt", 'r')

scores = [float(s.split()[1]) for s in scores.readlines() if float(s.split()[1]) < 20]


counter_tot = 0.0
counter_over = 0.0
counter_under = 0.0
total_scores = 0.0

for score in scores:
    print score
    total_scores += score
    if score > 9.6:
        counter_over += 1
    else:
        counter_under += 1
    counter_tot += 1

print "Avg: ", total_scores/counter_tot
print "Over: ", counter_over
print "Under: ", counter_under
