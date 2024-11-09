class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()

musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 45.50

musica2 = Musica()
musica2.nome = 'Hotel California'
musica2.artista = 'Queen'
musica2.duracao = 45.50

musicas = [musica1,musica2]

print(vars(musica1))