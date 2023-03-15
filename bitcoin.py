import requests

def main():
  bitcoin = get_bitcoin_amount()
  dollar_value = get_us_dollar_bitcoin_value()
  converted = convert_dollars_to_bitcoin(bitcoin, dollar_value)
  display_result(bitcoin, converted)

def get_bitcoin_amount():
  bitcoin = float(input('Enter the number of bitcon: '))
  return bitcoin

def get_us_dollar_bitcoin_value():
  url = 'https://claraj.github.io/mock-bitcoin/currentprice.json'
  response = requests.get(url)
  data = response.json()
  dollar_value = data['bpi']['USD']['rate_float']
  return dollar_value

def convert_dollars_to_bitcoin(bitcoin, dollars):
   bitcoin_value_in_dollars = bitcoin * dollars
   return bitcoin_value_in_dollars

def display_result(bitcoin, converted):
   print(f'{bitcoin:0.2f} Bitcoin is equivalent to ${converted:0.2f}')


if __name__ == '__main__':
    main()