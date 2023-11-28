def slogan():
    print(55*'-')
    print ("BEM-VINDA AO MOM CARE\nPensado e desenvolvido para todas as mães!")
    print(55*'-')




def perfil_usuario():

    perfil = ''

    print("QUAL O SEU PERFIL?")
    print("1- MÉDICO")
    print("2- PACIENTE")

    user_op = input("Digite sua opção: ")
    
    if user_op == "1":
        perfil = "medico"

    elif user_op == "2":
        perfil = "paciente"

    return perfil 