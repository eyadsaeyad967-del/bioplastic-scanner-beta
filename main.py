import streamlit as st
from google import genai
from PIL import Image

# إعدادات صفحة المتصفح (الاسم والشعار)
st.set_page_config(
    page_title="BioPlastic Scanner Beta",
    page_icon="🌱",
    layout="centered"
)

client = genai.Client(api_key="ضع_مفتاح_الجيميني_هنا")

def analyze_image_with_ai(image):
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                image, 
                "Analyze this image. Return your answer strictly in this exact format: [Fruit],[Number]. "
                "Where [Fruit] is either 'Banana' or 'Apple', and [Number] is the exact integer count of the peels visible in the image. "
                "Example: Banana,3 or Apple,2"
            ]
        )
        
        text_res = response.text.strip()
        parts = text_res.split(',')
        
        detected_fruit = parts[0].strip().capitalize()
        if "Banana" not in detected_fruit and "Apple" not in detected_fruit:
            detected_fruit = "Banana"
            
        detected_quantity = 1
        if len(parts) > 1:
            try:
                detected_quantity = int(''.join(filter(str.isdigit, parts[1])))
                if detected_quantity < 1:
                    detected_quantity = 1
            except:
                detected_quantity = 1
                
        return detected_fruit, detected_quantity
        
    except Exception as e:
        return "Banana", 1

def generate_bioplastic_resource(detected_fruit, quantity, lang):
    BRIGHT_YELLOW = '<span style="color: #FFD700;">'
    RESET = '</span>'

    if lang == "العربية":
        fruit_name = "موز" if detected_fruit.lower() == "banana" else "تفاح"
        st.markdown(BRIGHT_YELLOW + "🤖 [نظام الذكاء الاصطناعي (Gemini)]: تم تحليل الصورة والتعرف على العينة والعدد..." + RESET, unsafe_allow_html=True)
        st.markdown(f"✅ [نتيجة الذكاء الاصطناعي]: تم اكتشاف - {quantity}x قشور {fruit_name}", unsafe_allow_html=True)
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
        st.markdown(BRIGHT_YELLOW + "🤖 [AI System (Gemini)]: Image analyzed successfully (Type & Count detected)..." + RESET, unsafe_allow_html=True)
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


language = st.sidebar.selectbox("Choose Language / اختر اللغة", ("English", "العربية"), index=1)

if language == "العربية":
    st.markdown('<span style="color: #FFD700; font-size: 24px; font-weight: bold; direction: rtl; display: block; text-align: center;">=== BioPlastic Scanner Beta ===</span>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #888; font-size: 14px;">إعداد المطورين: إياد الزرعة & عمار الزهراني</p>', unsafe_allow_html=True)
    st.write("الرجاء اختيار طريقة الإدخال:")
    
    method = st.radio(
        "اختر الطريقة:",
        ("1. ⚙️ الاختيار اليدوي (نوع + عدد)", "2. 📸 التعرف التلقائي بالذكاء الاصطناعي (النوع + العدد من الصورة)")
    )
    
    if "1" in method:
        choice_input = st.selectbox("اختر نوع الفاكهة:", ("🍌 موز (Banana)", "🍎 تفاح (Apple)"))
        quantity_input = st.number_input("أدخل عدد القشور:", min_value=1, value=1, step=1)
        button_text = "توليد الوصفة"
        camera_image = None
    else:
        camera_image = st.camera_input("التقط صورة للقشور (سيقوم الذكاء الاصطناعي بتحديد النوع والعدد تلقائياً)")
        button_text = "تحليل وتوليد الوصفة تلقائياً"

else:
    st.markdown('<span style="color: #FFD700; font-size: 24px; font-weight: bold; text-align: block;">=== BioPlastic Scanner Beta ===</span>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #888; font-size: 14px;">Developers: Eyad Al-Zarah & Ammar Al-Zahrani</p>', unsafe_allow_html=True)
    st.write("Please select your preferred input method:")
    
    method = st.radio(
        "Select method:",
        ("1. ⚙️ Manual Selection (Type + Count)", "2. 📸 AI Auto-Detection (Type + Count from Image)")
    )
    
    if "1" in method:
        choice_input = st.selectbox("Select fruit type:", ("🍌 Banana", "🍎 Apple"))
        quantity_input = st.number_input("Enter number of peels:", min_value=1, value=1, step=1)
        button_text = "Generate Recipe"
        camera_image = None
    else:
        camera_image = st.camera_input("Take a picture (AI will detect type and quantity automatically)")
        button_text = "Analyze & Generate Recipe Automatically"

if st.button(button_text):
    if camera_image is not None:
        img = Image.open(camera_image)
        with st.spinner("Analyzing image with Gemini AI (Detecting Fruit & Count)..." if language != "العربية" else "جاري تحليل الصورة بواسطة ذكاء Gemini (استخراج النوع والعدد)..."):
            selected_fruit, quantity_input = analyze_image_with_ai(img)
    else:
        if "موز" in choice_input or "Banana" in choice_input:
            selected_fruit = "Banana"
        else:
            selected_fruit = "Apple"

    st.write("\n")
    generate_bioplastic_resource(selected_fruit, quantity_input, language)