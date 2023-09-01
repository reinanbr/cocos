from cocos import Cocos
from cocos import make_report_pdf


files = ['data_all_ok.xlsx','data_ph_hight.xlsx','data_nitro_ok.xlsx','data.xlsx']
for file in files:
    cocos = Cocos('data/'+file)
    cocos.place = 'quidé, Juazeiro - BA'

    path_pdf = f"pdf/{file.split('.')[0]}.pdf"
    make_report_pdf(cocos,pdf_path=path_pdf)