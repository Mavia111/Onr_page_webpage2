
import streamlit as st

# Set page title and icon
st.set_page_config(page_title="T-Shirt Black - Product Page", page_icon="👕", layout="wide")

# Header Section
st.title("🖤 Classic Black T-Shirt")
st.subheader("Black is not a color, it’s an attitude.")

# Product Image & Details
st.image("https://radstore.pk/cdn/shop/products/IMG_7123_1080x.jpg?v=1615635326"  )

# Product Info in Columns
col1, col2 = st.columns([2, 1])  # Left (Details) | Right (Price & Button)

with col1:
    st.header("About This T-Shirt")
    st.write("""
    The **Classic Black T-Shirt** is a must-have wardrobe essential, offering timeless style and unmatched comfort. 
    Made from **premium cotton**, it delivers a **soft, breathable, and lightweight** feel for all-day wear.
     **Fade-resistant fabric**  
     **Perfect fit for men & women**  
     **Pairs well with jeans, joggers, or layered outfits**  
     **Available Sizes:** S, M, L, XL, XXL  
    """)

with col2:
    st.header("Price: **$19.99**")
    st.markdown('<a href="#" style="display: inline-block; padding: 10px 20px; font-size: 18px; color: white; background: black; text-align: center; border-radius: 5px; text-decoration: none;">Buy Now</a>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("© 2025 My Website | All rights reserved.")
