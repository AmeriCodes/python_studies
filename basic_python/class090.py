"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        

shopping_list = []

while True:
    options = input('Select options\n[i]nsert [d]ell [l]ist: ').lower().strip()
    if options not in 'idl' or options is None:
        cls()
        print('Invalid option')
        continue
    
    if options == 'i':
        cls()
        insert = input('Value: ')
        shopping_list.append(insert)
        continue
    
    elif options == 'd':
        cls()
        for i, j in enumerate(shopping_list):
            print(i, j)    
        
        dell_str = input('Choose the index to delete: ')
        
        try:
            dell = int(dell_str)
            del shopping_list[dell]
        except ValueError:
            print('Please enter a valid index.')
        except IndexError:
            print('That index is not in the list.')
        except Exception:
            print('Unkown Error.')
        
            
    elif options == 'l':
        if not any(shopping_list):
            # if buy_list == []
            # if len(buy_list) == 0:
            # if not bool(buy_list):
            # if not buy_list:
            # if buy_list is not True:
            cls()
            print('Nothing to list!')
            continue
        
        else:
            cls()
            for i, value in enumerate(shopping_list):
                print(i, value)
            #else:
                #print(buy_list)
                #continue
