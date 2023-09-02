import pyttsx3
import pygame
import time
import threading

engine = pyttsx3.init()

print("Hello! What song would you like me to play? (Please input the name of the songs. Will be shown below)")
print("Available songs: ")

print("mimosa boss fight ost")
print("friend of mine by avicii")
print("perfect drug")
print("when i'm gone")
print("sky full of stars")
print("wake me up by avicii")
print("the nights by avicii")
print("waiting for love by avicii")
print("without you by avicii")
print("levels by avicii")
print("what would i change it to by avicii")
print("hey brother by avicii")
print("broken arrows by avicii")
print("lonely boy by the black keys")
print("perfect strangers by jonas blue")
print("maroon 5 memories")
print("whirring")
print("too big to fail")
print("happier by marshmello")
print("free radicals")
print("fast as you can")
print("in a blink")
print("face my fears")
print("silhouettes by avicii")
print("the beacon")

engine.say("Activating Music Player. Type exit or quit to cancel.")
engine.runAndWait()

pygame.mixer.init()
last_input_time = time.time()
is_listening = True

def handle_input():
    global is_listening, last_input_time
    
    while is_listening:
        text = input("Enter the song you want to play: ")

        if "exit" in text or "quit" in text:
         print("Exiting the program. Goodbye!")
         is_listening = False
         return None

        if "mimosa boss fight ost" in text:
         print("Playing My Heart Feels No Pain. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\OST.mp3")
         return r"c:\Users\User\Documents\Music\OST.mp3"

        elif "friend of mine by avicii" in text:
         print("Playing Friend Of Mine. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Avicii - Friend Of Mine.mp3")
         return r"c:\Users\User\Documents\Music\Avicii - Friend Of Mine.mp3"

        elif "perfect drug" in text:
         print("Playing Perfect Drug. . .")
         pygame.mixer.music.load(r"c:\Users\User\Documents\Music\Hi-Fi Rush Soundtrack - Kale Boss Music (Nine Inch Nails - The Perfect Drug).mp3")
         return r"c:\Users\User\Documents\Music\Hi-Fi Rush Soundtrack - Kale Boss Music (Nine Inch Nails - The Perfect Drug).mp3"
        
        elif "when i'm gone" in text:
         print("Playing When I'm Gone. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Peekaboo - When I'm Gone (feat. XAELO).mp3")
         return r"C:\Users\User\Documents\Music\Peekaboo - When I'm Gone (feat. XAELO).mp3"

        elif "sky full of stars" in text:
         print("Playing A Sky Full Of Stars. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Coldplay - A Sky Full Of Stars.mp3")
         return r"c:\Users\User\Documents\Music\Coldplay - A Sky Full Of Stars.mp3"
 
        elif "wake me up by avicii" in text:
         print("Playing Wake Me Up. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Avicii - Wake Me Up.mp3")
         return r"c:\Users\User\Documents\Music\Avicii - A Sky Full Of Stars.mp3"
        
        elif "the nights by avicii" in text:
         print("Playing The Nights. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Avicii - The Nights.mp3")
         return r"c:\Users\User\Documents\Music\Avicii - The Nights.mp3"
        
        elif "waiting for love by avicii" in text:
         print("Playing Waiting For Love. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Avicii - Waiting For Love.mp3")
         return r"c:\Users\User\Documents\Music\Avicii - Waiting For Love.mp3"

        elif "without you by avicii" in text:
         print("Playing Without You. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Avicii - Without You.mp3")
         return r"c:\Users\User\Documents\Music\Avicii - Without You.mp3"

        elif "levels by avicii" in text:
         print("Playing Levels. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Levels - Avicii.mp3")
         return r"c:\Users\User\Documents\Music\Levels - Avicii.mp3"

        elif "what would i change it to by avicii" in text:
         print("Playing What Would I Change It To. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Avicii - What Would I Change It To.mp3")
         return r"c:\Users\User\Documents\Music\Avicii - What Would I Change It To.mp3"
        
        elif "hey brother by avicii" in text:
         print("Playing Hey Brother. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Avicii - Hey Brother.mp3")
         return r"c:\Users\User\Documents\Music\Avicii - Hey Brother.mp3"

        elif "broken arrows by avicii" in text:
         print("Playing Broken Arrows. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Avicii - Broken Arrows.mp3")
         return r"c:\Users\User\Documents\Music\Avicii - Broken Arrows.mp3"

        elif "lonely boy by the black keys" in text:
         print("Playing Lonely Boy. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\The Black Keys - Lonely Boy.mp3")
         return r"c:\users\user\Documents\Music\The Black Keys - Lonely Boy.mp3"

        elif "perfect strangers by jonas blue" in text:
         print("Playing Perfect Strangers. . .")
         pygame.mixer.music.load(r"c:\Users\User\Documents\Music\Perfect Strangers - Jonas Blue.mp3")
         return r"c:\Users\User\Documents\Music\Perfect Strangers - Jonas Blue.mp3"
 
        elif "maroon 5 memories" in text:
         print("Playing Maroon 5 - Memories. . .")
         pygame.mixer.music.load(r"c:\Users\User\Documents\Music\Maroon 5 - Memories.mp3")
         return r"c:\Users\User\Documents\Music\Maroon 5 - Memories.mp3"

        elif "whirring" in text:
         print("Playing Whirring. . .")
         pygame.mixer.music.load(r"c:\Users\User\Documents\Music\Whirring.mp3")
         return r"c:\Users\User\Documents\Music\Whiriing.mp3"
    
        elif "too big to fail" in text:
         print("Playing too big to fail. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Hi-Fi Rush OST Too Big to Fail(QA-1ML Boss).mp3")
         return r"c:\Users\User\Documents\Music\Hi-Fi Rush OST Too Big to Fail(QA-1ML Boss).mp3"

        elif "happier by marshmello" in text:
         print("Playing Happier By Marshmello. . .")
         pygame.mixer.music.load(r"C:\Users\User\Documents\Music\Marshmello ft. Bastille - Happier.mp3")
         return r"c:\Users\User\Documents\Music\Marshmello ft. Bastille - Happier.mp3"

        elif "free redicals" in text:
         print("Playing Flaming Lips - Free Radicals Elsinore Cover. . .")
         pygame.mixer.music.load(r"c:\Users\User\Documents\Music\Hi-Fi Rush Soundtrack - Rekka Boss Music (Flaming Lips - Free Radicals Elsinore Cover).mp3")
         return r"c:\Users\User\Documents\Music\Hi-Fi Rush Soundtrack - Rekka Boss Music (Flaming Lips - Free Radicals Elsinore Cover).mp3"

        elif "fast as you can" in text:
         print("Playing fast as you can. . .")
         pygame.mixer.music.load(r'c:\Users\User\Documents\Music\Fiona Apple - Fast As You Can.mp3')
         return r"c:\Users\User\Documents\Music\Fiona Apple - Fast As You Can.mp3"

        elif "in a blink" in text:
         print("Playing In A Blink. . .")
         pygame.mixer.music.load(r"c:\Users\User\Documents\Music\Hi-Fi Rush OST In a Blink.mp3")
         return r"c:\Users\User\Documents\Music\Hi-Fi Rush OST In a Blink.mp3"

        elif "face my fears" in text:
         print("Playing Face My Fears. . .")
         pygame.mixer.music.load(r"c:\Users\User\Documents\Music\Hikaru Utada, Skrillex - Face My Fears.mp3")
         return r"c:\Users\User\Documents\Music\Hikaru Utada, Skrillex - Face My Fears.mp3"

        elif "silhouettes by avicii" in text:
         print("Playing Silhouettes By Avicii. . .")
         pygame.mixer.music.load(r"c:\Users\User\Documents\Music\Avicii - Silhouettes.mp3")
         return r"c:\Users\User\Documents\Music\Avicii - Silhouettes.mp3"

        elif "the beacon" in text:
         print("Playing Hi-Fi Rush OST The Beacon. . .")
         pygame.mixer.music.load(r"c:\Users\User\Documents\Music\Hi-Fi Rush OST The Beacon.mp3")
         return r"c:\Users\User\Documents\Music\Hi-Fi Rush OST The Beacon.mp3"
    
    


        else:
         print("Song not found!")
         return None
    
    
    return None
    

def play_music(file_path):
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)



def music_player():
    global is_listening, last_input_time

    while is_listening:
        song_file = handle_input()
        if song_file:
            play_music(song_file)
            pygame.mixer.music.fadeout(2000)
            last_input_time = time.time()

music_player_thread = threading.Thread(target=music_player)
music_player_thread.start()

music_player_thread.join()

pygame.mixer.music.stop()
pygame.mixer.quit()