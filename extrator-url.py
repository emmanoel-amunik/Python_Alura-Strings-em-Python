class UrlExtractor:
    def __init__(self, url):
        self.url = self.url_strip(url)
        self.url_validation()

    @staticmethod
    def url_strip(url):
        url_type = type(url)

        if url_type == str:
            return url.strip()
        else:
            return ""

    def url_validation(self):
        if not self.url:
            raise ValueError("The URL is empty")

    def get_url_base(self):
        question_index = self.url.find("?")
        url_base = self.url[:question_index]
        return url_base

    def get_url_parameter(self):
        question_index = self.url.find("?")
        url_parameters = self.url[question_index + 1:]
        return url_parameters

    def get_value_parameter(self, parameter_name):
        parameter_index = self.get_url_parameter().find(parameter_name)
        index_value = parameter_index + len(parameter_name) + 1
        index_comercial_e = self.get_url_parameter().find("&", index_value)

        if index_comercial_e == -1:
            value = self.get_url_parameter()[index_value:]
        else:
            value = self.get_url_parameter()[index_value:index_comercial_e]
        return value


url_extractor = UrlExtractor("https://bytebank.com/cambio?quantidade=100&"
                             "moedaOrigem=real&moedaDestino=dólar")
quantity_value = url_extractor.get_value_parameter("quantidade")
print(quantity_value)
