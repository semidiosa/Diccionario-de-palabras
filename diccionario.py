meme_dict = {
            "LOL": "una respuesta a algo gracioso",
            "CRINGE": "algo raro o embarazoso",
            'SHEESH': "ligera desaprobacion",
            "CREEPY": "aterrador, siniestro",
            "AGGRO":  "ponerse agresivo/enojado",
            "ROFL": "una respuesta a una broma"
            }
for i in range(5):      
  word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")  
  if word in meme_dict.keys():
      # ¿Qué debemos hacer si se encuentra la palabra?
      print("Aqui esta la definicion!",meme_dict[word])
  else:
      # ¿Qué hacer si no se encuentra la palabra?
      print("Esa palabra no esta en el diccionario")
