#error's

class KeyDataNotFound(Exception):
    def __init__(self,key,file_data):
        super().__init__(f"A chave '{key}' não foi encontrada no arquivo '{file_data}'. Com isso, não podemos trabalhar com ele.")
        self.key = key
        
class FileIsNotExcelType(Exception):
    def __init__(self,file_data,file_type):
        super().__init__(f"O arquivo '{file_data}' não possui o tipo adequado para trabalho em noso sistema. Ele é um arquivo '{file_type}' e só aceitamos '.osd' ou '.xlsx'.")
        

class FileNotFound(Exception):
    def __init__(self,file_data):
        super().__init__(f"O arquivo '{file_data}' simplesmente não existe, ou não foi encontrado.")