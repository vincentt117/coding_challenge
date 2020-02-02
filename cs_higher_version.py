# https://app.codesignal.com/challenge/wdaNioTdYMMogFHeH

def higherVersion2(ver1, ver2):
    ver1_list = ver1.split('.')
    ver2_list = ver2.split('.')
    for i in range(len(ver1_list)):
        if (int(ver1_list[i]) > int(ver2_list[i])):
            return 1
        if (int(ver1_list[i]) < int(ver2_list[i])):
            return -1
    return 0
        
