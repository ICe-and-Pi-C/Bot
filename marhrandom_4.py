# mathrandom

def MathRandom(s):
    a = s.split('"')
    ans = ''
    for i in a:
        if '|' in i:
            p = i.split('|')
            if p[0] == "cypher":
                x = CaesarForJson(i.split("cypher|")[1])
                p[0] = x.split('|')[0]
                p[1] = x.split('|')[1]
            if p[0] == "math":
                ans += '"' + MathBot3(p[1]) + '" '
            if p[0] == "string-number":
                if "plus" in p[1]:
                    x = p[1].split("plus")
                    ans += '"' + str(int(translator(x[0])) + int(translator(x[1]))) + '" '
                elif "minus" in p[1]:
                    x = p[1].split("minus")
                    ans += '"' + str(int(translator(x[0])) - int(translator(x[1]))) + '" '
                elif "times" in p[1]:
                    x = p[1].split("times")
                    ans += '"' + str(int(translator(x[0])) * int(translator(x[1]))) + '" '
                elif "twice" in p[1]:
                    x = p[1].split("twice")
                    ans += '"' + str(int(translator(x[0]))*2) + '" '
                elif "thrice" in p[1]:
                    x = p[1].split("thrice")
                    ans += '"' + str(int(translator(x[0]))*3) + '" '
                elif "squared" in p[1]:
                    x = p[1].split("squared")
                    ans += '"' + str(round(int(translator(x[0]))**2)) + '" '
                elif "cubed" in p[1]:
                    x = p[1].split("cubed")
                    ans += '"' + str(round(int(translator(x[0]))**3)) + '" '
                else:
                    ans += '"' + str(translator(p[1])) + '" '
            if p[0] == "determinant":
                p[1] = p[1].replace('\\\\', '\\\\\\\\')
                ans += '"' + str(determinant(parse_matrix(p[1]), 1)) + '" '
            if p[0] == "polynomial-root":
                ans += '"' + str(doPolynom(p[1])) + '" '
            
    return ans               

