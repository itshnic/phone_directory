import text

def print_message(message:str):
  print('\n'+'-'*(len(message)+2))
  print(f' {message}')
  print('-'*(len(message)+2))

def max_len_item_dict(dict_txt)->list:
  return [len(max(dict_txt.keys(),key=len)),len(max(dict_txt.values(),key=len))]
  
def max_len_item_list(dict_txt)->list:
  return [len(max(dict_txt.keys(),key=len)),len(max(dict_txt.values(),key=len))]

def panel(text_1,text_2,dict_txt):
  print_message(text_1)
  max_size=max_len_item_dict(dict_txt)
  for i,f in dict_txt.items():
    print(f'  {i:<{max_size[0]}} -> {f}')
  return input(f'\n{text_2} ')

  
