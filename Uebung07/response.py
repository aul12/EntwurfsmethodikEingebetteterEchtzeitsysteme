import math
import copy


def lowest_period_prio(task):
    return -task["p"]
     

def get_response_times(tasks, prio):
    r = {}
    for i, task in enumerate(tasks):
        r[i] = task["c_plus"]

    r_changed = True

    while r_changed:
        r_changed = False
        new_r = copy.deepcopy(r)

        for i, task in enumerate(tasks):
            this_r = task["c_plus"]
            for j, tau in enumerate(tasks):
                if prio(tau) > prio(task):
                    eta = math.ceil(r[i] / tasks[j]["p"])
                    this_r += eta * tasks[j]["c_plus"]
            
            if new_r[i] != this_r:
                new_r[i] = this_r
                r_changed = True
        
        r = new_r                

    return r

def main():
    script = [
        {"c_plus": 2, "p": 5, "d": 5},
        {"c_plus": 10, "p": 20, "d": 20},
    ]

    gamma2 = [
        {"c_plus": 1, "p": 10, "d": 10},
        {"c_plus": 2, "p": 20, "d": 20},
        {"c_plus": 4, "p": 50, "d": 50},
        {"c_plus": 10, "p": 100, "d": 100},
    ]

    gamma3 = [
        {"c_plus": 1, "p": 4, "d": 4},
        {"c_plus": 2, "p": 6, "d": 6},
        {"c_plus": 3, "p": 10, "d": 10},
    ]


    print("Example from script:\t", get_response_times(script, lowest_period_prio))
    print("Gamma 2:\t", get_response_times(gamma2, lowest_period_prio))
    print("Gamma 3:\t", get_response_times(gamma3, lowest_period_prio))
         

if __name__=="__main__":
    main()
