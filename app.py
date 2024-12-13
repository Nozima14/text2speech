import streamlit as st
import pyttsx3

# Streamlit sarlavha
st.title("Multilingual Text-to-Speech (TTS) Web App")
st.write("Matnni ovozga o'zgartiruvchi veb-dastur (Inglizcha, Ruscha, O'zbekcha)")

# Foydalanuvchi matn kiritishi
text_input = st.text_area("Matn kiriting:", "Salom, bu mening birinchi TTS dasturim!")

# Til tanlash
language = st.selectbox("Tilni tanlang:", ("Inglizcha", "Ruscha", "O'zbekcha"))

# Pyttsx3 TTS funksiyasi
def text_to_speech(text, lang):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if lang == "Inglizcha":
        engine.setProperty('voice', voices[0].id)  # Inglizcha ovoz (odatiy)
    elif lang == "Ruscha":
        engine.setProperty('voice', voices[2].id)  # Ruscha ovoz (mos keladigan ovozni tanlang)
    elif lang == "O'zbekcha":
        engine.setProperty('voice', voices[0].id)  # O'zbekcha uchun universal ovoz
    
    engine.save_to_file(text, 'output_audio.mp3')
    engine.runAndWait()

# Tugma bosilganda
if st.button("Ovozga o'zgartirish"):
    if text_input.strip():
        st.write(f"Ovoz hosil qilinmoqda ({language})...")
        text_to_speech(text_input, language)
        st.success("Ovoz muvaffaqiyatli hosil qilindi!")
        
        # Ovozli faylni ijro etish
        with open('output_audio.mp3', 'rb') as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
    else:
        st.error("Iltimos, matn kiriting!")
