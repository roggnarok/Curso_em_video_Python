# Desafio018 - Recebe o valor de um ângulo e mostra o seno, cosseno e tangente.
import math
angulo = float(input('Digite o seu ângulo favorito: '))# Recebe o valor do ângulo.
ang_rad = math.radians(angulo)       # Converte o ângulo de graus para Radianos.
print(f'O valor do ângulo {angulo}° em radianos é: {ang_rad:.4f} rad.') # Mostra o ângulo em Radianos.
#Realiza o cálculo do Seno, Cosseno e Tangente
seno = math.sin(ang_rad) # Calcula o Seno (O ângulo DEVE estar em Radianos)!
cosseno = math.cos(ang_rad) #Calcula o Cosseno (O ângulo DEVE estar em Radianos)!
tang = math.tan(ang_rad) # Calcula a Tangente (O ângulo DEVE estar em Radianos)!
# Mostra o resultado.
print(f'O Seno é {seno:.3f}\
      \nO Cosseno é {cosseno:.3f}\
      \nA Tangente é {tang:.3f}')
#This job was made by Rodrigo. https://github.com/roggnarok
