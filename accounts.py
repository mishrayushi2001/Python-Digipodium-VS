class Account:

    def __init__(self, name, acc_no, branch, balance):
        self.name = name
        self.acc_no = acc_no
        self.branch = branch
        self.balance = balance

    def debit(self, amt):
        self.balance -= amt
        print(f"{amt} debited from {self.holder_name}'s account")

acc1 = Account("Mr.Neo Aneder son", 12456789, 'hazratganj', 2000)
acc2 = Account("Mrs.Neo Aneder son", 98754321, 'hazratganj', 5000)

acc1.debit(1500)
acc2.debit(3300)

print(acc1.balance)
print(acc2.balance)

   # def credit(self, amt):
       # self.balance += amt
      #  print(f"{amt}")
    