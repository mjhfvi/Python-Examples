import json
file_name = "D:\\LocalComputerList.json"

def json_read():
    json_file = open(file_name, 'r')
    json_object = json.load(json_file)
    json_file.close()
    return json_object

def json_write(dict):
    json_file = open(file_name, "w")
    json.dump(dict, json_file, indent=4)
    json_file.close()

def input_data():
    # host_input = input('Enter Host Name: ')
    ip_input = input('Enter IP Address:  ')
    # user_input = input('Enter User Name:  ')
    # password_input = input('Enter User Password:  ')
    return ip_input

def get_dictionary_values(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            get_dictionary_values(value)
        else:
            print(key, ":", value)

json_data = json_read()
get_dictionary_values(json_data)
