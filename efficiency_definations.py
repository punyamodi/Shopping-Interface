from prettytable import PrettyTable as PT

def print_table(tuple_array, fieldname_array):
    table = PT()
    table.field_names = fieldname_array
    for items in tuple_array:
        table.add_row(items)
    print(table)
