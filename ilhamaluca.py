import time, os
os.system('cls')

print('''
Você é um explorador corajoso em busca de tesouros lendários na
misteriosa Ilha Maluca. Rumores dizem que um grande tesouro está
escondido em algum lugar na ilha, mas para encontrá-lo, você
precisa decifrar uma série de enigmas.
Ao chegar na ilha, você se depara com uma placa estranha com
inscrições antigas. As inscrições dizem o seguinte:
''')
time.sleep(10)
os.system("cls")
print('''
      "𝒫𝒶𝓇𝒶 𝒹𝑒𝓈𝒷𝓁𝑜𝓆𝓊𝑒𝒶𝓇 𝑜 𝓉𝑒𝓈𝑜𝓊𝓇𝑜 𝑒𝓈𝒸𝑜𝓃𝒹𝒾𝒹𝑜, 𝓋𝑜𝒸𝑒 𝒹𝑒𝓋𝑒 𝓅𝓇𝑜𝓋𝒶𝓇 𝓈𝓊𝒶 𝒹𝑒𝓈𝓉𝓇𝑒𝓏𝒶. 𝑅𝑒𝓈𝑜𝓁𝓋𝒶 𝑜𝓈
𝒹𝑒𝓈𝒶𝒻𝒾𝑜𝓈 𝒶 𝓈𝑒𝑔𝓊𝒾𝓇 𝑒 𝓈𝒾𝑔𝒶 𝒶𝓈 𝒾𝓃𝓈𝓉𝓇𝓊ç𝑜𝑒𝓈 𝓅𝒶𝓇𝒶 𝑒𝓃𝒸𝑜𝓃𝓉𝓇𝒶𝓇 𝑜 𝒸𝒶𝓂𝒾𝓃𝒽𝑜 𝒸𝑒𝓇𝓉𝑜."
''')
time.sleep(5)
os.system("cls")
print(''' Desafio 1: O Guardião da Porta
      
Você se depara com uma porta enorme guardada por um gigante adormecido. Para passar
pela porta e continuar sua jornada, você precisa responder a seguinte questão:
''')
time.sleep(5)
os.system("cls")
print('''
"𝒬𝓊𝒶𝓃𝓉𝑜𝓈 𝒸𝑜𝒸𝑜𝓈 𝑜 𝓂𝒶𝒸𝒶𝒸𝑜 𝓉𝑒𝓂 𝓈𝑒 𝑒𝓊 𝓅𝑒𝑔𝒶𝓇 𝓂𝑒𝓉𝒶𝒹𝑒 𝒹𝑜𝓈 𝒸𝑜𝒸𝑜𝓈 𝓆𝓊𝑒 𝑒𝓁𝑒 𝓉𝑒𝓂, 𝓂𝒶𝒾𝓈 𝒹𝑜𝒾𝓈 𝒸𝑜𝒸𝑜𝓈,
𝑒 𝒹𝑒𝓅𝑜𝒾𝓈 𝓈𝓊𝒷𝓉𝓇𝒶𝒾𝓇 𝓉𝓇𝑒𝓈 𝒸𝑜𝒸𝑜𝓈?"
''')
cocos = float(input("Informe o número de cocos que o macaco tinha inicialmente: "))
resposta1 = float(input("Informe o número de cocos que o macaco ficou: "))
conta = cocos/2 + 2 - 3
if conta == resposta1: 
      print("Resposta correta! O gigante permitirá sua pssagem! ")
else:
      print("Resposta incorreta!")
      quit()

