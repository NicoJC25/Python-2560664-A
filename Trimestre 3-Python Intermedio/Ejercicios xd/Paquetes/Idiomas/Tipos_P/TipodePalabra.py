def Ing():
    palabra=input('Put a word: ')
    Ving=['do sport','Diving','cover','tick','throw away','To win','to lose','thrash','to run','to jump','beat','rollerblading','slurp','train','compete','swim','mount','play','do','skiing','train','heat up','annotate','bat']
    susting=['ball','soccer','basketball','volleyball','goal','inch','amateur','fan','sport','player','goalie','team','Golf','match','exercise','baseball','surfer','runner','scaler','boxer','diver','tennis','court','coach']
    AdIng=['winner','loser','high','under','well','bad','clumsy','amazing']
    if palabra in Ving:
        print('the word',palabra,'is a verb')
    elif palabra in susting:
        print('the word',palabra,' is a noun')
    elif palabra in AdIng:
        print('the word',palabra,'is an adjective')
    else:
        print('the word',palabra,'is not found')
        
def Por():
    palabra=input('Digite uma palavra: ')
    Vport=['Mergulhando','cobrir','marcação','jogar fora','Ganhar','perder','amarrar','lixo','para correr','saltar','bater','andar de patins','sorver','Comboio','competir','nadar','montar','lançar','Toque','Faz','esquiar','Comboio','aquecer','anotar','bastão']
    sustpr=['bola','futebol','basquetebol','vôleibola','meta','estádio','polegada','amador','ventilador','esporte','jogador','goleiro','equipe','Golfe','partida','exercício','beisebol','surfista','corredor','escalador','boxer','mergulhador','tênis','quadra','treinador']
    AdPor=['vencedora','fracassado','Alto','debaixo','mau','desajeitado','incrível']
    if palabra in Vport:
        print('a palavra',palabra,'é um verbo')
    elif palabra in sustpr:
        print('a palavra',palabra,'é um substantivo')
    elif palabra in AdPor:
        print('a palavra',palabra,' é um adjetivo')
    else:
        print('a palavra',palabra,' não foi encontrada')
        
def Esp():
    palabra=input('Ingrese una palabra: ')
    Vesp=['bucear','tapar','marcar','tirar','ganar','perder','empatar','golear','correr','saltar','golpear','patinar','sorfear','entrenar','competir','nadar','montar','lanzar','jugar','hacer','esquiar','entrenar','calentar','anotar','batear']
    SusEsp=['Pelota', 'fútbol', 'baloncesto', 'voleibol', 'pelota', 'gol', 'estadio', 'pulgar', 'aficionado', 'aficionado', 'deporte', 'jugador', 'portero ', 'equipo', 'golf', 'partido', 'ejercicio', 'béisbol', 'surfista', 'corredor', 'escalador', 'boxeador', 'buceador', 'tenis', 'investigador', 'entrenador',]
    AdEsp=['ganador', 'perdedor', 'alto', 'bajo', 'bueno', 'malo', 'incómodo', 'increíble']
    if palabra in Vesp:
        print('la palabra',palabra,'es un verbo')
    elif palabra in SusEsp:
        print('la palabra',palabra,' es un sustantivo')
    elif palabra in AdEsp:
        print('la palabra',palabra,', es un adjetivo')
    else:
        print('la palabra',palabra,'no se encuentra')
        
def Fran():
    palabra=input('Entrer un mot: ')
    Vfran=['plonger', 'couvrir', 'marquer', 'tirer', 'gagner', 'perdre', 'attacher', 'thrat', 'courir', 'sauter', 'frapper', 'skate', 'surf ', 'sentraîner', 'compétition', 'nager', 'rouler', 'lancer', 'jouer', 'faire', 'ski', 'train', 'échauffement', 'score', 'frapper']
    SusFran=['Balle','football','basketball','volley-ball','Balle','but','stade','pouce','amateur','ventilateur','sport','joueur','gardien de but','équipe','Le golf','correspondre','exercer','base-ball','surfeur','coureur','écailleur','boxeur','plongeur','tennis','rechercher','entraîneur']
    AdFran=['gagnant','perdant','haute','bas','bon','mal','maladroit','étonnante']
    if palabra in Vfran:
        print('le mot',palabra,'est un verbe')
    elif palabra in SusFran:
        print(' le mot',palabra,'est un nom')
    elif palabra in AdFran:
        print('le mot',palabra, 'est un adjectif')
    else:
        print('le mot',palabra,'est introuvable')


