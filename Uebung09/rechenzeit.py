import math

def satz12(t, gamma):
    ret = 0
    for tau in gamma:
        ret += math.floor((t-tau["d"])/tau["p"] + 1) * tau["c_plus"] 

    return ret


def main():
    gamma = [
        {"p": 10, "c_plus": 5, "d": 5},
        {"p": 55, "c_plus": 10, "d": 40},
        {"p": 100, "c_plus": 15, "d": 75},
        {"p": 200, "c_plus": 20, "d": 150},
    ]

    for i in range(42):
        t = i * 5
        rechenzeit = satz12(t, gamma)
        print(t, rechenzeit)
        if rechenzeit > t:
            print("\tError!") 



if __name__=="__main__":
    main()
