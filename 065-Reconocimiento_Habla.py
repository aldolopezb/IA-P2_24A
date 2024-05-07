#Aldo López Barrios
#21310106
#--------------------------
import speech_recognition as sr

# Crear un objeto Recognizer
recognizer = sr.Recognizer()

# Capturar audio del micrófono
with sr.Microphone() as source:
    print("Diga algo:")
    audio = recognizer.listen(source)

# Utilizar el reconocedor de voz de Google
try:
    print("Google Speech Recognition:")
    print(recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition no pudo entender el audio")
except sr.RequestError as e:
    print("No se pudo obtener respuesta desde Google Speech Recognition; {0}".format(e))
