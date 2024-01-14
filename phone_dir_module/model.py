import os
file='phone_dir.txt'
cache_list = []
SEPARATOR=';'

def add_user(list_request: list, text_request: str) ->list:
  new_contact=[]
  for i in list_request:
    new_contact.append(checkNull(input(f'Введите {i}: ')))
  return new_contact
  

def to_list(file, flag):
  base_data = []
  if os.path.isfile(file):
    with open(file, flag,encoding='utf-8') as data:
      for line in data:
        base_data.append(line.split(SEPARATOR))
      print(base_data)
  return base_data

def to_file(file, cache_list, flag):
  with open(file, flag, encoding='utf-8') as data:
    for i in cache_list:
      data.write(f'{" ".join(i)}\n')
  data.close()
  
def checkNull(item):
  if item:
    return item
  else:
    return 'Null'

def search(list):
  index_true = []
  for i in range(len(list)):
      if list[i][0]==name:
        index_true.append(i)
  return index_true