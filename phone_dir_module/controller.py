import view
import model
import text

def start_up():
  view.print_message(text.text_items['welcome'])
  answer=0
  while text.command['Выход'] != answer:
    answer = view.panel(text.text_items['panel'],text.text_items['command'], text.command) 
    model.cache_list=model.to_list(model.file, 'r')
    match answer:
      case '1': #Создать
        new_contact = view.add_user(text.text_items['user'], text.text_items['request'])
        model.cache_list.append(new_contact)
        model.to_file(model.file,model.cache_list,'w')
        view.print_message(f'{text.text_items["added"]}{new_contact[0]}')
      case '2': #Изменить
        item_true=model.search(model.cache_list, view.search(text.text_items['search_text']))
        print(item_true)
        view.show_all(item_true[1], text.text_items['user'],text.text_items['error_search'])
        view.change_record(item_true[0],model.cache_list,text.text_items['user'])
        model.to_file(model.file,model.cache_list,'w')
      case '3': #Найти
        item_true=model.search(model.cache_list, view.search(text.text_items['search_text']))
        view.show_all(item_true[1], text.text_items['user'],text.text_items['error_search'])
      case '4': #Показать_все
        view.show_all(model.cache_list, text.text_items['user'],text.text_items['error_search'])
      case '5': #Удалить
        item_true=model.search(model.cache_list, view.search(text.text_items['search_text']))
        view.show_all(item_true[1], text.text_items['user'],text.text_items['error_search'])
        delete_item=model.delete(item_true[0],model.cache_list,view.search(text.text_items['delete_request']))
        model.to_file(model.file,model.cache_list,'w')
        if len(delete_item):
          view.print_message(f'{text.text_items['delete_info']}{delete_item[0]}')
        else:
          view.print_message(text.text_items['error_search_id'])
      case '9': #Выход
        view.print_message(text.text_items['exit'])
      case _:
        view.print_message(text.text_items['error_command'])
        