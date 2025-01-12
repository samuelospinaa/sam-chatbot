import streamlit as st
import backend

# Main page configuration
st.set_page_config(page_title="Sam Chatbot", page_icon="./public/sam.svg", layout="centered", initial_sidebar_state="collapsed")

# Initialize state in `st.session_state`
if "theme" not in st.session_state:
    st.session_state["theme"] = "Claro"  # Default theme
if "text_size" not in st.session_state:
    st.session_state["text_size"] = 14  # Default text size

# Change background color
def background_color_claro():
    st.session_state["theme"] = "Claro"

def background_color_oscuro():
    st.session_state["theme"] = "Oscuro"

# Change text size
def apply_text_size(size_chat):
    st.session_state["text_size"] = size_chat

# Apply dynamic styles according to theme and text size
if st.session_state["theme"] == "Claro":
    st.markdown("""
        <style>
        body {
            background-color: white;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body {
            background-color: #2c2f33;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

st.markdown(f"""
    <style>
    body {{
        font-size: {st.session_state["text_size"]}px;
    }}
    </style>
""", unsafe_allow_html=True)

# Main title with image
col1, col2 = st.columns([1, 8])  # Adjust proportions
with col1:
    st.image("./public/sam.svg", width=80)
with col2:
    st.title("Sam Chatbot")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's happening?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display assistant response
    with st.chat_message("assistant"):
        response = backend.run_chat(prompt)
        st.markdown(response)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})