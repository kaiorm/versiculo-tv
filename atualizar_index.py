from datetime import datetime

# Data de hoje no formato AAAAMMDD
data = datetime.now().strftime('%Y%m%d')
url_imagem = f"https://s3.amazonaws.com/static.youversionapi.com/images/base/{data}.jpg"

# Carrega o index.html
with open("index.html", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Substitui o PLACEHOLDER pela data atual
conteudo = conteudo.replace("PLACEHOLDER", data)

# Salva o novo HTML
with open("index.html", "w", encoding="utf-8") as f:
    f.write(conteudo)
