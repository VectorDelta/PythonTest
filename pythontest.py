option = ''
def card_reader():
  while True:
    try:
      identifier_bool = str(input('is the card original?'))
      if identifier_bool.lower() == 'yes':
        print('Ok')
      elif identifier_bool.lower() == 'no':
        raise Exception('This card isn\'t original')
      else:
        print('invalid input, type yes or no')
    finally:
      pass
card_reader()
