def FindLatestDate(FileToOpen):
    try:
        InputFile = open(FileToOpen)
        DatesList = []
        for line in InputFile:
            if line.startswith('    Written:'):
                entry = line[line.index(',') + 1:line.index(',') + 6]
                DatesList.append(entry)
        InputFile.close()
        if DatesList:
            return max(DatesList)
        else:
            return 0
    except IOError:
        print 'Not Found' + FileToOpen
        return 0

def TakeEmailInfo(FileToOpen):
    try:
        InputFile = open(FileToOpen)
        AllEmails = {}
        company = '0'
        for line in InputFile:
            Email = {}
            if line.startswith('- Company'):
                line = InputFile.next()
                line = InputFile.next()
                company = line[8:].rstrip('\r\n')
            if line.startswith('- Email'):
                id = line[8:-4]
                line = InputFile.next()
                line = InputFile.next()
                if line.startswith('    Author:'):
                    #Email['Assigned to ID'] = line[12:]
                    #Email['Assigned to ID'] = Email['Assigned to ID'].rstrip('\r\n')
                    #if Email['Assigned to ID'] == 'Glenn H.':
                    #    Email['Assigned to ID'] = 'Glenn Hilton'
                    #    Email['Account ID'] = '005i0000001iROX'
                    #else:
                    #    Email['Assigned to ID'] = 'Jennifer Hols'
                    #    Email['Account ID'] = '005i0000000KkkG'
                    Email['Assigned to ID'] = 'Jennifer Hols'
                    #Email['Account ID'] = '005i0000000KkkG'
                    Email['Account ID'] = 'Jennifer Hols'
                    line = InputFile.next()
                    line = InputFile.next()
                if line.startswith('    Written:'):
                    Email['Due Date Only'] = line[14:-9]
                    Email['Due Date Only'] = Email['Due Date Only'].rstrip('\r\n')
                    line = InputFile.next()
                    line = InputFile.next()
                if line.startswith('    About:'):
                    Email['Contact/Lead ID'] = line[11:]
                    Email['Contact/Lead ID'] = Email['Contact/Lead ID'].rstrip('\r\n')
                    #Email['Contact/Lead ID'] = FindSalesforceContactID(Email['Contact/Lead ID'])
                    line = InputFile.next()
                    line = InputFile.next()
                if line.startswith('    Subject:'):
                    Email['Subject'] = line[13:]
                    Email['Subject'] = Email['Subject'].rstrip('\r\n')
                    line = InputFile.next()
                    line = InputFile.next()
                Email['Priority'] = 'Normal'
                Email['Status'] = 'Complete'

                target = FileToOpen.lstrip('../highrise-export/contacts/')
                target = target.rstrip('.txt')
                Email['Opportunity/Account ID'] = target;
                #if company == '0':
                #    target = FileToOpen.lstrip('../highrise-export/contacts/')
                #    #target = target.rstrip('.txt')
                #    target = target[:-4]
                #    Email['Opportunity/Account ID'] = FindSalesforceAccountID(target)
                #else:
                #    Email['Opportunity/Account ID'] = FindSalesforceAccountID(company)

                #Email['EmailID'] = id
                if line.startswith('    Body:'):
                    line = InputFile.next()
                    Email['Description'] = ''
                    while line.startswith('      '):
                        line = line.lstrip('      ')
                        line = line.rstrip('\r\n')
                        Email['Description'] += line
                        AllEmails[id] = Email
                        line = InputFile.next()

        InputFile.close()
    except IOError:
        return 0
    finally:
        return AllEmails

import csv
def FindSalesforceAccountID(Name):
    SalesforceID = '0'
    LookupFile = open('Account IDs.csv', 'rU')
    IDReader = csv.reader(LookupFile, delimiter=',')
    for CurrentRow in IDReader:
        if CurrentRow[2] == Name:
            SalesforceID = CurrentRow[0]
            break
    return SalesforceID

def FindSalesforceContactID(Name):
    SalesforceID = '0'
    LookupFile = open('Contact IDs.csv', 'rU')
    IDReader = csv.reader(LookupFile, delimiter=',')
    for CurrentRow in IDReader:
        if CurrentRow[1] + ' ' + CurrentRow[2] == Name:
            SalesforceID = CurrentRow[0]
            break
    return SalesforceID