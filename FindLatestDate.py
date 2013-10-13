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
        return 0