import speech_recognition as sr
import webbrowser
import os

def listen_and_open():
    r = sr.Recognizer()

    # Get microphone list (assuming the updated module has Microphone)
    microphone_list = sr.Microphone.list_microphone_names()
    for index, name in enumerate(microphone_list):
        print(f"Microphone with name '{name}' found for `Microphone(device_index={index})`")

    # Choose microphone (adjust index if needed)
    mic_index = 15  # Select the first microphone by default (or set it based on the list)

    while True:
        with sr.Microphone(device_index=mic_index) as source:  # Ensure source is created within the with block
            print("Listening...")
            r.adjust_for_ambient_noise(source)  # Call adjust_for_ambient_noise after creating source
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="el-GR").lower()
            print("You said: " + command)
            if "τάσο άνοιξε youtube" in command:
                print("Opening YouTube...")
                webbrowser.open('http://www.youtube.com')
            elif "τάσο άνοιξε excel" in command:
                print("Opening Excel...")
                os.system('start excel')
            else:
                print("Command not recognized, try again.")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


listen_and_open()
