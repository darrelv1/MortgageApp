from abc import abstractmethod
from Account import InvestorAccount

import pandas as pd
import numpy as np


class Profile():

    def __init__(self):
        pass


    @abstractmethod
    def showAccount(self):
        pass


class BarberOwner(Profile):
    def __init__(self, name):
        super.__init__()
        self.name = name

class Investor(Profile):
    def __init__(self, name, rate):
        super.__init__()
        self.name = name
        self.account = InvestorAccount(name, rate)
        self._balance = 0.00

    @property
    def balance(self):
        return self.account.balance

