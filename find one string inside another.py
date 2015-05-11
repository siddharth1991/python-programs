__author__ = 'siddharth'

class FindString:
    def __init__(self, original_string, string_to_find):
        i=0
        j=0
        while i < len(original_string):
            while j < len(string_to_find):
                if original_string[i] == string_to_find[j]:
                    i += 1
                    j += 1
                    if j > len(string_to_find)-1:
                        print "String matched"
                        exit(0)
                    elif i == len(original_string):
                        print "String not found"
                        exit()
                else:
                    i += 1
                    j = 0
                    break

        print "String not found"

f = FindString('siddharth', 'ddharth')