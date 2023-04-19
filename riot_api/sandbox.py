import time

lol_time = 1681760967467
convert_time = lol_time/1000

now = time.time()
now_nice = time.ctime(time.time())
one_day = 86400
one_week = 7 * 86400
one_day_ago = now - one_day

print(now)
print(one_day_ago)