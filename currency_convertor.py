def get_amount():
    while True:
        try:
            amount=float(input('Enter amount: '))
            
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amount , please try again!!!')
            
             
def get_currency(label):    
    currencies= ('UGX','USD','EUR')
    while True:
        currency = input(f'Enter {label} currency(UGX/USD/EUR): ').upper() 
        if currency not in currencies:
            print("invalid currency ,please try again!!!")
        else:
            return currency
        
def convert_currency(amount,source_currency,Target_currency):
    exchange_rates ={
    'UGX' : {'USD': 1.20,'EUR': 0.50},
    'USD' : {'UGX': 2.40,'USD': 1.75},
    'EUR' : {'UGX': 3.21,'USD' :1.29}
    }

    if source_currency == Target_currency:
        return  amount  
    else:    
        return amount*exchange_rates[source_currency][Target_currency]

def main():    
    amount=get_amount()
    source_currency=get_currency('source')
    Target_currency=get_currency('Target')
    converted_amount=convert_currency(amount,source_currency,Target_currency)
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {Target_currency}')
    
    
if __name__ == '__main__':
    main()