import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import google.generativeai as genai
import datetime
import random

def ai(prompt):
    # Set up the generation configuration
    genai.configure(api_key="AIzaSyAqip1JqptAc9n7l7JOKqOXDPvMJLDulf8")
    text = f"Gemini AI response for prompt: {prompt} \n ********\n\n"

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Load the generative model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
    )

    # Start a conversation
    convo = model.start_chat(history=[])

    # Send the prompt
    response = convo.send_message(prompt)

    # Access the text from the response using .text attribute
    text += response.text

    # Save response to a file
    if not os.path.exists("openai"):
        os.mkdir("openai")

    # Save the response in a text file
    #with open(f"openai/prompt-{random.randint(1,1243242)}.txt", 'w') as f:
    with open(f"openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

    # Return the generated text
    #return text


def say(text):  # Jarvis speaking
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8  # Increase pause threshold for longer commands
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")  # Use a single language code (en-IN or hi-IN)
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
        say("Sorry, I did not catch that. Could you repeat, please?")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        say("I'm having trouble connecting to the internet. Please check your connection.")
        return "None"
    return query


if __name__ == '__main__':
    say("Hello, I'm Jarvis AI")
    while True:
        query = takeCommand().lower()

        # Open popular websites based on voice command
        sites = [['youtube', 'https://www.youtube.com'],
                 ['wikipedia', 'https://www.wikipedia.com'],
                 ['google', 'https://www.google.com']]

        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {current_time}")

        if "open amazon music" in query or "open music" in query:
            say("Opening Amazon Music...")
            try:
                amazon_music_path = r"C:\Program Files\WindowsApps\AmazonMobileLLC.AmazonMusic_9.5.2.0_x86__kc6t79cpj4tp0\Amazon Music.exe"
                os.startfile(amazon_music_path)
            except Exception as e:
                print(f"Error opening Amazon Music: {e}")
                say("I couldn't open Amazon Music.")

        if "using generative ai" in query:
            prompt = query.replace("using generative ai", "").strip()
            say("Generating response using AI...")
            ai_response = ai(prompt=prompt)
            say("Here is the response:")
            print(ai_response)
            say(ai_response)

        if query == "none":
            continue
        if "stop" in query or "exit" in query:
            say("Goodbye!")
            break
