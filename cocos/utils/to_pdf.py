from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from tqdm import tqdm

from cocos import Cocos
# Create a PDF document

def make_report_pdf(cocos:Cocos,pdf_path=None):
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)

    content = []
    
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    title_style = styles["Title"]


    title1 = Paragraph(f"Relatório de Analíse do Solo", title_style)
    title2 = Paragraph(f"Localidade: {cocos.place}",title_style)
    content.append(title1)
    content.append(title2)


    y_list = ['ph', 'potassium', 'phosphorus', 'nitrogen']
    for y in tqdm(y_list):
        content.append(Spacer(1, 12))
        text_title_y = f"Dados do {y}"
        print()
        
        paragraph = Paragraph(text_title_y, normal_style)
        
    
        img = f'plots/{y}.png'
        cocos.plot_by_key(key=y).savefig(img)
        image = Image(img,width=400,height=300)
        content.append(Spacer(1, 12))
        content.append(paragraph)
        content.append(image)


    mean_ph = cocos['ph']['mean']
    mean_nitro = cocos['nitrogen']['mean']
    if mean_ph < 6.:
        nota = f'Por favor, verifique as quantidades de produtos que você está utilizando, pois o pH está muito abaixo do recomendado: pH = {mean_ph:.2f}. O recomendado é pH > 6. Você pode considerar o uso de calagem para ajustar o pH do solo.'
        if mean_nitro > .3:
            nota = f'Cara ... Veja: [ph médio = {mean_ph:.2f} | nitrogen médio = {mean_nitro:.2f}] Aposto, que você é aquelas pessoas que sofria bulling na escola, por fazer tudo simplesmente errado! Que você era odiado até pela sua mãe. E seu pai falava que você era adotado na sua cara. Como você simplesmente consegue estragar o seu solo! seu Asno! Animal! Agora vai ter que vender essa porra de graça! Muleque burro! Até um garoto de 10 anos entenderia os limites de nitrogênio e ph, seu asno. Adotado! Sua mãe ti culpa pela separação com o seu pai e ela tem toda razão! Vai lá, ser a merda na vida de alguém, seu bosta. Burro'

    elif mean_nitro > 0.3:
        nota = f'Por favor, verifique as quantidades de produtos de fertilizantes à base de nitrogênio que você está utilizando, pois o nível de nitrogênio está muito acima do recomendado: nitrogênio = {mean_nitro:.2f}. O recomendado é nitrogênio < 0.3. Evite o uso excessivo de fertilizantes à base de nitrogênio para evitar danos ao solo.'
        
    else:
        nota = 'Parabéns! O solo está em perfeito estado. Continue com os cuidados adequados.'

    
    content.append(Spacer(1, 12))
    content.append(Paragraph('Nota',title_style))
    content.append(Paragraph(nota,normal_style))
    doc.build(content)
