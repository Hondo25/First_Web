import streamlit as st 
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":wave:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    
local_css("style/style.css")


lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_C61K8f.json")


with st.container():
    st.subheader("Hi, I am Timothee :wave:")
    st.title("A Python Developer")
    st.write("""Hi, My name is Timothee. I am a full-time student at Wake Technical Community College in computer programming.
    I am passionate about computers and finding new ways to use my skills to be more efficient in day-to-day tasks.""")
    st.write("[LinKdin profile >](https://www.linkedin.com/in/timothee-chibashimba-b54573233/)")

with st.container():
    st.title("About This Project")
    
    st.write(
            """
            Hello,  Welcome to Tech With Timo website. This is a small project I was doing on the side. It is nothing fancy. It's just a page about Iron Man's last speech, nothing fancy, and at the bottom, it has a way that you can reach out to me through email. I had a little trouble deploying this project and making it public, but I also loved it because it forced me to learn more and research things I needed to know. Are you curious or have any questions on how I did this project? Where did I start? What were my resources? And how you can do the same thing in 3 days. Feel free to send me a message. Please let me know what I should turn this website into. Also, if you have any projects or ideas, let me know in the message section. Enjoy 
            """
        )











# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Iron Man")
        st.write("##")
        st.write(
            """
            Tony Stark: Everybody wants a happy ending, right? But it doesn't always roll that way. Maybe this time. I'm hoping if you play this back... it's in celebration. I hope families are reunited. I hope we get it back, in somewhat like a normal version of the planet has been restored, if there ever was such a thing.
            God, what a world. Universe now. If you told me 10 years ago that we weren't alone, let alone you know to this extent... I mean, I wouldn't have been surprised. But come on, you know. That epic forces of darkness and light that have come into play. And for better or worse, that's the reality Morgan's going to find a way to grow up in. So I found a private area to record a little greeting in case of an untimely death on my part. Not that death at any time is ever timely.

This time travel thing that we are going to pull off tomorrow... it's got me scratching my head about the survivability of all this. But then again that's the hero gig. Part of the journey is the end. What am I tripping for? Everything is going to work out exactly the way it's supposed to.

Tony Stark: I love you 3000.
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")



    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")
        
        contact_form = """
    <form action="https://formsubmit.co/tmartial123@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name: " required>
        <input type="email" name="email" placeholder="Your Email: " required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
