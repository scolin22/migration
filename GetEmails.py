#This stuff all works good
import FindLatestDate
import csv
import copy
import re

csvfile = open('CurrentContacts.csv', 'rU')
ContactReader = csv.reader(csvfile, dialect='excel', delimiter=',')

#Skip through first header row
ContactReader.next()

#Write down the header information
EmailIDs = []
AllEmails = []
IgnoredEmails = ['17029392', '16658864', '16995266', '21208201', '21204144', '33273510', '141965358', '24219923', '29854070', '13998396']
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
        if key in EmailIDs or key in IgnoredEmails:
            del CopyFoundEmail[key]
        else:
            EmailIDs.append(key)
    FoundEmail = copy.deepcopy(CopyFoundEmail)

    AllEmails.append(FoundEmail)

#Output List in a csv format
outfile = open('Emails.csv', 'wb')
fieldnames = ['Priority', 'Status', 'Subject', 'Due Date Only', 'Description', 'Assigned to ID', 'Opportunity/Account ID', 'Contact/Lead ID', 'Account ID'] #, 'EmailID']
#ContactWriter = csv.DictWriter(outfile, delimiter=',', fieldnames=fieldnames, quoting=csv.QUOTE_ALL, dialect='excel')
ContactWriter = csv.DictWriter(outfile, fieldnames=fieldnames, dialect='excel', extrasaction='ignore')

ContactWriter.writerow(dict((fn,fn) for fn in fieldnames))
for batchemail in AllEmails:
    for key, value in batchemail.iteritems():
        ContactWriter.writerow(value)

csvfile.close()
outfile.close()

print 'done'