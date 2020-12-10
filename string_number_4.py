# string-number

digits = ["zero", "one", "two", "three",'four',
          'five', 'six', 'seven', 'eight', 'nine',
          'ten', 'eleven', 'twelve', 'thirteen',
          'fourteen', 'fifteen', 'sixteen',
          'seventeen','eighteen', 'nineteen']

decads = ['twenty', 'thirty', 'forty', 'fifty',
          'sixty','seventy','eighty', 'ninety']

def translator(s):
    out = 0
    a = s.split()
    if "trillion" in s:
        return "Fail"
    if "billion" in s:
        f = False
        x = -1
        y = a.index("billion")
        for i in range(x+1, y):
            if "hundred" == a[i]:
                f = True
                break
        outT = 0
        if f:
            outT += digits.index(a[x+1])*100
            for i in range(x+2, y):
                q = a[i].split('-')
                for j in q:
                    if j in decads:
                        outT += (decads.index(j)+2)*10
                    if j in digits:
                        outT += digits.index(j)
        else:
            for i in range(x+1, y):
                q = a[i].split('-')
                for j in q:
                    if j in decads:
                        outT += (decads.index(j)+2)*10
                    if j in digits:
                        outT += digits.index(j)
        out += outT*1000000000
    if "million" in s:
        f = False
        if "billion" not in s:
            x = -1
        else:
            x = y
        y = a.index("million")
        for i in range(x+1, y):
            if "hundred" == a[i]:
                f = True
                break
        outT = 0
        if f:
            outT += digits.index(a[x+1])*100
            for i in range(x+2, y):
                q = a[i].split('-')
                for j in q:
                    if j in decads:
                        outT += (decads.index(j)+2)*10
                    if j in digits:
                        outT += digits.index(j)
        else:
            for i in range(x+1, y):
                q = a[i].split('-')
                for j in q:
                    if j in decads:
                        outT += (decads.index(j)+2)*10
                    if j in digits:
                        outT += digits.index(j)
        out += outT*1000000
    if "thousand" in s:
        f = False
        if "million" not in s and "billion" not in s :
            x = -1
        else:
            x = y
        y = a.index("thousand")
        for i in range(x+1, y):
            if "hundred" == a[i]:
                f = True
                break
        outT = 0
        if f:
            outT += digits.index(a[x+1])*100
            for i in range(x+2, y):
                q = a[i].split('-')
                for j in q:
                    if j in decads:
                        outT += (decads.index(j)+2)*10
                    if j in digits:
                        outT += digits.index(j)
        else:
            for i in range(x+1, y):
                q = a[i].split('-')
                for j in q:
                    if j in decads:
                        outT += (decads.index(j)+2)*10
                    if j in digits:
                        outT += digits.index(j)
        out += outT*1000
    if "thousand" in s:
        x = a.index("thousand")
    elif "million" in s:
        x = a.index("million")
    elif "billion" in s:
        x = a.index("billion")
    else:
        x = -1
    f = False 
    outT = 0
    y = len(a)
    for i in range(x+1, y):
        if "hundred" == a[i]:
            f = True
            break
    if f:
        outT += digits.index(a[x+1])*100
        for i in range(x+2, y):
            q = a[i].split('-')
            for j in q:
                if j in decads:
                    outT += (decads.index(j)+2)*10
                if j in digits:
                    outT += digits.index(j)
    else:
        for i in range(x+1, y):
            q = a[i].split('-')
            for j in q:
                if j in decads:
                    outT += (decads.index(j)+2)*10
                if j in digits:
                    outT += digits.index(j)
    out += outT
    return str(out)

