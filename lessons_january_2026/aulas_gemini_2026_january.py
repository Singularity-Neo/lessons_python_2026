"""

nota = int(input("Digite a nota final (0-100): "))

# 1. Primeiro: Vamos filtrar os erros (menor que 0 OU maior que 100)
if nota < 0 or nota > 100:
    print("Erro: Nota impossível! Digite entre 0 e 100.")

# 2. Agora vamos do maior para o menor (Ordem decrescente)
# Se for maior ou igual a 90...
elif nota >= 90:
    print("Nota A (Excelente) 🌟")

# 3. Se não foi A, verificamos se é B (maior ou igual a 70)
elif nota >= 70:
    print("Nota B (Bom) 👍")

# 4. Verificamos se é C (maior ou igual a 50)
elif nota >= 50:
    print("Nota C (Suficiente) 😐")

# 5. Se não é erro, nem A, nem B, nem C... só sobra o quê?
else:
    print("Nota F (Reprovado) ❌")

"""


"""    
# 1. Primeiro, nós CRIAMOS (Ensinamos o Python)
def dar_oi():
    print("Olá!")
    print("Seja bem-vindo ao sistema.")
    print("-------------------------")

# Até aqui, nada acontece. O Python só "aprendeu".

# 2. Agora, nós CHAMAMOS (Usamos o comando)
dar_oi()
"""

# A variável 'nome' aqui é um "espaço reservado"
"""nome = input("Digite seu nome: ")
def saudar(nome):
    print(f"Olá, {nome}!")
    print("Como você está?")

# Agora usamos com clientes diferentes
saudar("Jefferson")
saudar("Maria")
saudar("Carlos")"""


# Definindo a função
"""
numero = int(input("Digite um número para dobrar: "))
def dobrar(numero):
    resultado = numero * 2
    print(f"O dobro de {numero} é {resultado}")

# Agora, o programa principal:
print("--- Início do Programa ---")
"""
# Use a função 'dobrar' para calcular o dobro de 10, 50 e 123.
# 1. Pede o número e guarda na caixa 'numero'
 

"""
numero_digitado = int(input("Digite um número para dobrar: "))

def dobrar(valor_qualquer):
    resultado = valor_qualquer * 2
    print(f"O dobro é {resultado}")

print("--- Início do Programa ---")

# 2. O SEU ERRO ESTAVA AQUI:
# Você chamou com números fixos (10, 50).
# O jeito certo é pegar a variável lá de cima e jogar aqui dentro:
dobrar(numero_digitado)


vida = 100
def atacar(dano):
    resultado = dano - 15
    print(f"15 de dano recebido, HP: {resultado}")


atacar(vida) 
if vida == 0:
    print("Morreu!")
"""
  

# Função que SOMA dois números e RETORNA o resultado
"""
def somar(a, b):
    return a + b

# Olha que magia:
# O computador resolve 'somar(10, 10)' -> vira 20
# Depois resolve 'somar(5, 5)' -> vira 10
# Depois soma os dois resultados (20 + 10)
total = somar(10, 10) + somar(5, 5)

print("O total final é:", total) """


"""
def calcular_lucro(venda, custo):
    lucro = venda - custo
    return lucro  # Que palavra mágica vai aqui para DEVOLVER o valor?

# Venda 1: Vendi por 100, custou 50
lucro1 = calcular_lucro(100, 50) 

# Venda 2: Vendi por 200, custou 100
lucro2 = calcular_lucro(200, 100)

# Agora somamos os resultados que voltaram
total_dia = lucro1 + lucro2

print(f"Hoje lucrei: {total_dia} €")"""

