#This stuff all works good
import FindLatestDate
import csv
import re

csvfile = open('../contactsJune6.csv', 'r')
outfile = open('CurrentContacts.csv', 'w')
ContactReader = csv.reader(csvfile, delimiter=',')
ContactWriter = csv.writer(outfile, delimiter=',')

#Skip through first header row
ContactWriter.writerow(ContactReader.next())
ContactReader.next()


#Check against what's currently in Salesforce Records
NOTRemoved = []

LookupFile = open('Contact IDs.csv', 'rU')
IDReader = csv.reader(LookupFile, delimiter=',')
for CurrentRow in IDReader:
    NOTRemoved.append(CurrentRow[1] + ' ' + CurrentRow[2])
LookupFile.close()

LookupFile = open('Account IDs.csv', 'rU')
IDReader = csv.reader(LookupFile, delimiter=',')
for CurrentRow in IDReader:
    NOTRemoved.append(CurrentRow[2])
LookupFile.close()

#Check Salesforce Records against Email dates
count = 0
NOTcount = 0
CurrentContacts = []
for CurrentRow in ContactReader:
    #Find Client File
    victim = CurrentRow[1]
    victim = re.sub('[^0-9a-zA-Z ]+', '_', victim)

    if victim not in NOTRemoved:
        print victim
        NOTcount += 1
        continue

    FileToOpen = '../highrise-export/contacts/' + victim +'.txt'
    #print FileToOpen
    if int(FindLatestDate.FindLatestDate(FileToOpen)) >= 2010:
        count += 1
        ContactWriter.writerow(CurrentRow)

csvfile.close()
outfile.close()

print 'done'
print count
print NOTcount