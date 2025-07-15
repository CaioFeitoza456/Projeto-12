"""
Este programa faz o seguinte:

- Visualizador de elementos moleculares.

- Mostra o nome, sigla, massa e número 
atômico de cada elemento.

O usuário escolhe um elemento para ser
expandido.
"""

import os
from elementos_quimicos_em_dict import elementos_quimicos
from time import sleep

tamanho_elementos_quimicos = len(elementos_quimicos)

while True:
    os.system("clear")
    for indice, item in enumerate(elementos_quimicos):
        print(f"{indice + 1} - {item['elemento']}")
        item["massa"] = item["massa"].replace(".", ",")

    print()
    print("Qual elemento deseja ver ?")
    
    indice_usuario = input("Digite aqui: ")
    
    try:
        indice_usuario = int(indice_usuario) - 1
    
    except ValueError:
        print("Digite um número.")
        sleep(3)
        continue
    
    if indice_usuario > tamanho_elementos_quimicos:
        print("Digite um índice válido.")
        sleep(3)
        continue

    os.system("clear")
    
    print("~" * 30)
    
    print("Nome do elemento:",
        elementos_quimicos[
            indice_usuario
                ][
            "elemento"
        ]
    )
    print("Sigla do elemento:",
        elementos_quimicos[
            indice_usuario
                ][
            "sigla"
        ]
    )
    print("Massa:", 
        elementos_quimicos[
            indice_usuario
                ][
            "massa"
        ]
    )
    print("N° Atômico:", 
        elementos_quimicos[
            indice_usuario
                ][
                "número atômico"
        ]
    )

    print("~" * 30)

    input("Digite qualquer tecla para retornar.")