"""

print("--- 🧮 CALCULADORA PRO 🧮 ---")

# --- ÁREA DAS FERRAMENTAS (FUNÇÕES) ---

def somar(a, b):
    return a + b

# 1. Complete a função de subtrair
def subtrair(a, b):
    return a - b

# 2. Complete a função de multiplicar
def multiplicar(a, b):
    return a * b  # O que falta para DEVOLVER o valor?

# 3. Crie a função de dividir do zero (seguindo o modelo das outras)
def dividir(a, b):
    return a / b  # (Dica: return a / b)
# --- PROGRAMA PRINCIPAL (O CHEFE) ---

while True:
    print("\nEscolha: 1.Somar | 2.Subtrair | 3.Multiplicar | 4.Dividir | 0.Sair")
    opcao = int(input("Opção: "))

    if opcao == 0:
        print("Calculadora desligada.")
        break # Sai do loop

    # Pedimos os números
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    # Agora o cérebro decide qual ferramenta usar
    if opcao == 1:
        resultado = somar(n1, n2)
    
    elif opcao == 2:
        # Chamamos a função subtrair enviando n1 e n2
        resultado = subtrair(n1, n2)

    elif opcao == 3:
        # 4. CHAME a função de multiplicar aqui
        resultado = multiplicar(n1, n2)

    elif opcao == 4:
        resultado = dividir(n1, n2)
    
    else:
        print("Opção inválida!")
        continue # Pula para o início do loop e ignora o print abaixo

    # Mostra o resultado final que veio do 'return'
    print(f"O resultado é: {resultado}")
    
""""""
import random

nome = input('Qual o seu nome? ')
vida = 100
gold = 10
print('Seu nome é ' + nome)
print('Sua vida é ' + str(vida))
print('Seu gold é ' + str(gold))


while True:
    opcoes = int(input("\nQual a sua opção? 1-Explorar 2-Loja 3-Sair: "))
    
    if opcoes == 1:
        print("Você escolheu Explorar!") 
        print("Rolando o dado do destino...")
        dado = random.randint(1, 6)

        # 2. Toda esta parte deve estar recuada (dentro do if opcoes == 1)
        if dado == 1:
            print("Saiu 1! Você tropeçou numa pedra.")
        elif dado == 2:
            print("Saiu 2! Tudo calmo.")
        elif dado == 3:
            print("Saiu 3! Achou 5 golds!")
            gold += 5
            print(f"Agora você tem {gold} golds.")
        else:
            print(f"Saiu {dado}! um Orc Furioso te acertou uma marretada.")
            vida -= 20
            print(f"Sua vida agora é {vida}.")
            
            if vida <= 0:
                print("Você morreu! Fim de jogo.")
                break  # Sai do loop principal e termina o jogo
  
    elif opcoes == 2: 
        print("Bem-vindo à loja!")
        if gold >= 10:
            print("Você comprou uma poção de vida por 10 golds.")
            gold -= 10
            vida += 20
            if vida > 100:
                vida = 100  # Vida máxima é 100
            print(f"Sua vida agora é {vida} e você tem {gold} golds restantes.")
        else:
            print("Você não tem gold suficiente para comprar nada.")    
    elif opcoes == 3: # 3. Agora este elif está alinhado corretamente com o primeiro 'if'
        print("Você escolheu Sair!")  
        break 
        
    else:
        print("Opção inválida! Tente novamente.")"""
    

