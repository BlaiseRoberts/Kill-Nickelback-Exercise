songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('Will.i.am', 'FIYAH')
}

no_nickelback = {song for song in songs if 'Nickelback' not in song}
print(no_nickelback)