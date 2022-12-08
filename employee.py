"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    def __init__(self, name, contract, commission = None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        totalPay = 0

        if self.getContract() == 'salary':
            totalPay += self.getSalaryContractPay()
        elif self.getContract() == 'hourly':
            totalPay += self.getHourlyContractPay()

        if self.commission == None:
            return totalPay

        if self.getCommission() == 'contract':
            totalPay += self.getContractPay()
        elif self.getCommission() == 'bonus':
            totalPay += self.getBonusPay()

        return totalPay

    def __str__(self):
        return f'{self.getName()} works on a {self.print_contract_details()}{self.print_commission_details()}. Their total pay is {self.get_pay()}.'

    def getName(self):
        return self.name

    def getContract(self):
        return self.contract[0]


    def getSalaryContractPay(self):
        return self.contract[1]

    def getHourlyContractPay(self):
        hoursWorked = self.contract[1]
        amountPaid = self.contract[2]
        return hoursWorked * amountPaid

    def getCommission(self):
        return self.commission[0]


    def getContractPay(self):
        contracts = self.commission[1]
        rate = self.commission[2]
        return contracts * rate

    def getBonusPay(self):
        return self.commission[1]

    def print_contract_details(self):
        if self.getContract() == 'salary':
            return f'monthly salary of {self.contract[1]}'
        elif self.getContract() == 'hourly':
            return f'contract of {self.contract[1]} hours at {self.contract[2]}/hour'

    def print_commission_details(self):
        if self.commission == None:
            return ""

        if self.getCommission() == 'contract':
            return f' and receives a commission for {self.commission[1]} contract(s) at {self.commission[2]}/contract'
        elif self.getCommission() == 'bonus':
            return f' and receives a bonus commission of {self.commission[1]}'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', ['salary', 4000])

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', ['hourly', 100, 25])

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', ['salary', 3000], ['contract', 4, 200])

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', ['hourly', 150, 25], ['contract', 3, 220])

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', ['salary', 2000], ['bonus', 1500])

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', ['hourly', 120, 30], ['bonus', 600])
