populacao_a = 80000
populacao_b = 200000
taxa_crescimento_a = (populacao_a * 0.03)+populacao_a
taxa_crescimento_b = (populacao_b * 0.015)+populacao_b
i=0

while (populacao_a < populacao_b):
  populacao_a = taxa_crescimento_a
  populacao_b = taxa_crescimento_b
  taxa_crescimento_a = (populacao_a * 0.03)+populacao_a
  taxa_crescimento_b = (populacao_b * 0.015)+populacao_b
  print(f"População A: {populacao_a:.0f}")
  print(f"População B: {populacao_b:.0f}")
  i=i+1
  print ("Anos passados: ", i, "\n")