import json
import random
import twitter
import urllib.request


with open("brasileiros_vivo_foto_opcional.json", "r", encoding="utf-8") as read_file:
    dataP = json.load(read_file)

with open("midia_brasileira.json", "r", encoding="utf-8") as read_file:
    dataM = json.load(read_file)

formatos = ["Em entrevista n", "No editorial d", "Em uma coluna n"]
artigos = {
	"male": "o novo",
	"female": "a nova",
	"transgender female": "a nova",
	"transgender male": "o novo",
	"non-binary": "x novx",
	"cisgender male": "o novo",
	"cisgender female": "a nova",
	"travesti": "x novx",
}

frases = {
    "online newspaper": "{formato}o jornal online \"{midia}\", {nome} declarou que será {artigo} vice de Lula.",
    "magazine": "{formato}a revista \"{midia}\", {nome} declarou que será {artigo} vice de Lula.",
    "newspaper": "{formato}o jornal \"{midia}\", {nome} declarou que será {artigo} vice de Lula.",
    "news program": "{formato}o programa \"{midia}\", {nome} declarou que será {artigo} vice de Lula.",
}


pessoa = random.choice(dataP)
midia = random.choice(dataM)

texto = frases[midia['tipoLabel']].format(formato=random.choice(
	formatos), midia=midia['jornalLabel'], nome=pessoa['humanLabel'], artigo=artigos[pessoa["genderLabel"]])

if ("image" in pessoa):
	urllib.request.urlretrieve(pessoa['image'] , "temp.jpg")
	twitter.tweet(texto, "temp.jpg")
else:
	twitter.tweet(texto, None)

