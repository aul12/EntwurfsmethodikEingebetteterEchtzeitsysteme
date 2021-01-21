import math
import copy


def lowest_deadline_prio(task):
    return -task["d"]
     

def eq25(tasks, prio, q, tau):
    w = tasks[tau]["c"]

    while True:
        new_w = tasks[tau]["c"] * (q+1)
        for tau_ in tasks:
            if prio(tau_) > prio(tasks[tau]):
                eta = math.ceil((w+tau_["j"]*2) / tau_["p"])
                new_w += eta * tau_["c"]

        if w == new_w:
            return w

        w = new_w
        

def r_plus(tasks, prio, tau):
    r_tau_plus = -math.inf

    for q in range(100):
        w = eq25(tasks, prio, q, tau)
        arg = w - q * tasks[tau]["p"] 

        if arg > r_tau_plus:
            r_tau_plus = arg

    return r_tau_plus


def r_minus(tasks, prio, tau):
    r = r_plus(tasks, prio, tau)
    while True:
        new_r = tasks[tau]["c"]
        for tau_ in tasks:
            if prio(tau_) > prio(tasks[tau]):
                m = max(math.ceil((r - tau_["j"] - tau_["p"])/tau_["p"]), 0)
                new_r += m * tau_["c"]
        if new_r == r:
            return r

        r = new_r


def main():
    # c is the same as c_minus
    cpu_1 = [
        {"j": 0, "c": 200, "p": 800, "d": 1100},
        {"j": 0, "c": 20, "p": 60, "d": 60},
        {"j": 0, "c": 1, "p": 4, "d": 2},
    ]

    cpu_2 = [
        {"j": 0, "c": 200, "p": 800, "d": 700},
        {"j": 0, "c": 20, "p": 60, "d": 40},
    ]

    cpu_2[0]["j"] = cpu_1[0]["j"] + r_plus(cpu_1, lowest_deadline_prio, 0) - r_minus(cpu_1, lowest_deadline_prio, 0)
    cpu_2[1]["j"] = cpu_1[1]["j"] + r_plus(cpu_1, lowest_deadline_prio, 1) - r_minus(cpu_1, lowest_deadline_prio, 1)

    print("a)")
    print("j_4 =", cpu_2[0]["j"])
    print("j_5 =", cpu_2[1]["j"])

    print("b)") 
    print(r_plus(cpu_2, lowest_deadline_prio, 0))

         

if __name__=="__main__":
    main()
