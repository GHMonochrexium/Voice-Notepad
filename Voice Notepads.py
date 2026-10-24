import speech_recognition as sr
import tkinter as tk
screen = tk.Tk()
screen.configure(bg="Red")
screen.geometry("700x700")
screen.title("Voice Notepads")
def DetectSpeech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

# Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Say something!")
    
    # Capture the audio
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            print("Transcribing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google service; {e}")  
        t1.insert("end", text)   
def Clear():
    t1.delete("1.0","end-1c")
def SaveDetails():
    file=open("speech recognition.txt","a")
    file.write(t1.get("1.0","end-1c"))
    file.write("/n")
    file.close()

label1 = tk.Label(text="Voice Notepad",width=30,height=2,bg="blue",fg="red", font=("Arial",  25))
label1.place(x=50,y=100)
b1 = tk.Button(text="Click me to start recording..",width=25,height=2,bg="blue",fg="red", font=("Arial",  16),command=DetectSpeech)
b1.place(x=10,y=250)
t1 = tk.Text(width=30,height=5,fg="white",bg="blue")
t1.place(x=450,y=250)
b2 = tk.Button(text="Save",width=25,height=2,bg="Green",fg="White", font=("Arial",  15), command=SaveDetails)
b2.place(x=10,y=450)
b3 = tk.Button(text="Clear",width=25,height=2,bg="Yellow",fg="White", font=("Arial",  15), command=Clear)
b3.place(x=400,y=450)

screen.mainloop()