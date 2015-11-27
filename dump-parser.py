#!/usr/bin/python
from validate_email import validate_email
import sys


def stringToIntArray(indexs):
    return map(int, indexs.split())


def displayLine(item, idemail, indexs):
    for i, index in enumerate(indexs):
        if index == idemail:
            p = "[{}] {:>40}".format(idemail, item[0].encode('string_escape'))
        else:
            p += " [{}] : {}".format(index, item[i].encode('string_escape'))
    return p


filename = raw_input("Enter filename : ")
seperator = raw_input("Enter data seperator [,]: ")

indexs = raw_input("Enter selected indexs (seperate by a single space): ")
indexs = stringToIntArray(indexs)

idemail = int(raw_input("Enter email index in file \
                            (blank for no email check): "))

not_blank_indexs = raw_input("Enter non blank check indexs \
                            (blank for no blan check): ")
not_blank_indexs = stringToIntArray(not_blank_indexs)

print "Dump : {}".format(filename)
print "Id Email : {}".format(idemail)

try:
    user = 0
    result = {}

    with open(filename, 'r') as f:
        for line in f:
            array = line.strip().split(seperator)
            is_valid = validate_email(array[idemail]) if idemail != "" else True

            if is_valid:
                is_selected = True
                for index in not_blank_indexs:
                    if array[index] in ("<blank>", ""):
                        is_selected = False
                        break

            if is_valid and is_selected:
                user += 1
                domaine = array[idemail].split("@")[1].encode('string_escape')

                entry = [array[index] for index in indexs]

                result.setdefault(domaine.lower(), []).append(entry)

except IOError:
    print "Error in handling file {}".format(filename)
    sys.exit(-1)

# Display all domaines
for i, domaine in enumerate(result, 1):
    print "{:3} : {}".format(i, domaine)

for domaine in result:
    print "[domaine : ] " + domaine
    nbemail = 0
    for item in result[domaine]:
        print displayLine(item, idemail, indexs)
        nbemail += 1
    print "=============================== {} ===========================".format(nbemail)

print "Total {}".format(user)
