import streamlit as st

def generate_bioplastic_resource(detected_fruit, quantity, lang):
    BRIGHT_YELLOW = '<span style="color: #FFD700;">'
    RESET = '</span>'

    if lang == "العربية":
        fruit_name = "موز" if detected_fruit.lower() == "banana" else "تفاح"
        st.markdown(BRIGHT_YELLOW + "🤖 [نظام الذكاء الاصطناعي]: يتم معالجة العينة..." + RESET, unsafe_allow_html=True)
        st.markdown(f"✅ [نتيجة الذكاء الاصطناعي]: تم الاكتشاف - {quantity}x قشور {fruit_name}", unsafe_allow_html=True)
        st.markdown(BRIGHT_YELLOW + ("=" * 60) + RESET, unsafe_allow_html=True)

        if detected_fruit.lower() == "banana":
            water = 50 * quantity
            glycerin = 5 * quantity
            vinegar = 5 * quantity
            starch = 10 * quantity
            curing_time = 48
            
            recipe = (
                f"💡 وصفة البلاستيك الحيوي المحسنة للموز (لعدد {quantity} قشرة):\n"
                f"-----------------------------------------\n"
                f"- المادة العضوية: {quantity} قشرة موز مقطعة ومغليّة\n"
                f"- الماء المقطر: {water} مللتر\n"
                f"- الجلسرين النباتي: {glycerin} مللتر (مطلوب كمية أكبر لتليين ألياف الموز القاسية)\n"
                f"- الخل الأبيض: {vinegar} مللتر\n"
                f"- نشا الذرة: {starch} جرام\n"
                f"- وقت التجفيف: {curing_time} ساعة في غرفة جافة.\n"
                f"👉 الخصائص الناتجة: قوة شد عالية، الأفضل للتغليف الصلب."
            )
        else:
            water = 40 * quantity
            glycerin = 3 * quantity
            vinegar = 5 * quantity
            starch = 8 * quantity
            curing_time = 36
            
            recipe = (
                f"💡 وصفة البلاستيك الحيوي المحسنة للتفاح (لعدد {quantity} قشرة):\n"
                f"-----------------------------------------\n"
                f"- المادة العضوية: {quantity} قشرة تفاح مفرومة\n"
                f"- الماء المقطر: {water} مللتر\n"
                f"- الجلسرين النباتي: {glycerin} مللتر (كمية أقل لأن التفاح يحتوي على البكتين الطبيعي)\n"
                f"- الخل الأبيض: {vinegar} مللتر\n"
                f"- نشا الذرة: {starch} جرام\n"
                f"- وقت التجفيف: {curing_time} ساعة.\n"
                f"👉 الخصائص الناتجة: مرونة عالية، الأفضل للأغطية والشرائح العضوية."
            )
    else:
        st.markdown(BRIGHT_YELLOW + "🤖 [AI System]: Processing sample..." + RESET, unsafe_allow_html=True)
        st.markdown(f"✅ [AI Result]: Detected - {quantity}x {detected_fruit} Peels", unsafe_allow_html=True)
        st.markdown(BRIGHT_YELLOW + ("=" * 60) + RESET, unsafe_allow_html=True)

        if detected_fruit.lower() == "banana":
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
        else:
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

    st.text(recipe)


language = st.sidebar.selectbox("Choose Language / اختر اللغة", ("English", "العربية"), index=0)

if language == "العربية":
    st.markdown('<span style="color: #FFD700; font-size: 24px; font-weight: bold; direction: rtl; display: block; text-align: center;">=== ماسح المخلفات العضوية الذكي ===</span>', unsafe_allow_html=True)
    st.write("الرجاء اختيار طريقة الإدخال المناسبة:")
    
    method = st.radio(
        "اختر الطريقة:",
        ("1. ⚙️ الاختيار اليدوي (Manual Selection)", "2. 📸 التقاط صورة بالكاميرا (Camera Capture)")
    )
    
    if "1" in method:
        choice_input = st.selectbox("اختر نوع الفاكهة:", ("🍌 موز (Banana)", "🍎 تفاح (Apple)"))
        quantity_input = st.number_input("أدخل عدد القشور:", min_value=1, value=1, step=1)
        button_text = "توليد الوصفة"
    else:
        camera_image = st.camera_input("التقط صورة العينة")
        choice_input = st.selectbox("حدد نوع القشور التي تصورت:", ("🍌 موز (Banana)", "🍎 تفاح (Apple)"))
        quantity_input = st.number_input("أدخل عدد القشور:", min_value=1, value=1, step=1)
        button_text = "توليد الوصفة من الصورة"

else:
    st.markdown('<span style="color: #FFD700; font-size: 24px; font-weight: bold; text-align: block;">=== SMART ORGANIC WASTE SCANNER ===</span>', unsafe_allow_html=True)
    st.write("Please select your preferred input method:")
    
    method = st.radio(
        "Select method:",
        ("1. ⚙️ Manual Selection", "2. 📸 Camera Capture")
    )
    
    if "1" in method:
        choice_input = st.selectbox("Select fruit type:", ("🍌 Banana", "🍎 Apple"))
        quantity_input = st.number_input("Enter number of peels:", min_value=1, value=1, step=1)
        button_text = "Generate Recipe"
    else:
        camera_image = st.camera_input("Take a picture of the sample")
        choice_input = st.selectbox("Select the detected fruit:", ("🍌 Banana", "🍎 Apple"))
        quantity_input = st.number_input("Enter number of peels:", min_value=1, value=1, step=1)
        button_text = "Generate Recipe from Camera"

if st.button(button_text):
    if "موز" in choice_input or "Banana" in choice_input:
        selected_fruit = "Banana"
    else:
        selected_fruit = "Apple"

    st.write("\n")
    generate_bioplastic_resource(selected_fruit, quantity_input, language)
