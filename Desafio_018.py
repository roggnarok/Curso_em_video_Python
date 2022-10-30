# Desafio018 - Recebe o valor de um ângulo e mostra o seno, cosseno e tangente.
import math
angulo = float(input('Digite o seu ângulo favorito: '))# Recebe o valor do ângulo.
ang_rad = math.radians(angulo)                         # Converte o ângulo em Radianos.
# Mostra o ângulo em Radianos.
print(f'O valor do ângulo {angulo}° em radianos é: {ang_rad:.4f} rad.')
# Calcula o Seno (O ângulo DEVE estar em Radianos)!
seno = math.sin(ang_rad)
#Calcula o Cosseno (O ângulo DEVE estar em Radianos)!
cosseno = math.cos(ang_rad)
# Calcula a Tangente (O ângulo DEVE estar em Radianos)!
tang = math.tan(ang_rad)
# Mostra o resultado.
print(f'O Seno é {seno:.4f}, o Cosseno é {cosseno:.4f}'
      f' e a Tangente é {tang:.4f}')