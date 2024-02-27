def get_usd():
  while True:
    try:
      usd=float(input("Enter the dollar amount you wish to convert: "))
      if usd<=0:
        print("Entry must be greater than 0")
      else:
        return usd 
    except ValueError:
        print("You did not enter a number")

def get_currency():
  while True:
    currency=input("Enter the desired currency (GBP for Pounds, EUR for Euro, or CNY for Yuan):") #.upper()
    if currency in ['GBP','EUR','CNY']:
      return currency
    else:
      print ("You did not enter a valid currency type")

def usd_to_gbp(usd):
  return usd * 0.77

def usd_to_eur(usd):
  return usd * 0.92

def usd_to_cny(usd):
  return usd * 6.98

def main():
  usd = get_usd()
  currency = get_currency()

  if currency == 'GBP':
    converted_amount = usd_to_gbp(usd)
    currency_name = "GBP"
  elif currency == 'EUR':
    converted_amount = usd_to_eur(usd)
    currency_name = "Euro"
  elif currency == 'CNY':
    converted_amount = usd_to_cny(usd)
    currency_name = "Yuan"


  print (f"${usd} in {currency_name} is {converted_amount}.")

if __name__== "__main__":
  main()
