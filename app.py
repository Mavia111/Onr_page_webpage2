import streamlit as st
import string as string
# Set page title and icon
st.set_page_config(page_title="Simple Website", page_icon=":tada", layout="wide")
# Header Section
st.title("Welcome to My Website 🌟")
st.write("I have a lot of Experience in WordPress, Asp .Net MVC, PHP development, Android applications, and Desktop Application Developer. I can make a magnificent and Professional site and applications within an exceptionally brief timeframe. I love to work with customers from everywhere throughout the world. ")
st.image("https://dcassetcdn.com/design_img/1374323/111332/111332_7052801_1374323_3419ad9a_image.jpg");
# About Section
st.header("About Us")
st.write("""
I am a highly experienced **Web and App Developer** with extensive expertise in **WordPress, ASP.NET MVC, PHP development, Android applications, and desktop applications**. With a strong passion for technology and innovation, I specialize in creating **high-quality, professional websites and applications** tailored to meet diverse business needs.  

My ability to deliver **exceptional digital solutions** within a short timeframe sets me apart. Whether it's building a **dynamic website, a powerful eCommerce platform, or a feature-rich mobile or desktop application**, I ensure that every project is designed for **efficiency, scalability, and seamless user experience**.  

With years of hands-on experience, I have worked with **clients across the globe**, understanding their unique requirements and transforming their ideas into **functional, visually appealing, and high-performing digital products**. My expertise spans **custom WordPress development, complex ASP.NET MVC applications, PHP-based web solutions, and Android apps**, ensuring that businesses can **streamline their operations, enhance customer engagement, and drive growth**.  

I take pride in offering **innovative, result-driven solutions**, combining **modern design, intuitive navigation, and cutting-edge technology**. Whether you need a website, mobile app, or a full-fledged software solution, I am committed to delivering **top-tier results with precision and professionalism**.  

If you're looking for a skilled developer who can bring your vision to life, optimize performance, and deliver outstanding results **within a short timeframe**, let's collaborate and build something exceptional together.
""")

# Contact Form
st.header("Contact Us")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Send")
    
    if submit:
        st.success(f"Thank you, {name}! We'll get back to you soon.")

# Footer
st.markdown("---")
st.write("© 2025 My Website ")
