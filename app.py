from flask import Flask, render_template, request, session
import random
from os import system, name

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Chave secreta para usar sessões

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    dado = request.form['dado']
    resultado = f'Você digitou: {dado}'
    return resultado

@app.route('/forca', methods=['GET', 'POST'])
def forca():
    if request.method == 'POST':
        tentativa = request.form['tentativa'].lower()
        palavra = session['palavra']
        letras_descobertas = session['letras_descobertas']
        chances = session['chances']
        letras_erradas = session['letras_erradas']

        if tentativa in palavra:
            for index, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        session['letras_descobertas'] = letras_descobertas
        session['chances'] = chances
        session['letras_erradas'] = letras_erradas

    else:
        palavras =  ['Abelha', 'Abutre', 'Águia', 'Albatroz', 'Alce', 'Alpaca', 'Anaconda',
    'Andorinha', 'Anhuma', 'Anta', 'Antílope', 'Aranha', 'Arara', 'Ararajuba',
    'Ariranha', 'Asno', 'Atum', 'Avestruz', 'Azulão', 'Babuíno', 'Badejo',
    'Bagre', 'Baiacu', 'Baleia', 'Barata', 'Beija-flor', 'Beluga', 'Bem-te-vi',
    'Besouro', 'Bicho-da-seda', 'Bisão', 'Bode', 'Boi', 'Borboleta', 'Boto',
    'Búfalo', 'Burro', 'Cabra', 'Cacatua', 'Cachorro', 'Calango', 'Camaleão',
    'Camarão', 'Camelo', 'Camundongo', 'Canário', 'Canguru', 'Capivara',
    'Caracol', 'Caramujo', 'Caranguejo', 'Carneiro', 'Carrapato', 'Cavalo',
    'Cegonha', 'Centopeia', 'Chacal', 'Cigarra', 'Cisne', 'Coala', 'Cobra',
    'Codorna', 'Coelho', 'Coruja', 'Crocodilo', 'Cuíca-lanosa', 'Cupim', 'Cutia',
    'Damão', 'Diabo-da-tasmânia', 'Diamante-de-gould', 'Dinossauro', 'Doninha',
    'Dragão-de-komodo', 'Dromedário', 'Dugongo', 'Elefante', 'Ema', 'Enguia',
    'Escorpião', 'Esponja', 'Esquilo', 'Estrela-do-mar', 'Faisão', 'Falcão',
    'Feneco', 'Flamingo', 'Foca', 'Formiga', 'Fuinha', 'Furão', 'Gafanhoto',
    'Gaivota', 'Galo', 'Gambá', 'Gamo', 'Ganso', 'Garça', 'Gato', 'Gavial',
    'Gavião', 'Gazela', 'Gecko leopardo', 'Girafa', 'Gnu', 'Golfinho', 'Gorila',
    'Gralha', 'Grilo', 'Guanaco', 'Guepardo', 'Hadoque', 'Hamster', 'Harpia',
    'Hiena', 'Hilochero', 'Hipopótamo', 'Íbex', 'Iguana', 'Impala', 'Inhambu-chororó',
    'Irara', 'Iraúna', 'Jabuti', 'Jaçanã', 'Jacaré', 'Jacutinga', 'Jaguatirica',
    'Jamanta', 'Jararaca', 'Javali', 'Jegue', 'Jiboia', 'Joaninha', 'Jumento',
    'Kadavu Fantail', 'Kakapo', 'kinguio', 'kiwi', 'kookaburra', 'kowari', 'krill',
    'Lacraia', 'Lagarta', 'Lagartixa', 'Lagosta', 'Lagostim', 'Lambari', 'Lampreia',
    'Leão', 'Lebre', 'Lêmure', 'Leopardo', 'Lesma', 'Lhama', 'Libélula', 'Lince',
    'Lobo', 'Lombriga', 'Lontra', 'Louva-a-deus', 'Lula', 'Macaco', 'Mamute',
    'Mangusto', 'Marimbondo', 'Mariposa', 'Mariquita', 'Maritaca', 'Marmota',
    'Marreco', 'Medusa', 'Mico', 'Minhoca', 'Mocó', 'Morcego', 'Moreia', 'Morsa',
    'Mosca', 'Mosquito', 'Mula', 'Não-pode-parar', 'Narval', 'Negrinho-do-mato',
    'Neinei', 'Nilgó', 'Niquim', 'Noitibó', 'Noivinha', 'Numbat', 'Ocapi', 'Ógea',
    'Onça', 'Orangotango', 'Orca', 'Ornitorrinco', 'Ostra', 'Ouriço', 'Ouriço-do-mar',
    'Ovelha', 'Paca', 'Pacupeba', 'Panda', 'Pangolim', 'Pantera', 'Papagaio', 'Pardal',
    'Pássaro', 'Pato', 'Pavão', 'Peixe', 'Peixe-boi-da-amazônia', 'Pelicano', 'Percevejo',
    'Perdiz', 'Perereca', 'Periquito', 'Pernilongo', 'Peru', 'Pica-pau', 'Pinguim',
    'Pintarroxo', 'Pintassilgo', 'Pinto', 'Piolho', 'Piranha', 'Pirarucu', 'Polvo',
    'Pombo', 'Pônei', 'Porco', 'Porco-espinho', 'Porquinho-da-índia', 'Preá', 'Preguiça',
    'Pulga', 'Puma', 'Quati', 'Quebra-nozes', 'Quero-quero', 'Quetzal', 'Quimera',
    'Quem-te-vestiu', 'Quete-do-sul', 'Rato', 'Ratazana', 'Raposa', 'Rinoceronte',
    'Rã', 'Rouxinol', 'Rena', 'Raia', 'Rola', 'Robalo', 'Rendeira', 'Sabiá', 'Sagui',
    'Salamandra', 'Salmão', 'Sanguessuga', 'Sapo', 'Sardinha', 'Saruê', 'Seriema',
    'Serpente', 'Serval', 'Siri', 'Suçuarana', 'Sucuri', 'Suricate', 'Tainha', 'Tamanduá',
    'Tamboril', 'Tangará', 'Tartaruga', 'Tatu', 'Tatuí', 'Teiú', 'Texugo', 'Teredo',
    'Tigre', 'Tilápia', 'Toupeira', 'Tritão', 'Truta', 'Tubarão', 'Tucano', 'Tucunaré',
    'Tucuxi', 'Tuiuiú', 'Tupaia', 'Unicórnio', 'Urso', 'Urubu', 'Urumutum', 'Uirapuru-de-peito-branco',
    'Uí-pi', 'Vaca', 'Vaga-lume', 'Veado', 'Verdilhão', 'Vespa', 'Víbora', 'Vicunha',
    'Vieira', 'Vison', 'Wallaby', 'Wombats', 'Wrentit', 'Xaiá', 'Xexéu', 'Ximango',
    'Xuê', 'Xuri', 'Yelkouan shearwater', 'Ynambu', 'Zebra', 'Zebu', 'Zangão', 'Zorrilho']
        palavra = random.choice(palavras)
        letras_descobertas = ['_' for _ in palavra]
        chances = 9
        letras_erradas = []

        session['palavra'] = palavra
        session['letras_descobertas'] = letras_descobertas
        session['chances'] = chances
        session['letras_erradas'] = letras_erradas

    return render_template('forca.html', 
                           letras_descobertas=session['letras_descobertas'],
                           chances=session['chances'],
                           letras_erradas=session['letras_erradas'],
                           palavra=session['palavra'])

if __name__ == '__main__':
    app.run(debug=True)
