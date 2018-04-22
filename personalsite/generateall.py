from os import listdir
from os.path import isfile, join
mypath = './images/portfolio/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

string = ''
modal = ''
i = 1

for d in onlyfiles:
    string = string + '<div class="columns portfolio-item"> <div class="item-wrap"><a href="#modal-' + str(i) + '" title=""><img src="images/portfolio/' + d + '"/></a></div></div>'
    modal = modal + '<div id="modal-' + str(i) + '" class="popup-modal mfp-hide"><img class="scale-with-grid" src="images/portfolio/' + d + '"/></div>'
    i = i + 1
print(string)
print(modal)