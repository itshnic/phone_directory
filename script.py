import os
command = {
	'Создать': 1,
	'Изменить': 2,
 	'Найти': 3,
  'Показать_все': 4,
  'Удалить': 5,
  'Копировать': 6,
  'Выход': 9
}
data_name = ['имя','телефон','комментарии']

def panel(text_1,text_2,list):
  print(text_1)
  for i,f in list.items():
    print(f' {i}: {f}')
  return input(text_2)

def checkNull(item):
  if item:
    return item
  else:
    return 'Null'

def to_list(file, flag):
  base_data = []
  if os.path.isfile(file):
    with open(file, flag) as data:
      for line in data:
        base_data.append(line.split())
  return base_data

def to_file(file, list, flag):
  with open(file, flag) as data:
    for i in list:
      data.write(f'{" ".join(i)}\n')
  data.close()
  
def search(list):
  name=input('Введите имя для поиска: ')
  index_true = []
  for i in range(len(list)):
      if list[i][0]==name:
        index_true.append(i)
  return index_true
          
def processor(command):
  print('Добро пожаловать в телефонный справочник!')
  answer=0
  while command['Выход'] != int(answer):
    answer = panel('Панель управления:','Введите команду -> ', command)
    list_all = to_list('phone.txt', 'r')
    if command['Создать'] == int(answer):
      new_contact=[]
      for i in data_name:
        new_contact.append(checkNull(input(f'Введите {i}: ')))
      print()
      list_all.append(new_contact)
      to_file('phone.txt',list_all, 'w')
      
    elif command['Показать_все']==int(answer):
      print('Имя  | Телефон | Комментарии |')
      for item in to_list('phone.txt', 'r'):
        for k in item:
          print(k, end=' | ' )
        print()
      print()  
    elif command['Найти']==int(answer):
      index_true = search(list_all)
      if len(index_true):
        print('Имя  | Телефон | Комментарии |')
        for i in index_true:
          for k in list_all[i]:
            print(k, end=' | ')
          print() 
      else:
        print('Нет такой записи(')
      print()
      
    elif command['Изменить']==int(answer):
      index_true = search(list_all)
      if len(index_true):
        for i in index_true:
          for k in range(len(list_all[i])):
            print(f'{data_name[k]} -> {list_all[i][k]}')
            list_all[i][k]=checkNull(input('Меняем на -> '))
        print('Имя  | Телефон | Комментарии |')
        for i in index_true:
          for k in list_all[i]:
            print(k, end=' | ')
          print()
        to_file('phone.txt',list_all, 'w')  
      else:
        print('Нет такой записи(')
      print()
      
    elif command['Копировать']==int(answer):
      index_true = search(list_all)
      if len(index_true):
        copy_list=to_list('copy_contact.txt', 'r')
        for i in index_true:
          copy_list.append(list_all[i])
        to_file('copy_contact.txt',copy_list, 'w')     
      else:
        print('Нет такой записи(')
      print() 
    elif command['Удалить']==int(answer):
      index_true = search(list_all)
      if len(index_true):
        for i in reversed(index_true):
          list_all.pop(i)
        to_file('phone.txt',list_all, 'w')
      else:
        print('Нет такой записи(')
      print()
      
					
processor(command)      
