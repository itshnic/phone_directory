import text

def print_message(message:str):
  print('\n'+'-'*(len(message)+2))
  print(f' {message}')
  print('-'*(len(message)+2))

def max_len_item_dict(list_txt)->list:
  if type(list_txt.values())==list:
    return [map(lambda x:len(max(x, key=len)),list(zip(*list_txt.values())))]
  else:
    return [len(max(list_txt.keys(),key=len)),len(max(list_txt.values(),key=len))]
  
  
def panel(text_1,text_2,dict_txt):
  print_message(text_1)
  max_size=max_len_item_dict(dict_txt)
  for i,f in dict_txt.items():
    print(f'  {i:<{max_size[0]}} -> {f}')
  return input(f'\n{text_2} ')

def checkNull(item):
  if item:
    return item
  else:
    return 'Null'

def add_user(list_request: list, text_request: str) ->list:
  new_contact=[]
  for user_info in list_request:
    new_contact.append(checkNull(input(f'{text_request} {user_info}: ')))
  return new_contact

def input_request(user_info, text_request):
  input(f'{text_request} {user_info}: ')
