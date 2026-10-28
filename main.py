import streamlit as st


def generate_bioplastic_resource(detected_fruit):
    # استخدام HTML لتلوين النصوص بنفس الألوان البرتقالية/الصفراء والحمراء في المتصفح
    BRIGHT_YELLOW = '<span style="color: #FFD700;">'
    RED = '<span style="color: #FF4B4B;">'
    RESET = '</span>'

    st.markdown(BRIGHT_YELLOW + "🤖 [AI System]: Scanning organic waste sample..." + RESET, unsafe_allow_html=True)
    st.markdown(f"✅ [AI Result]: Successful Detection - {detected_fruit} Peels", unsafe_allow_html=True)
    st.markdown(BRIGHT_YELLOW + "=" * 60 + RESET, unsafe_allow_html=True)

    if detected_fruit.lower() == "banana":
        recipe = (
                 "💡 OPTIMIZED BANANA BIOPLASTIC FORMULA:\n"
                "-----------------------------------------\n"
                "- Organic Material: Chopped & boiled banana peels\n"
                "- Distilled Water: 50 ml\n"
                "- Vegetable Glycerin: 5 ml (Higher dose needed to soften rigid banana fibers)\n"
                "- White Vinegar: 5 ml\n"
                "- Cornstarch: 10 grams\n"
                "- Curing Time: 48 hours in a dry room.\n"
                "👉 Resulting Properties: High tensile strength, best for rigid packaging."
        )
    elif detected_fruit.lower() == "apple":
        recipe = (
                💡 OPTIMIZED APPLE BIOPLASTIC FORMULA:\n"
                "-----------------------------------------\n"
                "- Organic Material: Blended apple skins\n"
                "- Distilled Water: 40 ml\n"
                "- Vegetable Glycerin: 3 ml (Lower dose needed because apples have natural pectin)\n"
                "- White Vinegar: 5 ml\n"
                "- Cornstarch: 8 grams\n"
                "- Curing Time: 36 hours.\n"
                "👉 Resulting Properties: High flexibility, best for organic wraps/foils."
        )
    else:
        recipe = "❌ Error: Material not recognized. Please scan either Banana or Apple peels."

    st.text(recipe)


# --- واجهة الويب باستخدام Streamlit ---
st.markdown('<span style="color: #FFD700; font-size: 24px; font-weight: bold;">=== ORGANIC WASTE SCANNER ===</span>',
            unsafe_allow_html=True)
st.write("Enter the detected fruit")

# بدلاً من input() في التيرمنال، نستخدم خياراً تفاعلياً في الموقع
choice_input = st.radio(
    "Select an option:",
    ("1. 🍌 Banana", "2. 🍎 Apple")
)

# زر لتوليد الوصفة
if st.button("Generate Recipe"):
    if "1" in choice_input:
        selected_fruit = "Banana"
    else:
        selected_fruit = "Apple"

    st.write("\n")
    generate_bioplastic_resource(selected_fruit)
