Ingles ={'Acrobacia':'Acrobatics',
         'Aeróbicos':'Aerobics',
         'Aikido':'Aikido',
         'Arqueria':'Archery',
         'Atletismo':'Athletics', 
         'Bádminton':'Bádminton',
         'Baloncesto':'Basketball',
         'Billar':'Billiards',
         'Culturismo':'Bodybuilding',
         'Boxeo':'Boxing',
         'Bolos':'Bowling',
         'Béisbol':'Baseball',
         'Regata':'Boat race',
         'Piragüismo':'Canoeing',
         'Automovilismo':'Car racing',
         'Ajedrez':'Chess',
         'Lucha':'Combat',
         'Crícquet':'Cricket',
         'Curling':'Curling',
         'Dardos':'Darts',
         'Buceo':'Diving',
         'Hípica':'Equestrian sports',
         'Esgrima':'Fencing',
         'Pesca':'Fishing',
         'Fútbol sala':'Five a side footbal',
         'Fútbol americano':'Football',
         'Golf':'Golf',
         'Gimnasia':'Gymnastics',
         'Balonmano':'Handball',
         'Senderismo':'Hiking',
         'Hockey':'Hockey',
         'Caza':'Hunting',
         'fútbol sala':'Indoor soccer',
         'Judo':'Judo',
         'Karate':'Karate',
         'Kickboxing':'Kickboxing',
         'Kung fu':'Kung fu',
         'Lacrosse':'Lacrosse',
         'salto de longitud':'Long jumping',
         'Artes marciales':'Martial arts',
         'Maratón':'Marathon',
         'Motorismo':'Motoring',
         'Automovilismo':'Motor racing ',
         'Motonáutica':'Motorboat racing',
         'Motociclismo':'Motorcycling',
         'Montañismo':'Mountaineering',
         'Ciclismo de montaña':'Mountain biking',
         'Paintball':'Paintball',
         'Pádel':'Paddel',
         'Paracaidismo':'Parachuting',
         'Parapente':'Paragliding',
         'Parkour':'Parkour',
         'Polo':'Polo',
         'Billar':'Pool',
         'Salto con pértiga':'Pole vault',
         'Ráquetbol':'Racquetball',
         'Canotaje':'Rafting',
         'Descenso con cuerdas':'Rapel',
         'Gimnasia rítmica':'Rhythmic gymnastics',
         'Anillas':'Rings',
         'Escalada':'Rock climbing',
         'Hockey sobre patines':'Rope jumping',
         'Remo':'Rowing',
         'Rugby':'Rugby',
         'Correr':'Running',
         'Vela':'Sailing',
         'Buceo':'Scuba diving',
         'Patinaje':'Skating',
         'Skateboard':'Skateboarding',
         'Esquí':'Skiing',
         'snowboard':'Snowboarding',
         'softbol':'Softball',
         'squash':'Squash',
         'estiramiento':'Streching',
         'Sumo':'Sumo',
         'Surf':'Surf',
         'natación':'Swimming',
         'Tenis de mesa':'Table tennis',
         'Taekwondo':'Taekwondo',
         'Tenis':'Tennis',
         'Salto de trampolín':'Trampolining',
          'Trapecio':'Trapeze',
         'Vóleibol':'Volleyball',
         'Deportes acuáticos':'Water sports',
         'Levantamiento de pesas':'Weight lifting',
         'Waterpolo':'Water polo',
         'Tabla a vela':'Windsurfing',
         'Esquí acuático':'Water skiing',
         'Deportes de invierno':'Winter sports',
         'Lucha':'Wrestling',
         'Atletas':'Athletes',
         'Bate de béisbol o raqueta de tenis de mesa':'Bat',
         'Botas':'Boots',
         'Campeón/ona':'Champion',
         'Campeonato':'Championship',
         'Palos de golf':'Clubs',
         'Deporte de contacto':'Contact Sport',
         'Casco protector':'Crash Helmet',
         'Multitud':'Crowd',
         'Jinete':'Jockey',
          'Equipamiento':'Equipment',
          'Balón de fútbol':'Football',
          'Guantes (boxeo)':'Gloves',
          'Vuelta':'Lap',
          'Perdedor':'Loser',
          'Juegos Olímpicos':'Olympic Games/Olympics',
         'Jugador/ra':'Player',
         'Disco de Hockey':'Puck',
          'Carrera':'Race',
         'Hipódromo':'Racetrack/Racecourse',
         'Raqueta de tenis':'Racket',
         'Arbitro de fútbol, rugby y baloncesto':'Referee',
         'Riesgo':'Risk',
         'Ring':'Ring',
         'Marcador':'Scoreboard',
         'Espectadores':'Spectators',
          'Patines':'Skates',
         'Piscina':'Swimming pool ',
         'Estadio':'Stadium',
         'Palo de Hockey':'Stick',
         'Espada (esgrima)':'Sword',
         'Entrenador':'Trainer/Coach',
         'Trofeo':'Trophy',
         'Pista':'Track',
         'Arbitro de béisbol y tenis':'Bounce',
         'Velódromo':'Velodrome',
          'Pito, Silbato':'Whistle',
         'Ganadores':'Winner',
         'Hacer rebotar la pelota':'Beat',
          'Vencer':'Catch',
         'Atrapar':'Cheer',
         'Animar, aplaudir':'Dive',
          'Tirarse clavados':'Drive',
         'Manejar':'Draw',
         'Caerse':'Fall',
         'Cabecear':'Head',
         'Golpear la pelota':'Hit',
          'Parar, dejar de hacer':'Give Up',
         'Ponerse en forma':'Get Fit',
         'Saltar  agua':'Jump',
         'Patear la pelota':'Kick',
         'Comenzar':'Kick Off',
         'Perder':'Lose',
         'Pasar':'Pass',
          'Montar':'Ride',
         'Correr':'Run',
         'Disparar':'Shoot',
         'Servir, saque':'Serve',
         'Patinar':'Skate',
          'Empezar':'Take Up',
         'Lanzar':'Throw',
         'Calentar':'Warm Up',
         'Ganar':'Win',} 

def buscar_palabra():
    palabra=input("Ingrese la palabra que desea buscar: ")
    for p in Ingles.keys():
        if palabra==p:
            print("La traduccion de la palabra",palabra,"al ingles, es : ",Ingles[p])
            return None 
        else:
            print('La palabra no esta en el diccionario')
            break

