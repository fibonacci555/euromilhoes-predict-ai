import excel
import predict_all
import colorama
from colorama import Fore, Back, Style
# 5. the best way is to use colorama with f-strings
colorama.init(autoreset=True)#auto resets your settings after every output



print(f"""{Fore.GREEN} 888888888                         888b     d888 d8b 888 888                                 
888                                8888b   d8888 Y8P 888 888                                 
888                                88888b.d88888     888 888                                 
8888888   888  888 888d888 .d88b.  888Y88888P888 888 888 88888b.   .d88b.   .d88b.  .d8888b  
888       888  888 888P"  d88""88b 888 Y888P 888 888 888 888 "88b d88""88b d8P  Y8b 88K      
888       888  888 888    888  888 888  Y8P  888 888 888 888  888 888  888 88888888 "Y8888b. 
888       Y88b 888 888    Y88..88P 888   "   888 888 888 888  888 Y88..88P Y8b.          X88 
8888888888 "Y88888 888     "Y88P"  888       888 888 888 888  888  "Y88P"   "Y8888   88888P' 
                                                                                             
                                                                                             
                                                                                             
8888888b.                       888 d8b          888                d8888 8888888            
888   Y88b                      888 Y8P          888               d88888   888              
888    888                      888              888              d88P888   888              
888   d88P 888d888 .d88b.   .d88888 888  .d8888b 888888          d88P 888   888              
8888888P"  888P"  d8P  Y8b d88" 888 888 d88P"    888            d88P  888   888              
888        888    88888888 888  888 888 888      888           d88P   888   888              
888        888    Y8b.     Y88b 888 888 Y88b.    Y88b.        d8888888888   888              
888        888     "Y8888   "Y88888 888  "Y8888P  "Y888      d88P     888 8888888            
                                                                                             
                                                                                             
                                                                                             """)
vezes = int(input("Quantas previsões pretende? (cada previsão demora em volta de 20 min)\nNumero:  "))



excel.start("numeros.xlsx")
for i in range(vezes):
    prediction = predict_all.predict()
    print(f"{Fore.YELLOW}########## Previsão número {i+1} ##########")
    print(f"{Fore.MAGENTA}Numeros: " , end=" ")
    for j in range(0,5):
        print(f"{Fore.BLUE}{prediction[j]}", end=" ")
    print(f"\n{Fore.MAGENTA}Estrelas: " , end=" ")
    for a in range(0,2):
        print(f"{Fore.YELLOW}{prediction[a+5]}", end=" ")