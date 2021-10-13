def evenDash(string):
    result = ""
    string = str(string)
    i = 0
    for s in str(string):
        if (int(s) % 2) == 0:
            if i < len(string) - 1:
                if (int(string[i+1]) % 2) == 0:
                    result = result + s + "-"
                else:
                    result += s
            else:
                result += s
        else:
            result += s
            
        i += 1
    print(result)
    
evenDash(553847)