"""    
import random

# --- GLOBAL VARIABLES ---
# Default values for a new game
nome = input('What is your name? ')
vida = 100
gold = 60 
inventario = [] 
tem_espada = False 
tem_escudo = False 

# --- FUNCTIONS ---

def save_game():
    # We need to access these variables to write them to the file
    global nome, vida, gold, tem_espada, tem_escudo
    
    print("\n--- 💾 SAVING GAME... ---")
    
    # 'w' mode (Write) creates the file or overwrites it
    try:
        with open("save.txt", "w") as file:
            file.write(f"{nome}\n")
            file.write(f"{vida}\n")
            file.write(f"{gold}\n")
            file.write(f"{tem_espada}\n") # Writes "True" or "False" text
            file.write(f"{tem_escudo}\n")
        print("✅ Game saved successfully!")
    except Exception as error:
        print(f"❌ Error saving game: {error}")

def load_game():
    # We need to CHANGE these variables with data from the file
    global nome, vida, gold, tem_espada, tem_escudo, inventario
    
    print("\n--- 📂 LOADING GAME... ---")
    
    try:
        # 'r' mode (Read) only opens if file exists
        with open("save.txt", "r") as file:
            data = file.readlines() # Reads all lines into a list
            
            # .strip() removes the \n (enter) at the end of the line
            nome = data[0].strip()
            vida = int(data[1].strip())
            gold = int(data[2].strip())
            
            # Parsing Booleans: "True" (str) -> True (bool)
            tem_espada = (data[3].strip() == "True")
            tem_escudo = (data[4].strip() == "True")
            
            # Rebuilding the visual inventory based on booleans
            inventario = [] # Clear current inventory
            if tem_espada:
                inventario.append("Espada")
            if tem_escudo:
                inventario.append("Escudo")
            
            print(f"✅ Welcome back, {nome}! Data loaded.")
            
    except FileNotFoundError:
        print("❌ Save file not found! Play and save first.")
    except Exception as error:
        print(f"❌ Corrupted file or error: {error}")

def explorar():
    global vida, gold, tem_espada, tem_escudo
    
    print("\n--- 🌲 Exploring the Dungeon 🌲 ---")
    print("Rolling the die of destiny...")
    dado = random.randint(1, 6)

    if dado == 1:
        print(">> You rolled 1! You tripped on a rock. (-5 HP)")
        vida -= 5
    elif dado == 2:
        print(">> You rolled 2! Silence. It's safe.")
    elif dado == 3:
        print(">> You rolled 3! Found a hidden chest! (+5 Gold)")
        gold += 5
        print(f"💰 Gold: {gold}")
    else: 
        print(f"\n>> DANGER! Die rolled {dado}!")
        print("👹 An ANGRY ORC appears!")
        
        # Defense Phase
        dano_recebido = 0
        if tem_escudo:
            print("🛡️ BLOCKED! Your Shield reduced the damage.")
            dano_recebido = 5 
        else:
            print("🤕 NO DEFENSE! You took a full hit.")
            dano_recebido = 20 
        
        vida -= dano_recebido
        print(f"💥 You lost {dano_recebido} HP.")

        # Attack Phase
        if tem_espada:
            print("⚔️ COUNTER-ATTACK! You killed the Orc!")
            print("💰 You looted 15 Gold!")
            gold += 15
        else:
            print("💨 You have no weapon... You ran away.")

def loja():
    global vida, gold, inventario, tem_espada, tem_escudo

    print("\n--- 🏪 MERCHANT SHOP ---")
    print(f"Your Gold: {gold}")
    print("1. Health Potion (10g) - Heals 30 HP")
    print("2. Wooden Shield (40g) - Reduces Damage")
    print("3. Steel Sword (60g) - Allows Killing")
    print("0. Back")

    escolha = input("Buy: ")

    if escolha == "1":
        if gold >= 10:
            gold -= 10
            vida += 30
            if vida > 100: vida = 100 
            print(f"🧪 Gulp! HP: {vida}")
        else:
            print("🚫 Not enough gold.")    

    elif escolha == "2":
        if tem_escudo:
            print("You already have a shield!")
        elif gold >= 40:
            gold -= 40
            inventario.append("Escudo") 
            tem_escudo = True 
            print("🛡️ Shield bought!")
        else:
            print("🚫 Cost: 40g.")

    elif escolha == "3":
        if tem_espada:
            print("You already have a sword!")
        elif gold >= 60:
            gold -= 60
            inventario.append("Espada") 
            tem_espada = True 
            print("⚔️ Sword bought!")
        else:
            print("🚫 Cost: 60g.")

# --- MAIN GAME LOOP ---
while True:
    print("------------------------------------------------")
    print(f"👤 {nome} | ❤️ HP: {vida} | 💰 Gold: {gold}")
    
    try:
        opcoes = int(input("1-Explore | 2-Shop | 3-Exit | 4-Inventory | 5-Save | 6-Load: "))
    except ValueError:
        print("⚠️ Numbers only, please!")
        continue

    if opcoes == 1:
        explorar() 
    elif opcoes == 2:
        loja()
    elif opcoes == 3:
        print("Goodbye!")
        break
    elif opcoes == 4:
        print(f"\n🎒 BACKPACK: {inventario}")
    elif opcoes == 5:
        save_game()
    elif opcoes == 6:
        load_game()
    else:
        print("Invalid Option!")

    if vida <= 0:
        print("\n💀 GAME OVER 💀")
        break
        
"""



