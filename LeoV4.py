#Por se tratar do software Zapier, devemos usar JSON no output do código
import json 

def format_phone_number(input_data):
    #Variável usada para medir o Lenght do número
    numberExampleWithNine = "+5551981758861"

    ddd_with_nine = [
        "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "21", "22", "24", "27", "28",
    ]
    ddd_without_nine = [
        "10", "23", "25", "26", "29", "30", "32", "36", "37", "39",
        "40", "41", "42", "43", "45", "46", "47", "48", "49", "50",
        "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
        "61", "63", "64", "65", "67", "68", "69", "71", "72", "74",
        "75", "76", "77", "78", "79", "80", "81", "82", "83", "84",
        "85", "86", "89", "90", "91", "92", "93", "94", "95", "96",
        "97", "98", "99",
    ]

    if not input_data:  # Se input_data for uma lista vazia, retorna uma string vazia
        return ""

    # Extrai o DDD do input_data, que é o número de telefone
    ddd = input_data[3:5]

    if ddd in ddd_with_nine:
        # Adiciona o digito "9" após o DDD se a condição DDD estiver na lista 
        input_data = input_data[:5] + "9" + input_data[5:]

    if len(input_data) < len(numberExampleWithNine):
            # Se o comprimento de input_data for menor que comprimento da variável criada, é adicionado zeros a direita
            input_data += "0" * (13 - len(input_data))

    elif ddd in ddd_without_nine:
        if len(input_data) == len(numberExampleWithNine):
        # Retira o número "9" da string input_data
            input_data = input_data[:5] + input_data[6:]

            # Se o comprimento de input_data for menor que comprimento da variável criada, é adicionado zeros a direita
    if len(input_data) < len(numberExampleWithNine[:11]):
            input_data += "0" * (12 - len(input_data))

    return input_data

# Inicializando como uma lista vazia, após essa lista vazia pega o número gerado pela planilha via Zapier
input_data = []  
formatted_phone_number = format_phone_number(input_data)
output = {"formatted_phone_number": formatted_phone_number}
print(json.dumps(output))

