# Desafio004
# Recebe uma entrada do usuário e informa se é número,
# alfabético, alfanumérico, decimal, maiúscula, minúscula ou se só tem espaços.
entrada = input(
    "Verifica o que é aquilo que foi digitado.\
                    \nDigite qualquer coisa: "
)
print(f'O tipo primitivo é {type(entrada)}') 
print(
    f'Só tem espaços?\t\t{entrada.isspace()}\
      \nÉ um número?\t\t{entrada.isnumeric()}\
      \nÉ alfabético?\t\t{entrada.isalpha()}\
      \nÉ alfanumérico?\t\t{entrada.isalnum()}\
      \nÉ decimal?\t\t{entrada.isdecimal()}\
      \nEstá em maiúsculo?\t{entrada.isupper()}\
      \nEstá em minúsculo?\t{entrada.islower()}\
      \nEstá capitalizada?\t{entrada.istitle()}'
)