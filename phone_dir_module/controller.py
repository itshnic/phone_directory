import view
import model
import text

def start_up():
  view.print_message(text.text_items['welcome'])
  answer=0
  while text.command['Выход'] != answer:
    answer = view.panel(text.text_items['panel'],text.text_items['command'], text.command)
    model.cache_list = model.to_list(model.file, 'r')
    match answer:
      case '1': #Создать
       new_contact = model.add_user(text.text_items['user'], text.text_items['request'])
       model.cache_list.append(new_contact)
       model.to_file(model.file,model.cache_list,'w')
       view.print_message(f'{text.text_items["added"]}{new_contact[0]}')
      #case '2': #Изменить
        
      case _:
        view.print_message(text.text_items['error_command'])
        