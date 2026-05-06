name='Gowreesan'
def generate_sequence(name):
    name = name.upper()
    name =name.strip()
    for i in name:
        print('**** ' + i + ' ****')      

generate_sequence(name)
input_name = input("Enter a name: ")
generate_sequence(input_name)