def validar_entrada_cpf():
    """Garante que a entrada do usuário tenha 11 dígitos numéricos."""
    while True:
        cpf = input("Digite o CPF (apenas 11 números): ")
        if len(cpf) == 11 and cpf.isdigit():
            print("Entrada validada com sucesso.")
            return cpf
        elif len(cpf) != 11:
            print(f"ERRO: O CPF deve ter 11 dígitos. Você digitou {len(cpf)}.")
        else:
            print("ERRO: O CPF deve conter apenas números.")

def calcular_dv1(cpf):
    """Calcula o primeiro Dígito Verificador (DV1)."""
    nove_digitos = cpf[:9]
    soma_ponderada = 0

    for indice, digito_str in enumerate(nove_digitos):
        peso = 10 - indice
        digito = int(digito_str)
        soma_ponderada += (digito * peso)

    resto = soma_ponderada % 11 

    if resto < 2:
        return 0
    else:
        return 11 - resto

def calcular_dv2(cpf, dv1_calculado):
    """Calcula o segundo Dígito Verificador (DV2) usando o DV1 calculado."""
    dv1_str = str(dv1_calculado)
    dez_digitos = cpf[:9] + dv1_str # 10 dígitos (D1...D9 + DV1)

    soma_ponderada = 0
    
    # O peso agora vai de 11 a 2
    for indice, digito_str in enumerate(dez_digitos):
        peso = 11 - indice
        digito = int(digito_str)
        soma_ponderada += (digito * peso)

    # Regra do DV2: módulo 11
    resto2 = soma_ponderada % 11
    
    if resto2 < 2:
        return 0
    else:
        return 11 - resto2

# --- FUNÇÃO PRINCIPAL ---
def validar_cpf_completo():
    cpf_usuario = validar_entrada_cpf()
    
    # Evitar CPFs inválidos óbvios (ex: 11111111111)
    if len(set(cpf_usuario)) == 1:
        print("CPF inválido: Todos os dígitos são iguais.")
        return

    # 1. VERIFICAÇÃO DO DV1
    dv1_calculado = calcular_dv1(cpf_usuario)
    dv1_original = int(cpf_usuario[9]) 

    if dv1_calculado != dv1_original:
        print("STATUS: INVÁLIDO")
        print("Motivo: O primeiro dígito verificador está incorreto.")
        return

    # 2. VERIFICAÇÃO DO DV2
    dv2_calculado = calcular_dv2(cpf_usuario, dv1_calculado)
    dv2_original = int(cpf_usuario[10]) # O DV2 é o dígito no índice 10

    if dv2_calculado != dv2_original:
        print("STATUS: INVÁLIDO")
        print("Motivo: O segundo dígito verificador está incorreto.")
        return
        
    print("---------------------------------")
    print("STATUS: VÁLIDO")
    print(f"CPF: {cpf_usuario[:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}")
    print("Este CPF segue o algoritmo de validação da Receita Federal.")
    print("---------------------------------")

# EXECUÇÃO DO PROGRAMA
validar_cpf_completo()