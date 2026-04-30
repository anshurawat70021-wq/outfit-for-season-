import streamlit as st

st.set_page_config(page_title="Aesthetic Outfit Finder", layout="wide")

st.title("✨ Aesthetic Outfit Suggestions 👗")
st.write("Choose a season and explore cute outfit ideas 💖")

season = st.selectbox("Select Season 🌸", ["Summer ☀️", "Winter ❄️", "Monsoon 🌧️", "Autumn 🍂"])

# Function to show images
def show_images(images):
    cols = st.columns(3)
    for i, img in enumerate(images):
        with cols[i % 3]:
            st.image(img, use_container_width=True)

# SUMMER
if season == "Summer ☀️":
    st.header("☀️ Cute Summer Outfits")
    images = [
        "https://images.unsplash.com/photo-1520975916090-3105956dac38",
        "https://images.unsplash.com/photo-1495121605193-b116b5b09a13",
        "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c",
        "https://images.unsplash.com/photo-1490481651871-ab68de25d43d",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.unsplash.com/photo-1483985988355-763728e1935b"
    ]
    show_images(images)

# WINTER
elif season == "Winter ❄️":
    st.header("❄️ Cozy Winter Outfits")
    images = [
        "https://images.unsplash.com/photo-1542060748-10c28b62716b",
        "https://images.unsplash.com/photo-1516826957135-700dedea698c",
        "https://images.unsplash.com/photo-1485968579580-b6d095142e6e",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.unsplash.com/photo-1521335629791-ce4aec67dd47",
        "https://images.unsplash.com/photo-1509631179647-0177331693ae"
    ]
    show_images(images)

# MONSOON
elif season == "Monsoon 🌧️":
    st.header("🌧️ Stylish Monsoon Outfits")
    images = [
        "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91",
        "https://images.unsplash.com/photo-1524504388940-b1c1722653e1",
        "https://images.unsplash.com/photo-1492707892479-7bc8d5a4ee93",
        "https://images.unsplash.com/photo-1503341455253-b2e723bb3dbb",
        "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f",
        "https://images.unsplash.com/photo-1496747611176-843222e1e57c"
    ]
    show_images(images)

# AUTUMN
elif season == "Autumn 🍂":
    st.header("🍂 Aesthetic Autumn Outfits")
    images = [
        "https://images.unsplash.com/photo-1475180098004-ca77a66827be",
        "https://images.unsplash.com/photo-1509631179647-0177331693ae",
        "https://images.unsplash.com/photo-1483985988355-763728e1935b",
        "https://images.unsplash.com/photo-1520974735194-9e89f7b45c3b",
        "https://images.unsplash.com/photo-1517841905240-472988babdf9",
        "https://images.unsplash.com/photo-1495121605193-b116b5b09a13"
    ]
    show_images(images)

st.write("💖 Stay stylish and confident!")
