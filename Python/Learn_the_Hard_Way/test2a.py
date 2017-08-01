
input_list = ['cat','dog','rat','mouse','bird','cat','dog','snake','dog','Tony']

def unique(data):
    output = []
    for tester in data:
        if tester not in output:
            output.append(tester)
    print output




##### make it more effecient #####

def unique2(data):
    output = []
    found = {}
    for tester in data:
        if tester not in found:
            output.append(tester)
            found[tester] = True
    print output

unique2(input_list)
