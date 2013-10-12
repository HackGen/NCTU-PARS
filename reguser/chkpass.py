def checkStrongPass(passwd):
    import crack

    crack.min_length = 11
    try:
        crack.VeryFascistCheck(passwd)
    except ValueError, msg:
        raise ValueError(msg)
    return passwd


# simple testing
if __name__ == '__main__':
    for passwd in ["5566", "5566dd11asdf", "asdftesting", "asdf"]:
        try:
            print "[+] legal password {}".format(checkStrongPass(passwd))
        except ValueError, msg:
            print "[-] illegal password {} {}".format(passwd, msg)
