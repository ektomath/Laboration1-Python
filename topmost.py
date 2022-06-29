import sys
import wordfreq
import urllib.request
textlist = []
stoplist = []
n = int(sys.argv[3])


if sys.argv[2].startswith('http'):
    response = urllib.request.urlopen(sys.argv[2])
    lines = response.read().decode("utf-8").splitlines()
    for line in lines:
        textlist.append(line.strip('\n'))

else:
    inp_file = open(sys.argv[2], encoding="utf-8")
    for line in inp_file:
        textlist.append(line.strip('\n'))
    inp_file.close()
    #print(textlist)


stop_file = open(sys.argv[1], encoding="utf-8")
for line in stop_file:
    stoplist.append(line.strip('\n'))
stop_file.close()


tokenized = wordfreq.tokenize(textlist)
counted = wordfreq.countWords(tokenized, stoplist)
listed = wordfreq.printTopMost(counted, n)
print(listed)