tarefas = []
gui_principal = True

while gui_principal == True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1 - Adicionar tarefas")
    print("2 - Ver tarefas")
    print("3 - Sair")
    escolha1 = int(input("Faça sua escolha:" ))
    if escolha1 == 1:
        tarefas.append(input("Digite sua tarefa: "))
    elif escolha1 == 2:
        print(tarefas)
    else:
        gui_principal = False
