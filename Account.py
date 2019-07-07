class Account:
    def __init__(self,amount):
        
        if amount<500:
            raise valueError("For Opening account must be greater than 500")
        self.total_amount=amount
        
    def deposit(self,amount):
        self.total_amount+=amount
        return f"Successfully Deposited. Your new balance is {self.total_amount}"
    
    def withdraw(self,amount):
        if self.total_amount-amount<500:
            raise ValueError("Insuffiecient Balance")
        if amount%500==0:
            self.total_amount-=amount
            return f"Your Remaining  balance is {self.total_amount}"
        raise ValueError("Amount must be multiple of 500")

        
    def enquiry(self):
        return f"Your Current Balance is: {self.total_amount}"

if __name__=='__main__':
    a = Account(500)
    while True:
        print("Choose One Of the Following")
        
        option = int(input())
        if option==1:
            print(a.enquiry())