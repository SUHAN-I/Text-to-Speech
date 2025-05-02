from gtts import gTTS

# Step 1: Get text input from user
text = input("📋 Paste the text from your PDF and press Enter:\n")

# Step 2: Get desired mp3 file name
mp3_name = "output.mp3"

# Step 3: Convert text to speech
tts = gTTS(text)

# Step 4: Save the mp3
tts.save(mp3_name)

# Step 5: Notify user
print("✅ Your speech is saved as", mp3_name)
