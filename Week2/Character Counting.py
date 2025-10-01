def demchu(path) :
    file = open(path,'r')
    str = file.read()
    str = str.lower()
    c_map = {}
    for i in str :
        if i in c_map :
            c_map[i] += 1
        else :
            c_map[i] = 1 


def demtu(path):
    with open(path,'r') as f :
        sentences = f.readlines()
    for sentence in sentences :
        sentence.lower()
        sentence.replace(',' , '' ).replace('.','')
        words = sentence.split()
        

def demchu("/home/nexy/Code/AIVIETNAM/Documentss/P1_data.txt")
print(c_map)
