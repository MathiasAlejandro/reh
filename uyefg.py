meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "xD": "Es un emoji que hace una carita riendo muchoooo",
            "XD": "Es un emoji que hace una carita riendo muchoooo",
            "xd": "Es un emoji que hace una carita riendo muchoooo",
            "WTF": "Es una mala palabra en ingles",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("No tenemos esa palabra, te recomiendo buscar en internet, una disculpa :)")
