import math
import copy


def lowest_deadline_prio(task):
    return -task["d"]
     

def eq25(tasks, prio, q, tau):
    w = tasks[tau]["c_plus"]

    while True:
        new_w = tasks[tau]["c_plus"] * (q+1)
        for tau_ in tasks:
            if prio(tau_) > prio(tasks[tau]):
                eta = math.ceil((w+tau_["j"]*2) / tau_["p"])
                new_w += eta * tau_["c_plus"]

        if w == new_w:
            return w

        w = new_w
        

def eq24(tasks, prio, tau):
    r_tau_plus = -math.inf

    for q in range(100):
        w = eq25(tasks, prio, q, tau)
        arg = w - q * tasks[tau]["p"] 

        if arg > r_tau_plus:
            r_tau_plus = arg

    return r_tau_plus

def main():
    cpu1_1 = [
        {"j": 0, "c_plus": 2, "p": 8, "d": 11},
        {"j": 0, "c_plus": 2+1, "p": 6, "d": 6},
        {"j": 0, "c_plus": 1, "p": 4, "d": 2},
    ]
    cpu1_2 = [
        {"j": 0, "c_plus": 2+1, "p": 8, "d": 11},
        {"j": 0, "c_plus": 2, "p": 6, "d": 6},
        {"j": 0, "c_plus": 1, "p": 4, "d": 2},
    ]
    cpu1_3 = [
        {"j": 0, "c_plus": 2, "p": 8, "d": 11},
        {"j": 0, "c_plus": 2, "p": 6, "d": 6},
        {"j": 0, "c_plus": 1, "p": 4, "d": 2},
    ]

    cpu2_4 = [
        {"j": 2, "c_plus": 2, "p": 5, "d": 7},
        {"j": 1, "c_plus": 2, "p": 4, "d": 4},
    ]
    cpu2_5 = [
        {"j": 2, "c_plus": 2, "p": 5, "d": 7},
        {"j": 1, "c_plus": 2, "p": 4, "d": 4},
    ]

    print(eq24(cpu1_1, lowest_deadline_prio, 0))
    print(eq24(cpu1_2, lowest_deadline_prio, 1))
    print(eq24(cpu1_3, lowest_deadline_prio, 2))
    print(eq24(cpu2_4, lowest_deadline_prio, 0))
    print(eq24(cpu2_5, lowest_deadline_prio, 1))

         

if __name__=="__main__":
    main()
