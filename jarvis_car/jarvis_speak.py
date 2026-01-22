import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)

engine.say("Sistema iniciado. Estou pronto.")
engine.runAndWait()
