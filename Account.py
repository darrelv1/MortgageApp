import pandas as pd
import numpy as np
from Profiles import Investor
import functools
import itertools


class Account:
    def __init__(self):
        self._table = pd.DataFrame(columns=['Date'
                                          ,'Debit'
                                          ,'Credit'
                                          ,'Balance',
                                           'Description'])
        self.tableLength = len(self._table.index)
        self._balance = 0.00

    @property
    def table(self):
        return self._table

    @property
    def balance(self):
        return self._balance

    @table.setter
    def table(self, row):

        # try:
        if len(row) == (len(self._table.columns) - 2):
            """
            Adjusting the row
            """
            prevBal = self._table.loc[len(self._table.index) - 1, "Balance"] if len(self._table.index) != 0 else 0.00
            futureBal = prevBal + row[1]
            row.insert(2, 0.00) if row[1] > 0.00 else row.insert(1, 0.00)
            row.insert(3, futureBal)

            """
            Adding the row
            """
            self._table.loc[len(self._table.index)] = row
            self._balance = self.table.loc[self.tableLength, "balance"]
        else:
            print("Array must have 5 items, Date, Debit, Credit, Balance and a Description!")
        # except TypeError:
        #     print("Must be an List or Array type")
        # except:
        #     print("Something else went wrong please review the Call Stack")

    @table.deleter
    def table(self):
        del self._table

    def deleteRow(self, index):
        self._table.drop(index)



class InvestorAccount(Account):
    def __init__(self, name, rate):
        self.investor = name
        self.ownership = rate
        super().__init__()


"""
All Transactions will be posted here
This obj will action the transacton split
"""
class GeneralLedger(Account):
    def __init__(self):
        super().__init__()
        self.identity = "General Ledger Account for all Inventory"
        self.investors = []

    def addInvestors(self,*args):
        for name, rate in args:
            investor = Investor(name, rate)
            self.investors.append(investor)

    def postEntry(self, entry):
        self.table = entry

    @classmethod
    def split(cls, entry, rate):
        amount = entry[1]
        return amount * rate

    def postSplit(self, entry):
        #modify the amount to match the split and give everyone their share
        map(lambda inv : ()inv.account.table = [entry[0], self.split(entry, inv.account.ownership),entry[2]],self.investors)




