import os, sys, time, random

greeting = f"Hello, {os.getlogin()}!"
colors = [31,32,33,34,35,36,91,92,93,94,95,96]
for ch in greeting:
    sys.stdout.write(f"\033[1;{random.choice(colors)}m{ch}\033[0m")
    sys.stdout.flush()
    time.sleep(0.08)
print()