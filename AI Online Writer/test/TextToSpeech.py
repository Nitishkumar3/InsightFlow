import subprocess

text = "This Python script will execute the edge-tts --list-voices command and print the output to the console. Make sure to replace 'edge-tts' with the actual command if it's different, and adjust the code accordingly based on your programming language of choice if it's not Python."

# Define the command
command = [
    'edge-tts',
    '--voice', 'en-CA-LiamNeural',
    '--text', text,
    '--write-media', 'hi hello.mp3',
    '--write-subtitles', 'hello_in_arabic.vtt',
    '--rate=-10%'
]

# Run the command
subprocess.run(command)

