import streamlit as st

def generate_bioplastic_resource(detected_fruit, quantity):
    BRIGHT_YELLOW = '<span style="color: #FFD700;">'
    RED = '<span style="color: #FF4B4B;">'
    RESET = '</span>'

    st.markdown(BRIGHT_YELLOW + "🤖 [AI System]: Scanning organic waste sample..." + RESET, unsafe_allow_html=True)
    st.markdown(f"✅ [AI Result]: Successful Detection - {quantity}x {detected_fruit} Peels", unsafe_allow_html=True)
    st.markdown(BRIGHT_YELLOW + ("=" * 60) + RESET, unsafe_allow_html=True)

    if detected_fruit.lower() == "banana":
        # حساب الكميات بناءً على الكمية المدخلة
        water = 50 * quantity
        glycerin = 5 * quantity
        vinegar = 5 * quantity
        starch = 10 * quantity
        curing_time = 48
        
        recipe = (
            f"💡 OPTIMIZED BANANA BIOPLASTIC FORMULA (For {quantity} Peel/s):\n"
            f"-----------------------------------------\n"
            f"- Organic Material: Chopped & boiled {quantity} banana peel(s)\n"
            f"- Distilled Water: {water} ml\n"
            f"- Vegetable Glycerin: {glycerin} ml (Higher dose needed to soften rigid banana fibers)\n"
            f"- White Vinegar: {vinegar} ml\n"
            f"- Cornstarch: {starch} grams\n"
            f"- Curing Time: {curing_time} hours in a dry room.\n"
            f"👉 Resulting Properties: High tensile strength, best for rigid packaging."
        )
    elif detected_fruit.lower() == "apple":
        water = 40 * quantity
        glycerin = 3 * quantity
        vinegar = 5 * quantity
        starch = 8 * quantity
        curing_time = 36
        
        recipe = (
            f"💡 OPTIMIZED APPLE BIOPLASTIC FORMULA (For {quantity} Peel/s):\n"
            f"-----------------------------------------\n"
            f"- Organic Material: Blended {quantity} apple skin(s)\n"
            f"- Distilled Water: {water} ml\n"
            f"- Vegetable Glycerin: {glycerin} ml (Lower dose needed because apples have natural pectin)\n"
            f"- White Vinegar: {vinegar} ml\n"
            f"- Cornstarch: {starch} grams\n"
            f"- Curing Time: {curing_time} hours.\n"
            f"👉 Resulting Properties: High flexibility, best for organic wraps/foils."
        )
    else:
        recipe = "❌ Error: Material not recognized. Please scan either Banana or Apple peels."

    st.text(recipe)


# --- واجهة الويب باستخدام Streamlit ---
st.markdown('<span style="color: #FFD700; font-size: 24px; font-weight: bold;">=== ORGANIC WASTE SCANNER ===</span>', unsafe_allow_html=True)
st.write("Enter the detected fruit and quantity")

choice_input = st.radio(
    "Select an option:",
    ("1. 🍌 Banana", "2. 🍎 Apple")
)

# استخدام حقل رقمي يقبل الأعداد من 1 فصاعداً بلا حدود
quantity_input = st.number_input("Enter number of peels:", min_value=1, value=1, step=1)

if st.button("Generate Recipe"):
    if "1" in choice_input:
        selected_fruit = "Banana"
    else:
        selected_fruit = "Apple"

    st.write("\n")
    generate_bioplastic_resource(selected_fruit, quantity_input)
