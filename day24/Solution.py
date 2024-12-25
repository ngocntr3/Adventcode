import re

wire = {}

def parseInput(file):
    global wire
    f = open(file, "r").read()
    section1 = f.split("\n\n")[0]
    section2 = f.split("\n\n")[1]
    
    # for section 1
    for line in section1.split("\n"):
        k = line.split(": ")[0]
        v = line.split(": ")[1]
        wire[k] = v
    
    # for section2
    for line in section2.split("\n"):
        k = line.split(" -> ")[1]
        v = line.split(" -> ")[0]
        wire[k] = v

def isPrimitive(ele):
    regex = re.compile(r'^[x-z]\d{2}$')
    if regex.match(ele):
        return True
    return False

def analyseExp(exp):
    p1, op, p2 = "", "", ""
    if " AND " in exp:
        p1 = exp.split(" AND ")[0]
        op = "&"
        p2 = exp.split(" AND ")[1]
    if " OR " in exp:
        p1 = exp.split(" OR ")[0]
        op = "|"
        p2 = exp.split(" OR ")[1]
    if " XOR " in exp:
        p1 = exp.split(" XOR ")[0]
        op = "^"
        p2 = exp.split(" XOR ")[1]
    return p1, op, p2

def isExp(exp):
    if (exp == "1") or (exp == "0"):
        return False
    else:
        return True

def solveExp(key):
    global wire
    print("[++] SolveExp("+key+") = " + wire[key])
    if not isExp(str(wire[key])):
        print("[-] Return exp: "+"wire["+key+"] = "+str(wire[key]))
        return eval(wire[key])

    p1, op, p2 = analyseExp(wire[key])
    sp1, sp2 = "", ""
    try:
        print("[-] Try: " + p1 + " " + op + " " + p2)
        sp1 = str(solveExp(p1))
        sp2 = str(solveExp(p2))
        print("[-] SolveExp("+p1+") = " + str(sp1) + "; solveExp("+p2+") = " + str(sp2))
        wire[key] = str(eval(sp1 + op + sp2))
        print("[-] Wire["+key+"] = "+str(wire[key]))
    except:
        print("[-] Exception:", sp1, op, sp2)
        # exit(0)

    

if __name__ == "__main__":
    parseInput("./input.txt")
    for k in wire:
        solveExp(k)
    print(wire)