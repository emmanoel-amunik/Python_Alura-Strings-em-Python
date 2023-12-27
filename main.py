# url = ("https://bytebank.com/cambio?quantidade=100&moedaOrigem="
       # "real&moedaDestino=dólar").strip()
url = " ".strip()

if url == "":
    raise ValueError("The URL is empty")
question_index = url.find("?")
url_base = url[:question_index]
url_parameters = url[question_index+1:]
print(url_parameters)

search_parameter = "quantidade"
parameter_index = url_parameters.find(search_parameter)
index_value = parameter_index + len(search_parameter) + 1
index_comercial_e = url_parameters.find("&", index_value)

if index_comercial_e == -1:
    value = url_parameters[index_value:]
else:
    value = url_parameters[index_value:index_comercial_e]

print(value)
