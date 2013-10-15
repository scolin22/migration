#This stuff all works good
import FindLatestDate
import csv
import copy
import re

csvfile = open('CurrentContacts.csv', 'rU')
outfile = open('Emails.csv', 'wb')
ContactReader = csv.reader(csvfile, delimiter=',')

#Skip through first header row
ContactReader.next()

#Write down the header information
EmailIDs = []
AllEmails = []
for CurrentRow in ContactReader:
    #Find Client File
    victim = CurrentRow[1]
    victim = re.sub('[^0-9a-zA-Z ]+', '_', victim)

    FileToOpen = '../highrise-export/contacts/' + victim +'.txt'
    FoundEmail = []
    FoundEmail = FindLatestDate.TakeEmailInfo(FileToOpen)

    print CurrentRow[1]

    CopyFoundEmail = copy.deepcopy(FoundEmail)
    for key, value in FoundEmail.iteritems():
        if key in EmailIDs:
            del CopyFoundEmail[key]
        else:
            EmailIDs.append(key)
    FoundEmail = copy.deepcopy(CopyFoundEmail)

    AllEmails.append(FoundEmail)

#Output List in a csv format
fieldnames = ['Priority', 'Status', 'Subject', 'Due Date Only', 'Description', 'Assigned to ID', 'Opportunity/Account ID', 'Contact/Lead ID', 'Account ID', 'EmailID']
ContactWriter = csv.DictWriter(outfile, delimiter=',', fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
ContactWriter.writerow(dict((fn,fn) for fn in fieldnames))
for batchemail in AllEmails:
    for key, value in batchemail.iteritems():
        ContactWriter.writerow(value)

csvfile.close()
outfile.close()

print 'done'