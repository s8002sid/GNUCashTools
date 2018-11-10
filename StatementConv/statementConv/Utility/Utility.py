from datetime import datetime, timedelta;
class Utility:
    @staticmethod
    def NumberToCurrency(number):
        numStr = str(number);
        numStrSplit = numStr.split('.');
        if (len(numStrSplit) == 1):
            numStrSplit.append('00');
        curPos = 0;
        strLen = len(numStrSplit[0]);

        for i in range(int(strLen/3)):
            strLen = len(numStrSplit[0]);
            if (strLen - curPos > 3):
                curPos += 3;
                numStrSplit[0] = numStrSplit[0][:(strLen - curPos)] + ',' +  numStrSplit[0][(strLen-curPos):]
                curPos+=1;
        return numStrSplit[0] + '.' + numStrSplit[1];
    @staticmethod
    def WriteStatement(statementExporter, outputFile):
        strStatement = statementExporter.ToString();
        fob = open(outputFile, "w");
        fob.write("\n".join(strStatement));
        fob.close();

    @staticmethod
    def GetDate(dateStr):
        if ("/" in dateStr):
            return dateStr.replace("/", "-");
        startDate=datetime(1899,12,30);
        dateDelta = timedelta(int(dateStr.split('.')[0]));
        date = startDate + dateDelta;
        return date.strftime('%m-%d-%Y');#We will consider final emitted date in fromat dd-mm-yyyy