print('''
Desafio 2: O Labirinto dos Crocodilos
      
Após passar pela porta, você entra em um labirinto infestado de
crocodilos famintos. Para escapar deles, você precisa resolver o seguinte
problema:
''')
time.sleep(5)
os.system("cls")
print('''
"𝒮𝑒 𝑒𝓊 𝓉𝑒𝓃𝒽𝑜 𝓊𝓂𝒶 𝒸𝑜𝓇𝒹𝒶 𝒹𝑒 12 𝓂𝑒𝓉𝓇𝑜𝓈 𝑒 𝓅𝓇𝑒𝒸𝒾𝓈𝑜 𝒶𝓉𝓇𝒶𝓋𝑒𝓈𝓈𝒶𝓇 𝓊𝓂 𝓇𝒾𝑜 𝒹𝑒 7 𝓂𝑒𝓉𝓇𝑜𝓈 𝒹𝑒 𝓁𝒶𝓇𝑔𝓊𝓇𝒶,
𝓆𝓊𝒶𝓃𝓉𝑜𝓈 𝓂𝑒𝓉𝓇𝑜𝓈 𝒹𝑒 𝒸𝑜𝓇𝒹𝒶 𝒶 𝓂𝒶𝒾𝓈 𝑒𝓊 𝓉𝑒𝓃𝒽𝑜 𝓅𝒶𝓇𝒶 𝒶𝓂𝒶𝓇𝓇𝒶𝓇 𝓃𝒶𝓈 𝒶𝓇𝓋𝑜𝓇𝑒𝓈 𝑒 𝒶𝓉𝓇𝒶𝓋𝑒𝓈𝓈𝒶𝓇 𝒸𝑜𝓂
𝓈𝑒𝑔𝓊𝓇𝒶𝓃ç𝒶?"
''')
resposta2 = float(input("Informe quantos metros de corda sobrou para amarrar nas arvores: "))
if resposta2 == 5:
      print("Resposta correta!")
else: 
      print("Resposta incorreta!")
      quit()

print('''
Desafio 3: O Enigma Final
      
Finalmente, você chega à câmara do tesouro, mas para abri-la, você precisa resolver um
enigma final:
''')
time.sleep(5)
os.system("cls")
print('''
"𝒮𝑒 𝑜 𝓃𝓊𝓂𝑒𝓇𝑜 𝒹𝑒 𝓉𝑒𝓈𝑜𝓊𝓇𝑜𝓈 𝑒𝓃𝓉𝑒𝓇𝓇𝒶𝒹𝑜𝓈 𝓃𝒶 𝒾𝓁𝒽𝒶 𝑒 𝒾𝑔𝓊𝒶𝓁 𝒶𝑜 𝒹𝑜𝒷𝓇𝑜 𝒹𝑜 𝓃𝓊𝓂𝑒𝓇𝑜 𝒹𝑒 𝓅𝒶𝓁𝓂𝑒𝒾𝓇𝒶𝓈,
𝑒 𝑜 𝓃𝓊𝓂𝑒𝓇𝑜 𝒹𝑒 𝓅𝒶𝓁𝓂𝑒𝒾𝓇𝒶𝓈 𝑒 𝒾𝑔𝓊𝒶𝓁 𝒶 𝓉𝓇𝑒𝓈 𝓋𝑒𝓏𝑒𝓈 𝑜 𝓃𝓊𝓂𝑒𝓇𝑜 𝒹𝑒 𝓅𝑒𝓇𝒾𝓆𝓊𝒾𝓉𝑜𝓈 𝓃𝒶 𝒾𝓁𝒽𝒶, 𝑒 𝑜 𝓃𝓊𝓂𝑒𝓇𝑜
𝓉𝑜𝓉𝒶𝓁 𝒹𝑒 𝓅𝑒𝓇𝒾𝓆𝓊𝒾𝓉𝑜𝓈 𝑒 42, 𝓆𝓊𝒶𝓃𝓉𝑜𝓈 𝓉𝑒𝓈𝑜𝓊𝓇𝑜𝓈 𝓉𝑒𝓂 𝓃𝒶 𝒾𝓁𝒽𝒶?"
''')
resposta3 = float(input("Informe o número de tesouros que tem na ilha: "))
periquitos = 42
palmeiras = periquitos * 3
numerotesouros = palmeiras * 2 
if resposta3 == numerotesouros:
      print("Resposta correta! Você recebeu a localização exata do tesouro!")
else:
      print("Resposta incorreta! Infelizmente você não irá receber a localização do tesouro.")
      quit()