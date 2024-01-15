import text

def print_message(message:str):
  print('\n'+'-'*(len(message)+2))
  print(f' {message}')
  print('-'*(len(message)+2))
  
def panel(text_1,text_2,dict_txt):
  print_message(text_1)
  max_size=[len(max(dict_txt.keys(),key=len)),len(max(dict_txt.values(),key=len))]
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

def show_all(cache_list, list_request):
  cache_list.insert(0,list_request)
  max_size=[]
  for i in range(len(cache_list[0])):
    max_item=[]
    for j in range(len(cache_list)):
      max_item.append(cache_list[j][i])
    max_size.append(len(max(max_item, key=len)))
  for i in range(len(cache_list)):
    if i==0:
      print_message(f'   {cache_list[i][0]:<{max_size[0]+2}}{cache_list[i][1]:<{max_size[1]+2}}{cache_list[i][2]:<{max_size[2]+2}}')
    else:
      print(f' {i}. {cache_list[i][0]:<{max_size[0]+2}}{cache_list[i][1]:<{max_size[1]+2}}{cache_list[i][2]:<{max_size[2]+2}}')
      
def exit(text):
  print_message(text)
  
def search(search_text):
  return input(search_text)
