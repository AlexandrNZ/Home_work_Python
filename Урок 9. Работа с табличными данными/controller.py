import view
import model
import text

def start():
    while True:
        choice = view.min_menu()
        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb = model.get_pd()
                view.print_contacts(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cansel_input)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                view.print_message(text.search_contact)
                
            case 6:
                pass
            case 7:
                pd = model.get_pd()
                index = view.input_index(text.index_del_contact, pb, text.load_error)
                name = model.del_contact(index)
                view.print_message(text.del_contact(name))
            case 8:
                break
    
