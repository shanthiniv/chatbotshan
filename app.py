import streamlit as st

st.title('Gemini AI Assistant')

st.write('## Enter your question:')
user_question = st.text_input('')

st.write('## Upload an image (optional):')
uploaded_file = st.file_uploader('', type=['jpg', 'jpeg', 'png'])

if st.button('Ask'):
    st.write('Response: "Gemini" can refer to a few different things. To give you the best answer, I need a little more context. Could you please clarify what you\'re asking about?')
    st.write('For example, are you interested in:')
    st.write('- **The Gemini constellation?** This is a constellation in the Northern Hemisphere, known for its bright stars Castor and Pollux.')
    st.write('- **The Gemini spacecraft?** This was a series of American crewed spacecraft used in the early days of the space race.')
    st.write('- **The Gemini project?** This was NASA\'s program that developed the Gemini spacecraft and conducted human spaceflights in the mid-1960s.')
    st.write('- **The Gemini AI model?** This is a large language model developed by Google AI, similar to ChatGPT.')
    st.write('- **The astrological sign Gemini?** This is one of the twelve signs of the zodiac, associated with the element Air and known for its adaptability, communication skills, and dualistic nature.')
