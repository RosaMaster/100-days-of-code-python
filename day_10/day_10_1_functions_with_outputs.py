# Functions with Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    #print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"


nome = str(input("Informe seu nome: "))
sobrenome = str(input("Informe seu sobrenome: "))

formated_string = format_name(nome, sobrenome)
print(formated_string)