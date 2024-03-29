Español={'Acrobatics':'Acrobacia',
         'Aerobics':'Aerobico',
         'Aikido':'Aikido',
         'Archery':'Arqueria',
         'Athletics':'Atletismo',
         'Badminton':'Badminton',
         'Baseball':'Beisbol',
         'Basketball':'Baloncesto',
         'Billiards':'Billar',
         'Bodybuilding':'Culturismo',
         'Boxing':'Boxeo',
         'Bowling':'Bolos',
         'Boat race':'Regata',
         'Canoeing':'Piragüismo',
         'Car racing':'Automovilismo',
         'Chess':'Ajedrez',
         'Combat':'Lucha',
         'Cricket':'Criquet',
         'Cycling':'Ciclismo',
         'Curling':'Curling',
         'Darts':'Dardos',
         'Diving':'Buceo',
         'Fencing':'Esgrima',
         'Fishing':'Pesca',
         'Five a side footbal':'Futbol sala',
         'Football':'Futbol americano',
         'Golf':'Golf',
         'Gymnastics':'Gimnasia',
         'Handball':'Balonmano',
         'Hiking':'Senderismo',
         'Hockey':'Hockey',
         'Hunting':'Caza',
         'Indoor soccer':'Futbol sala',
         'Karate':'Karate',
         'Kickboxing':'Kickboxing',
         'Kung fu':'Kung fu',
         'Lacrosse':'Lacrosse',
         'Martial arts':'Artes marciales',
         'Marathon':'Maraton',
         'Motoring':'Motorismo',
         'Motorboat racing' : 'Motonautica',
         'Motorcycling' : 'Motociclismo',
         'Mountaineering' : 'Montañismo',
         'Mountain biking' : 'Ciclismo de montaña',
         'Paintball' : 'Paintball',
         'Paddel' : 'Padel',
         'Parachuting' : 'Paracaidismo',
         'Paragliding' : 'Parapente',
         'Parkour' : 'Parkour',
         'Pole vault' : 'Salto con pertiga',
         'Polo' : 'Polo',
         'Pool' : 'Billar (16 bolas)',
         'Racquetball' : 'Raquetbol',
         'Rafting' : 'Canotaje',
         'Rapel' : 'Descenso con cuerdas',
         'Rhythmic gymnastics' : 'Gimnasia ritmica',
         'Rings' : 'Anillas',
         'Rock climbing' : 'Escalada',
         'Roller hockey' : 'Hockey sobre patines',
         'Rope jumping' : 'Saltar la cuerda',
         'Rowing' : 'Remo',
         'Rugby' : 'Rugby',
         'Running' : 'Correr',
         'Sailing' : 'Vela',
         'Scuba diving' : 'Buceo',
         'Skating' : 'Patinaje',
         'Skateboarding' : 'Skateboard',
         'Skiing' : 'Esqui',
         'Snorkeling' : 'Esnorquel',
         'Snowboarding' : 'Snowboard',
         'Soccer' : 'Futbol',
         'Softball' : 'Softbol',
         'Squash' : 'Squash',
         'Streching' : 'Estiramiento',
         'Sumo' : 'Sumo',
         'Surf' : 'Surf',
         'Swimming' : 'Natacion',
         'Table tennis' : 'Tenis de mesa',
         'Taekwondo' : 'Taekwondo',
         'Tennis' : 'Tenis',
         'Trampolining' : 'Salto de trampolín',
         'Trapeze' : 'Trapecio',
         'Volleyball' : 'Voleibol',
         'Water polo' : 'Waterpolo',
         'Water skiing' : 'Esqui acuático',
         'Winter sports' : 'Deportes de invierno',
         'Wrestling' : 'Lucha',
         'Athletes' : 'atletas',
         'Bat' : 'bate de béisbol o raqueta de tenis de mesa',
         'Boots' : 'botas',
         'Champion' : 'campeon',
         'Championship' : 'campeonato',
         'Clubs' : 'palos de golf',
         'Crash Helmet' : 'casco protector',
         'Crowd' : 'multitud',
         'Jockey' : 'jinete',
         'Equipment' : 'equipamiento',
         'Gloves' : 'guantes (boxeo)',
         'Lap' : 'vuelta',
         'Loser' : 'perdedor',
         'Olympic Games' : 'juegos Olímpicos',
         'Player' : 'jugador',
         'Puck' : 'disco de Hockey',
         'Race' : 'carrera',
         'Racetrack' : 'hipódromo',
         'Racket' : 'raqueta de tenis',
         'Referee' : 'árbitro de fútbol, rugby y baloncesto',
         'Risk' : 'riesgo',
         'Ring' : 'ring',
         'Scoreboard' : 'marcador',
         'Spectator' : 'espectador',
         'Skates' : 'patines',
         'Swimming pool' : 'piscina',
         'Stadium' : 'estadio',
         'Stick' : 'palo de Hockey',
         'Sword' : 'espada (esgrima)',
         'Trainer' : 'Entrenador',
         'Trophy' : 'Trofeo',
         'Track' : 'Pista',
         'Umpire' : 'Arbitro de beisbol y tenis',
         'Velodrome' : 'velodromo',
         'Winners' : 'ganador',
         'Whistle' : 'pito'}
def buscar_palabra():
    palabra=input('Ingrese la palabra que desea buscar: ')
    for p in Español.keys():
        if palabra==p:
            print('La traduccion de la palabra',palabra,'al español, es:',Español[p])
            return None
        
    print('La palabra no esta en el diccionario')
    return None
            
