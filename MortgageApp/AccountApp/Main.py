from .models import Ledgers
def add():
    come = Ledgers(date="2022-12-22", debit=150, credit=105, balance=1200, description="dummy")
    come.save()
    Ledgers.objects.create(date="2022-12-22", debit=150, credit=105, balance=1200, description="dummy")
    print("hello")



