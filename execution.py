import funcoesMedico
import funcoesPaciente
import funcoes

def menu():
    while True: 
        funcoes.slogan()

        print("1- ACESSAR MENU")
        print("2- SAIR MENU")

        user_op = input("O que gostaria de fazer? ")

        if user_op == "1": 
            print("\n")
            
            perfil = funcoes.perfil_usuario()

            if perfil == "medico":
                funcoesMedico.menuMedico()
                print("VOLTANDO AO MENU PRINCIPAL...")

            elif perfil == "paciente":
                funcoesPaciente.menuPaciente
                print("VOLTANDO AO MENU PRINCIPAL...")

        elif user_op == "2":
            print(50*"-")
            print("OBRIGADO(a) POR ACESSAR O MOMCARE!")
            print("VOLTE SEMPRE")
            print(50*"-")
            break
            

if __name__ == "__main__":
    menu()