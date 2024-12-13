import streamlit as st
from gtts import gTTS

# Streamlit sarlavha
st.title("Multilingual Text-to-Speech (TTS) Web App")
st.write("Matnni ovozga o'zgartiruvchi veb-dastur (Inglizcha, Ruscha, O'zbekcha)")

# Foydalanuvchi matn kiritishi
text_input = st.text_area("Matn kiriting:", "Salom, bu mening birinchi TTS dasturim!")

# Til tanlash
language = st.selectbox("Tilni tanlang:", ("Inglizcha", "Ruscha", "O'zbekcha"))

# Til kodi moslamasi
lang_code = {"Inglizcha": "en", "Ruscha": "ru", "O'zbekcha": "uz"}

# Tugma bosilganda
if st.button("Ovozga o'zgartirish"):
    if text_input.strip():
        st.write(f"Ovoz hosil qilinmoqda ({language})...")
        tts = gTTS(text=text_input, lang=lang_code[language])
        tts.save("output_audio.mp3")
        st.success("Ovoz muvaffaqiyatli hosil qilindi!")
        
        # Ovozli faylni ijro etish
        with open("output_audio.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
    else:
        st.error("Iltimos, matn kiriting!")
