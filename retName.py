#This stuff all works good
import FindLatestDate
import csv
csvfile = open('../contactsJune6.csv', 'r')
outfile = open('CurrentContacts.csv', 'w')
ContactReader = csv.reader(csvfile, delimiter=',')
ContactWriter = csv.writer(outfile, delimiter=',')

#Skip through first header row
ContactWriter.writerow(ContactReader)
ContactReader.next()

count = 0
CurrentContacts = []
for CurrentRow in ContactReader:
    #Find Client File
    FileToOpen = '../highrise-export/contacts/' + CurrentRow[1] +'.txt'
    if int(FindLatestDate.FindLatestDate(FileToOpen)) >= 2010:
        ContactWriter.writerow(CurrentRow)
    #    CurrentContacts.append(CurrentRow[1])
    #else:
    #    CurrentContacts.append('OUTDATED ' + CurrentRow[1])

    #print FileToOpen

    count += 1

#for Entry in CurrentContacts:
#    outfile.write(Entry + '\n')

csvfile.close()
outfile.close()

print 'done'
print count