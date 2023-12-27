import re


class UrlExtractor:
    def __init__(self, url):
        self.url = self.url_strip(url)
        self.url_validation()

    def url_validation(self):
        if not self.url:
            raise ValueError("The URL is empty")

        url_pattern = re.compile(
            "(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = url_pattern.match(self.url)
        if not match:
            raise ValueError("The URL is invalid!")

    @staticmethod
    def url_strip(url):
        url_type = type(url)

        if url_type == str:
            return url.strip()
        else:
            return ""

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

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return (self.url + "\n" + "Parameters: " + self.get_url_parameter() +
                "\n" + "URL base: " + self.get_url_base())

    def __eq__(self, other):
        return self.url == other.url


url_standard = ("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&"
                "moedaDestino=dólar")

url_extractor = UrlExtractor(url_standard)
url_extractor2 = UrlExtractor(url_standard)
print(f"The size the URL: {len(url_standard)}")
print(url_extractor)
print(url_extractor == url_extractor2)

quantity_value = url_extractor.get_value_parameter("quantidade")
print(quantity_value)
