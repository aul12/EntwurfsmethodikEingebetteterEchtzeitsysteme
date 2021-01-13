import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcd(a, b):
    return abs(a*b) // gcd(a, b)

def get_busy_period(tasks, prio):
    remaining_times = []
    h = 1
    for task in tasks:
        h = lcd(h, task["p"])
        remaining_times.append(0)

    max_busy = 0
    current_busy = 0

    for t in range(h):
        # Check if new tasks exist
        for i, task in enumerate(tasks):
            if t % task["p"] == 0:
                remaining_times[i] += task["c_plus"]

        # Find the task to run
        max_prio = -math.inf
        max_task = None
        for i, task in enumerate(tasks):
            if remaining_times[i] > 0 and prio(task) > max_prio:
                max_task = i
                max_prio = prio(task)
    
        # "Run" the task
        if max_task is not None:
            remaining_times[max_task] -= 1
            current_busy += 1
        else:
            if current_busy > max_busy:
                max_busy = current_busy
            current_busy = 0
        
    return max_busy
       

def lowest_period_prio(task):
    return -task["p"]


def main():
    gamma4 = [
        {"c_plus": 1, "p": 4},
        {"c_plus": 2, "p": 6},
        {"c_plus": 3, "p": 8},
    ]

    gamma5 = [
        {"c_plus": 1, "p": 4},
        {"c_plus": 2, "p": 6},
        {"c_plus": 3, "p": 10},
    ]

    print(get_busy_period(gamma4, lowest_period_prio))
    print(get_busy_period(gamma5, lowest_period_prio))
    

if __name__=="__main__":
    main()
