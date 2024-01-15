import os
file='phone_dir.txt'
cache_list = []
SEPARATOR=';'

def to_list(file:str, flag:str,hat:list):
  if os.path.isfile(file):
    with open(file, flag,encoding='utf-8') as data:
      base_data={i:item for i, item in enumerate(list(map(lambda x: x.strip().split(SEPARATOR), data)),1)}
      print(base_data)
      return base_data

def to_file(file, cache_list, flag):
  with open(file, flag, encoding='utf-8') as data:
    for i in cache_list:
      data.write(f'{SEPARATOR.join(i)}\n')
  data.close()

def search(list):
  index_true = []
  for i in range(len(list)):
      if list[i][0]==name:
        index_true.append(i)
  return index_true