"""velocidade = int(input("Digite a velocidade do carro (km/h): "))
if velocidade > 50:
    print("Multado! Você excedeu o limite de velocidade.")
    
else:
    print("Velocidade dentro do limite. Dirija com segurança!")
    
valor = float(input("Digite o valor da entrega"))
if valor >= 3.50:
    print("Aceitar pedido imediatamente")
else:
    print("Não dá nem para o baseado!")

tempo = input("Está chovendo? (s/n): ")
if tempo.lower() == 's':
    print("Leve um guarda-chuva!")
else:
    print("Bom dia! Aproveite o sol!")"""
    

"""

entregas = [5.50, 3.00, 8.00, 2.50, 6.00]

# 1. Somar (Sem colchetes!)
total_dia = sum(entregas)

# 2. Contar (Quantas entregas fiz?)
qtd_entregas = len(entregas)

print(f"Fiz {qtd_entregas} entregas.")
print(f"O total ganho no dia foi: {total_dia} €")
"""

"""corridas = [4.50, 8.00, 3.20, 12.50, 6.00]

# 1. Total (Tu fizeste certo, mas olha a versão manual)
total = 0
for valor in corridas:
    total += valor  # Vai somando um por um

# 2. Maior Valor (Função max ou lógica)
maior_corrida = max(corridas) # O Python acha o maior sozinho

# 3. Média (Total dividido pela quantidade)
quantidade = len(corridas)
media = total / quantidade

print(f"Total: {total}")
print(f"Maior corrida: {maior_corrida}")
print(f"Média: {media}")

notas = [10, 20]
menor_nota = min(notas)
maior_nota = max(notas)
total = 0
for valor in corridas:
    total += valor
quantidade_notas = len(notas)
media = total / quantidade_notas
print(f"total {total}, maior nota {maior_nota}, menor nota {menor_nota}")

###

nomes = ['Ana', 'Pedro', 'João', 'Maria']
idades = [16, 25, 17, 30]

# 1. Cria a lista de números (0, 1, 2, 3)
indices = range(len(nomes))

# 2. Loop
for i in indices:
    # AQUI ESTÁ O SEGREDO:
    # Pega o nome e a idade usando o 'i'
    nome_atual = nomes[i]
    idade_atual = idades[i]
    
    # Agora faz o IF com a idade_atual
    if idade_atual >= 18:
        print(nome_atual, "pode entrar")
    else:
        print(nome_atual, "menor de idade")
        pass"""
        

"""piloto = "Jeff"
ganho_hoje = float(input("Quanto você já fez hoje?"))
meta_dia = 30
falta_quanto = meta_dia - ganho_hoje
if ganho_hoje >= meta_dia:
    print("Meta batida! Você é brabo.")
else:
    print(falta_quanto, "Faltam para meta.")"""
    
"""fatura = float(input("Quanto faturou?"))
nota = float(input("Qual sua nota de estrelas (0 a 5)?"))
if fatura >= 30 and nota >= 4:
    print("Motorista Vip")
else:
    print("Sem bônus hoje.")"""
    
