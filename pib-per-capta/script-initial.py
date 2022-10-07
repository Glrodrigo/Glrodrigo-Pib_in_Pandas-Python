#Carregamento variaveis
import pandas as pd

#Codigo principal
#1.Carregar arquivo base xlsx
#2.Exibir linhas do arquivo

class CalculatePib:
    raw_data = None
    def load_file(self):
        print('Inicio do script')
        self.raw_data = pd.ExcelFile("base.xlsx")

    def load_uf_region(self):
        content = pd.read_excel(self.raw_data, "UF_Regiao")
        return content

def main():
    calculate = CalculatePib()
    #r = pd.ExcelFile("base.xlsx")
    #df = pd.read_excel(r, "UF_Regiao")
    #print(df)
    # load_file()
    #result = load_uf_region()
    calculate.load_file()
    result = calculate.load_uf_region()
    print(result)


main()