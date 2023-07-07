def remove_repeated(key):
  alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  out = key.upper()
  
  for letter in alfabeto:
    if not letter in key.upper():
      out += letter
  return out
print(remove_repeated("JOAOZAVISAS"))