"""semana = [7.00, 3.00, 4.00]
print(f" segunda feira fiz: {semana[0]}")
print(f" quarta feira fiz: {semana[1]}")
print(f" sexta feira fiz: {semana[2]}")"""

"""carrinho = []
carrinho.append("Trotinete")
carrinho.append("Capacete")
carrinho[0] = "Moto"
print(carrinho)"""

"""ganhos_semana = [10, 20, 50, 5]
indices = 0
for i in ganhos_semana:
   print(i * 2)"""
   
"""corridas = [5.50, 10.00, 4.50, 20.00]

total_cofre = 0  # Começa zerado

for grana in corridas:
    # Pega o que tem no cofre e soma a grana nova
    total_cofre = total_cofre + grana 

print(total_cofre) # Só imprime no final, fora do loop
"""


"""dias = ["Segunda", "Terça", "Quarta"]
valores = [30.00, 15.50, 40.00]
for i in range(len(dias)):
    valor_atual = valores[i]
    dia_atual = dias[i]
    print(valor_atual,dia_atual)"""

"""placa = "ABCD-12"
letras = placa[0:4]
numeros = placa[5:8]
print(letras, numeros)

entrada = " jEfFeRsOn "
entrada = entrada.strip().lower().replace("o", "0")
print(entrada)"""

"""cpf = "123.456.789-00"
cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")
print(cpf)"""
"""
def calcular_lucro(ganho, gasto):
    total = ganho - gasto
    return total
lucro_hoje = calcular_lucro(50, 10)
print(lucro_hoje)
 

def atacar(vida):
    total = vida - 15
    return total

ataque = atacar(1)
print(ataque)"""







"""ganhos_brutos = [20, 30, 10, 20] 

def calcular_lucro_semanal(lista, custo_por_dia):
    lucro_total = 0 # O Cofre começa vazio
    
    for dia in lista:
        # 1. Calcula quanto sobrou hoje
        sobra_do_dia = dia - custo_por_dia
        
        # 2. A LINHA QUE FALTAVA: Joga no cofre!
        lucro_total = lucro_total + sobra_do_dia  # <<<< AQUI!
        # (Ou poderia ser: lucro_total += sobra_do_dia)
    
    return lucro_total

# Teste
resultado = calcular_lucro_semanal(ganhos_brutos, 5)
print(f"Lucro Limpo da Semana: {resultado}")"""

"""def gritar(texto):
    print(f"!!! {texto} !!!")

gritar("jefferson")
gritar("luiza")
gritar(1000)"""
# --- TEU CÓDIGO AQUI EM BAIXO ---
# Chama a função 'gritar' 3 vezes com coisas diferentes dentro dos parênteses
"""
nome = "Jeff"
gosto = "Buceta"

def fofoca(quem, o_que):
    quem = nome
    o_que = gosto
    print(f"Olha só: O {quem} gosta muito de {o_que}")
    
fofoca(nome, gosto)

# 1. Definir as variáveis LÁ FORA (O Mundo Real)
nome = "Jeff"
nave = "Trotinete"

# 2. Definir a máquina (A Função)
# Repara: Aqui dentro SÓ usamos 'piloto' e 'veiculo'
def pilotar(piloto, veiculo):
    # NÃO FAZEMOS 'piloto = nome'. A passagem é automática.
    print(f"O motorista {piloto} ligou a {veiculo}")

# 3. Fazer a Passagem (O Arremesso)
# Aqui o Python pega o VALOR de 'nome' e joga para 'piloto'
pilotar(nome, nave)


vida = 100
def atacar(quem_sofreu):
    quem_sofreu - 15
    print("Sofreu 15 de dano")
atacar(vida)

nome_do_cliente = "Luiza"

def dar_ola(pessoa):
    # O erro vai acontecer na linha abaixo. Porquê?
    print(f"Olá, {pessoa}") 

dar_ola(nome_do_cliente)"""


# Código do desafio dos dicionários. 

