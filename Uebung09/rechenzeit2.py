import math

def satz12(t, gamma):
    ret = 0
    for tau in gamma:
        ret += math.floor((t-tau["d"])/tau["p"] + 1) * tau["c_plus"] 

    return ret


def main():
    gamma = [
        {"p": 22, "c_plus": 4, "d": 15},
        {"p": 35, "c_plus": 10, "d": 30},
        {"p": 55, "c_plus": 18, "d": 45},
    ]

    for t in range(720):
        rechenzeit = satz12(t, gamma)
        print(t, rechenzeit)
        if rechenzeit > t:
            print("\tError!") 



if __name__=="__main__":
    main()
