import os
file='phone_dir.txt'
cache_list = []
SEPARATOR=';'

def to_list(file:str, flag:str):
  base_data=[]
  if os.path.isfile(file):
    with open(file, flag,encoding='utf-8') as data:
      base_data=[i for i in list(map(lambda x: x.strip().split(SEPARATOR), data))]
  return base_data

def to_file(file, cache_list, flag):
  with open(file, flag, encoding='utf-8') as data:
    for i in cache_list:
      data.write(f'{SEPARATOR.join(i)}\n')
  data.close()

def search(cache_list,word):
  item_true = []
  for i in range(len(cache_list)):
      if word.lower() in ' '.join(cache_list[i]).lower():
        item_true.append(cache_list[i])
  return item_true