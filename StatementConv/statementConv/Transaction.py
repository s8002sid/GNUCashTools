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

    """
    This function is used for determining Transaction Type using TransactionMap file.
    """
    def DetermineTranstype(self):
        transTypeMap = self.transTypeMap;
        for i in range(len(transTypeMap)):
            if ((self.value[TTEnum.TransType] == '' and transTypeMap[i][0].lower() in self.value[TTEnum.Narration].lower()) or
                transTypeMap[i][0].lower() in self.value[TTEnum.TransType].lower()):
                self.value[TTEnum.TransType] = transTypeMap[i][1];
                self.updated = 1;

    """
    This function is used for populating TransactionTypeMap using Transaction MAP Text file.
    """
    @staticmethod
    def PopulateTTMap(ttMapFName):
        if (len(Transaction.transTypeMap) == 0):
            try:
                fob = open(ttMapFName, "r");
            except IOError:
                return;
            lines = fob.readlines();
            fob.close();
            lines = [e.replace('\n', '') for e in lines];
            lines = [e.split(',') for e in lines];
            Transaction.transTypeMap = lines;

    """
    Constructor for storing values
    """
    def __init__(self, sno, date, transtype, narration, refno, valuedate, withdrawal, deposit, closingbalance):
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
        #self.PopulateTTMap();
        self.updated = 0;
        self.DetermineTranstype();
