from MyEnum import TTEnum;
"""
Transaction class is used for storing single transaction.
"""
class Transaction:
    """
    Header Names
    """
    TransTypeName = {
        TTEnum.SNO: 'Sno',
        TTEnum.Date: 'Date',
        TTEnum.TransType: 'TransType',
        TTEnum.Narration: 'Narration',
        TTEnum.Refno: 'Reference number',
        TTEnum.ValueDate: 'Value Date',
        TTEnum.Withdrawal: 'Withdrawal',
        TTEnum.Deposit: 'Deposit',
        TTEnum.ClosingBalance: 'Closing Balance'
        };

    """
    Name of Transaction Map File
    """
    #ttMapFName = "TransactionMap.txt";
    transTypeMap = [];
    accountTypeMap = [];
    """
    This function is used for determining Transaction Type using TransactionMap file.
    """
    def DetermineType(self, typeMap, selfVal, matchWith):
        transTypeMap = typeMap;
        retVal = '';
        if (transTypeMap == None):
            return retVal;
        for i in range(len(transTypeMap)):
            if ((selfVal == '' and transTypeMap[i][0].lower() in matchWith.lower()) or
                transTypeMap[i][0].lower() in selfVal.lower()):
                retVal = transTypeMap[i][1];
        return retVal;

    """
    This function is used for populating TransactionTypeMap using Transaction MAP Text file.
    """
    @staticmethod
    def Parse(fName):
        try:
            fob = open(fName, "r");
        except IOError:
            return;
        lines = fob.readlines();
        fob.close();
        lines = [e.replace('\n', '') for e in lines];
        lines = [e.split(',') for e in lines];
        return lines;
    @staticmethod
    def PopulateMap(ttMapFName, atMapFName):
        if (ttMapFName.strip() != '' and len(Transaction.transTypeMap) == 0):
            Transaction.transTypeMap = Transaction.Parse(ttMapFName);
        if (atMapFName.strip() != '' and len(Transaction.accountTypeMap) == 0):
            Transaction.accountTypeMap = Transaction.Parse(atMapFName);


    """
    Constructor for storing values
    """
    def __init__(self, sno, date, transtype, narration, refno, valuedate, withdrawal, deposit, closingbalance, action, account, price):
        self.value = {};
        self.value[TTEnum.SNO] = sno;
        self.value[TTEnum.Date] = date.replace('/','-');
        self.value[TTEnum.TransType] = transtype;
        self.value[TTEnum.Narration] = narration;
        self.value[TTEnum.Refno] = refno;
        self.value[TTEnum.ValueDate] = valuedate.replace('/', '-');
        self.value[TTEnum.Withdrawal] = withdrawal;
        self.value[TTEnum.Deposit] = deposit;
        self.value[TTEnum.ClosingBalance] = closingbalance;
        self.value[TTEnum.Action] = action;
        self.value[TTEnum.Account] = account;
        self.value[TTEnum.Price] = price;
        #self.PopulateTTMap();
        self.updated = 0;
        self.value[TTEnum.TransType] = self.DetermineType(Transaction.transTypeMap, transtype, narration);
        if (self.value[TTEnum.TransType].strip() != ''):
            self.updated = 1;
        self.value[TTEnum.Account] = self.DetermineType(Transaction.accountTypeMap, account, account);
        if (self.value[TTEnum.Account].strip() != ''):
            self.updated = 1;

