INDICE = 13
SOMA = 0
K = 0
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print(SOMA)

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Entrada de um número
numero = int(input("Informe um número: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
  
  import json

# Exemplo de dados JSON (isso seria lido de um arquivo ou entrada)
data = '''
{
    "faturamento": [1000, 2000, 1500, 3000, 2500, null, 0, 1800, 2200, 2500, null, 2600]
}
'''

faturamento_diario = json.loads(data)['faturamento']

# Ignorar valores nulos e calcular a média
faturamento_diario = [x for x in faturamento_diario if x is not None]
media_mensal = sum(faturamento_diario) / len(faturamento_diario)
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
dias_acima_da_media = len([x for x in faturamento_diario if x > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_da_media}")

# Dados de faturamento
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento.values())

percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

def inverter_string(s):
    s_invertida = ''
    for char in s:
        s_invertida = char + s_invertida
    return s_invertida

# Entrada de uma string
string_original = input("Informe uma string: ")
string_invertida = inverter_string(string_original)
print(f"String invertida: {string_invertida}")
