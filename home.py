import streamlit as st
import ML

def main(user_id, pdf_texts):
    # Initialize session state variables
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    if "pdf_texts" not in st.session_state:
        st.session_state["pdf_texts"] = []

    # Sidebar for uploading documents
    st.sidebar.title("Upload your Reports")
    pdf_docs = st.sidebar.file_uploader("Upload PDF documents", accept_multiple_files=True, type=["pdf", "jpeg", "png"])
    
    # Submit button
    submit = st.sidebar.button("Submit")

    if submit and pdf_docs:
        # Clear previous chat history and text extractions
        st.session_state["chat_history"] = []
        st.session_state["pdf_texts"] = []

        for doc in pdf_docs:
            if doc.type == 'application/pdf':
                pdf_text = ML.extract_text_from_pdf(doc)
            else:
                pdf_text = ML.extract_text_from_image(doc)

            # Check for extraction errors
            if "error" not in pdf_text.lower():
                st.session_state["pdf_texts"].append(pdf_text)
                st.session_state["chat_history"].append({"user_health_history": pdf_text})
            else:
                st.error(f"Error extracting text from file: {pdf_text}")

    # User input field
    user_input = st.text_input("Your message")

    # Information message
    st.markdown("<p style='font-size: small;'>Find the genomic analysis, disease prediction, and biomarker mapping based on uploaded report</p>", unsafe_allow_html=True)

    if user_input:
        # Combine all extracted texts and user input
        combined_texts = " ".join(st.session_state["pdf_texts"])
        combined_input = f"{combined_texts} {user_input}"

        # Determine the type of advice to generate
        if "genomic analysis" in user_input.lower():
            ai_response = ML.analyze_genomic_data(combined_input)
        elif "disease prediction" in user_input.lower():
            ai_response = ML.predict_disease(combined_input)
        elif "biomarker mapping" in user_input.lower():
            ai_response = ML.map_biomarkers_dynamically(combined_input)
        else:
            ai_response = "Please specify whether you want genomic analysis, disease prediction, or biomarker mapping."

        # Append the interaction to the chat history
        st.session_state["chat_history"].append({"user": user_input})
        st.session_state["chat_history"].append({"ai": ai_response})

    # Display chat history
    for chat in st.session_state.get("chat_history", []):
        if "user" in chat:
            st.markdown(f"<div style='text-align: right; font-weight: bold;'>User: {chat['user']}</div>", unsafe_allow_html=True)
        if "ai" in chat:
            st.markdown(f"<div style='text-align: left;'>Aicure Dynamics: {chat['ai']}</div>", unsafe_allow_html=True)
