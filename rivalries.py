#standard file reader from all of my previous assignments
import sys
unsortedMatrix = [];
names = {};
Rivalries = {};
txt = sys.argv[1]
with open(txt) as f:
    unsortedMatrix = f.read().splitlines()
#get the amount of names from the first file arg
nameCount = int(unsortedMatrix[0])
del unsortedMatrix[0]
for i in range(0,nameCount):
    names[unsortedMatrix[0]] = ''
    del unsortedMatrix[0]
#get the rivalrycount from the now-first line
rivalryCount = int(unsortedMatrix[0])
del unsortedMatrix[0]
#for every rivalry split the line and assign the rivals to eachother
#in the the dictionary:[] Rivalries 
for i in range(0,rivalryCount):
    tup = unsortedMatrix[0].split()
    #append the names to the array tied to the name in the dictionary
    Rivalries.setdefault(tup[0], []).append(tup[1])
    Rivalries.setdefault(tup[1], []).append(tup[0]) 
    del unsortedMatrix[0]

def rivalries(names, rivalries):
    #get the keys of both dictionaries
    nKey = names.keys()
    nRiv = rivalries.keys()
    #initialize heels and babyfaces
    heels = []
    babyfaces = []
    for n in range(0, len(names)):
        if n == 0 :
            names[nKey[0]] ='babyface'
            babyfaces.append(nKey[0])
        for r in range(0,len(rivalries[nKey[n]])):
            rival = rivalries[nKey[n]][r]
            #below is syntax to check that the current value tied  to the name doesnt match the rivals value.
            if names[nKey[n]]== 'babyface' and names[rival] != 'babyface':
                if names[rival] == '':
                    names[rival] = 'heels'
                    heels.append( rivalries[nKey[n]][r])
            elif names[nKey[n]] =='heels' and names[rival] != 'heels':
                if names[rival] == '':
                    names[rival] = 'babyface'
                    babyfaces.append(rivalries[nKey[n]][r])
            elif names[nKey[n]] == '':
                if names[rival] == 'heels':
                    names[nKey[n]] = 'babyface'
                    babyfaces.append(nKey[n])
                elif names[rival] == 'babyface':
                    names[nKey[n]]= 'heels'
                    heels.append(nKey[n])
                #holy crap this elif statement is wild, but it captures a uncommon scenario,
                #where if both the current name index and its rival have 1 rival
                #and theyre eachothers rival, then they'll be put on random sides of the rivalry
                elif len(rivalries[nKey[n]]) == 1 and len(rivalries[rival]) == 1 and rivalries[rival][0] == nKey[n] and rivalries[nKey[n]][r] ==rival :
                    names[nKey[n]]= 'heels'
                    heels.append(nKey[n])
                    names[rival] = 'babyface'
                    babyfaces.append(rivalries[nKey[n]][r])
            #if none of these scenarios can be met by the dictionary then its impossible
            else:
                print 'Impossible\n'
                return

    printer = ''      
    print "Yes"
    printer += "Babyfaces: "
    for baby in babyfaces:
        printer += baby
        printer += ' '
    printer += '\nHeels: '
    for heel in heels:
        printer += heel
        printer += ' '
    print printer
		       
rivalries(names, Rivalries)
