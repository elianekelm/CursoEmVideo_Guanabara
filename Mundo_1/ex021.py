print('======== DESAFIO 021 ========')

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Pressione "ENTER" para interromper a música: ')

# Tocando mp3 em python