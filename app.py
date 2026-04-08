import streamlit as st
from data_gumluk import gumluk_data
from data_kadumpa import kadumpa_data

# ตั้งค่าหน้าเพจ Streamlit
st.set_page_config(
    page_title="คำทำนายดวงดาวกำเนิด",
    page_icon="⭐",
    layout="centered"
)

# โครงสร้างฐานข้อมูลถูกแยกไปอยู่ในไฟล์โมดูลแล้ว และดึงมารวมกันที่นี่
astrology_database = {
    "สถิตย์อยู่กับลัคนา (กุมลัคน์)": gumluk_data,
    "เป็นสองกับลัคนา (ภพกดุมภะ)": kadumpa_data
}

# ส่วนหัวของแอปพลิเคชัน
st.markdown("<h1 style='text-align: center;'>⭐ คำทำนายดวงดาวกำเนิด</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b;'>ระบุดาวที่สถิตในภพต่างๆ เพื่ออ่านคำทำนายจากคัมภีร์โหราศาสตร์จักรทีปนี</p>", unsafe_allow_html=True)
st.divider()

st.subheader("📖 ผูกดวงวางลัคนา")

selections = {}

# สร้างช่องเลือก (Multiselect) สำหรับแต่ละภพ เพื่อให้เลือกดาวได้หลายดวง
for position, planets_data in astrology_database.items():
    choices = st.multiselect(
        f"**{position}**", 
        options=list(planets_data.keys()),
        placeholder="คลิกเพื่อเลือกดาว (เลือกได้มากกว่า 1 ดวง)",
        key=position
    )
    
    if choices:
        selections[position] = choices

st.divider()

# แสดงผลการทำนาย
if selections:
    st.subheader("✨ ผลการทำนาย")
    
    # วนลูปตามภพ และดาวทั้งหมดที่เลือกในภพนั้นๆ
    for pos, selected_planets in selections.items():
        for planet in selected_planets:
            result_data = astrology_database[pos][planet]
            
            # ใช้ HTML และ CSS ตกแต่งกล่องข้อความ
            html_card = f"""
            <div style="
                background-color: {result_data['bg']}; 
                border: 1px solid {result_data['border']};
                border-left: 6px solid {result_data['color']};
                padding: 24px; 
                border-radius: 12px; 
                margin-bottom: 20px; 
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            ">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 12px;">
                    <span style="font-size: 14px; font-weight: 600; color: #64748b; letter-spacing: 0.5px;">{pos}</span>
                    <span style="background-color: white; color: {result_data['color']}; padding: 4px 12px; border-radius: 9999px; font-weight: bold; font-size: 14px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                        {planet}
                    </span>
                </div>
                <p style="font-size: 18px; color: #1e293b; margin: 0; line-height: 1.6; font-family: 'Sarabun', sans-serif;">
                    "{result_data['text']}"
                </p>
            </div>
            """
            st.markdown(html_card, unsafe_allow_html=True)
else:
    st.info("💡 โปรดเลือกดาวที่สถิตในตำแหน่งต่างๆ อย่างน้อย 1 ดวง เพื่อดูผลคำทำนาย")
