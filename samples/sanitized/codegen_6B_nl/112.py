
def reverse_delete(s,c):
    """
    Task
    Humare paas do strings s aur c di gayi hain, aapko s mein se un sabhi characters ko delete karna hai jo c ke kisi bhi character ke barabar hain
    phir check karo ki resultant string palindrome hai ya nahi.
    Ek string ko palindrome tabhi kaha jata hai jab woh backward aur forward dono taraf se same padhti ho.
    Aapko ek tuple return karna hai jisme resultant string aur True/False check ke liye hoga.
    Udaharan
    Agar s = "abcde", c = "ae", toh result ('bcd',False) hona chahiye
    Agar s = "abcdef", c = "b"  toh result ('acdef',False) hona chahiye
    Agar s = "abcdedcba", c = "ab", toh result ('cdedc',True) hona chahiye
    """
    if s and c:
        if not s == c:
            diffc = c.difference(s)
            revs = []
            for i in diffc:
                revs.append(re.sub(r's(\w)(\1)', '\1*\2', diffc))

            revstring = ''.join(revs)
            if int(revs)!= len(revs) or revstring!= revstring[::-1]:
                revs.append('***')
                revc = 0
                for i in revs: