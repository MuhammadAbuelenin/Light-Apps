import PyPDF2 ,pyttsx3

# Target Pdf
path = open('Muhammad Abuelenin CV.pdf', 'rb')

# Reading PDF File
pdfReader = PyPDF2.PdfFileReader(path)

# Getting Speech
speak = pyttsx3.init()

# Loop fo all the pages
for p in range(pdfReader.numPages):
    text = pdfReader.getPage(p).extractText()
    speak.say(text)
    speak.runAndWait()

speak.save_to_file(text, 'speech1.mp3')

speak.stop()
path.close()

#################
# Anouther Script
import pyttsx3

# Create a string
string = "Lorem Ipsum is simply dummy text " \
         + "of the printing and typesetting industry."

# Initialize the Pyttsx3 engine
engine = pyttsx3.init()

# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'speech.mp3')

# Wait until above command is not finished.
engine.runAndWait()
