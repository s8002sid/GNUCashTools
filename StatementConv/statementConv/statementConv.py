from MyEnum import TTEnum;
from Statement import Statement;
from Statement import HDFCEditedStatementParser;
from Statement import HDFCStatementParser;
import re;
inputFile=r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\HDFC\Sid\2014-2015.csv';
#outputFile=r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\HDFC\Sid\2014-2015-edited.csv';
outputFile=r'output\2014-2015-edited.csv'
fob = open(inputFile, "r");
lines = fob.readlines();
fob.close();
p=re.compile ('[^"]*("[^"^,]*,?[^"]*")*[^"]*');
for i in range(len(lines)):
    m=p.findall(lines[i]);
    for j in range(len(m)):
        if(m[j] != ''):
            m1=m[j].replace('"','').replace(',',' ');
            lines[i] = lines[i].replace(m[j],m1);
del lines[0];
parser = HDFCEditedStatementParser();
statement=Statement(lines, parser);
strStatement = statement.ToStringList();
#strStatement = statement.NotUpdatedTransTypeStringList();
fob = open (outputFile, "w");
fob.write("\n".join(strStatement));
fob.close();
