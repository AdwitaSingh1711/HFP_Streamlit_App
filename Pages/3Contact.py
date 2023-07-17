import streamlit as st

st.header(":mailbox: Get in Touch with Our Team!")
st.write("""
         We has rigorously worked on multiple AI models to bring to our users the most accurate analyis, for their health is our priority!

         We believe in transperancy, and if you have any reservations about our methods, feel free to contact us below. 
         """)

contact_form = """
<form action="https://formsubmit.co/adwita114btit21@email.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Review"></textarea>
     <button type="submit">Send</button>
</form>"""

st.markdown(contact_form, unsafe_allow_html=True)
st.write("##")
st.write("""
         We do not claim to be affiliated with any medical instituion nor do we claim to offer treatement.

         The algorithm promises to calculate the RISK of heart failure, and not time of heart failure itself 
         (We'll need a few more years for that. )
         
         """)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")