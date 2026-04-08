import streamlit as st
from data_gumluk import gumluk_data
from data_kadumpa import kadumpa_data
from data_sahatcha import sahatcha_data
from data_puntu import puntu_data
from data_putta import putta_data
from data_ari import ari_data
from data_patni import patni_data
from data_morana import morana_data
from data_subha import subha_data
from data_kamma import kamma_data
from data_lapha import lapha_data
from data_winat import winat_data

# ตั้งค่าหน้าเพจ Streamlit เป็นแบบ Wide เพื่อให้มีพื้นที่สำหรับ 3 คอลัมน์
st.set_page_config(
    page_title="Chakkathipani",
    page_icon="⭐",
    layout="wide"
)

# ฝัง CSS เพื่อบังคับใช้ฟอนต์ Sarabun ทั้งหน้าเว็บ และจัดคอลัมน์กึ่งกลางแนวตั้ง
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"], div, span, h1, h2, h3, h4, h5, h6, p, a, label, button, input, select {
    font-family: 'Sarabun', sans-serif !important;
}

/* จัดกึ่งกลางคอลัมน์ตามแนวตั้ง */
[data-testid="stHorizontalBlock"] {
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

# 1. ฐานข้อมูลดาว และ การแปลงเป็นเลขไทยสำหรับตารางราศีจักร
planets_map = {
    "พระอาทิตย์ (1)": "๑",
    "พระจันทร์ (2)": "๒",
    "พระอังคาร (3)": "๓",
    "พระพุธ (4)": "๔",
    "พระพฤหัสบดี (5)": "๕",
    "พระศุกร์ (6)": "๖",
    "พระเสาร์ (7)": "๗",
    "พระราหู (8)": "๘",
}

# 2. รายชื่อภพทั้ง 12 ภพ
houses = ["ลัคนา", "กดุมภะ", "สหัชชะ", "พันธุ", "ปุตตะ", "อริ", 
          "ปัตนิ", "มรณะ", "ศุภะ", "กัมมะ", "ลาภะ", "วินาศ"]

# สร้าง Dictionary เพื่อเก็บชื่อสำหรับแสดงผลในช่องเลือกดาว
house_labels = {
    "ลัคนา": "สถิตร่วมกับลัคนา",
    "กดุมภะ": "สองจากลัคนา (กดุมภะ)",
    "สหัชชะ": "สามจากลัคนา (สหัชชะ)",
    "พันธุ": "สี่จากลัคนา (พันธุ)",
    "ปุตตะ": "ห้าจากลัคนา (ปุตตะ)",
    "อริ": "หกจากลัคนา (อริ)",
    "ปัตนิ": "เจ็ดจากลัคนา (ปัตนิ)",
    "มรณะ": "แปดจากลัคนา (มรณะ)",
    "ศุภะ": "เก้าจากลัคนา (ศุภะ)",
    "กัมมะ": "สิบจากลัคนา (กัมมะ)",
    "ลาภะ": "สิบเอ็ดจากลัคนา (ลาภะ)",
    "วินาศ": "สิบสองจากลัคนา (วินาศ)"
}

# ดึงข้อมูลจากไฟล์โมดูลมาผูกกับชื่อภพ
astrology_database = {
    "ลัคนา": {"title": "สถิตย์อยู่กับลัคนา (กุมลัคน์)", "data": gumluk_data},
    "กดุมภะ": {"title": "เป็นสองกับลัคนา (ภพกดุมภะ)", "data": kadumpa_data},
    "สหัชชะ": {"title": "เป็นสามกับลัคนา (ภพสหัชชะ)", "data": sahatcha_data},
    "พันธุ": {"title": "เป็นสี่กับลัคนา (ภพพันธุ)", "data": puntu_data},
    "ปุตตะ": {"title": "เป็นห้ากับลัคนา (ภพปุตตะ)", "data": putta_data},
    "อริ": {"title": "เป็นหกกับลัคนา (ภพอริ)", "data": ari_data},
    "ปัตนิ": {"title": "เป็นเจ็ดกับลัคนา (ภพปัตนิ)", "data": patni_data},
    "มรณะ": {"title": "เป็นแปดกับลัคนา (ภพมรณะ)", "data": morana_data},
    "ศุภะ": {"title": "เป็นเก้ากับลัคนา (ภพศุภะ)", "data": subha_data},
    "กัมมะ": {"title": "เป็นสิบกับลัคนา (ภพกัมมะ)", "data": kamma_data},
    "ลาภะ": {"title": "เป็นสิบเอ็ดกับลัคนา (ภพลาภะ)", "data": lapha_data},
    "วินาศ": {"title": "เป็นสิบสองกับลัคนา (ภพวินาศ)", "data": winat_data},
}

# ส่วนหัวของแอปพลิเคชัน
st.markdown("<h1 style='text-align: center;'>⭐ คำทำนายดวงดาวกำเนิด</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 30px;'>ระบุดาวลงในภพต่างๆ เพื่อสร้างผังราศีจักรและอ่านคำทำนายจากคัมภีร์จักรทีปนี</p>", unsafe_allow_html=True)
st.divider()

# สร้างพื้นที่แบบ 3 คอลัมน์ (ซ้าย:ราศีจักร 1.2 ส่วน, กลาง:ตัวเลือก 1 ส่วน, ขวา:คำแปล 1.5 ส่วน)
col_left, col_mid, col_right = st.columns([1.2, 1, 1.5], gap="large")

# ตัวแปรสำหรับเก็บค่าที่เลือก
selections_names = {}
selections_thai_nums = {}

# --- คอลัมน์กลาง: ตัวเลือกดาว (เรียงยาวลงมาแถวเดียว) ---
with col_mid:
    st.markdown("<h3 style='text-align: center; color: #334155; margin-bottom: 20px;'>📝 ระบุดาวสถิต</h3>", unsafe_allow_html=True)
    
    for house in houses:
        selected = st.multiselect(
            f"{house_labels[house]}", 
            options=list(planets_map.keys()), 
            key=f"sel_{house}",
            placeholder="เลือกดาว..."
        )
        if selected:
            selections_names[house] = selected
            selections_thai_nums[house] = [planets_map[p] for p in selected]

# ฟังก์ชันสำหรับสร้าง HTML ตาราง 12 ช่อง
def generate_zodiac_grid(selections):
    # แก้ไข Layout เป็นการเวียนทวนเข็มนาฬิกา ตามหลักโหราศาสตร์ไทย
    layout = {
        (1, 2): "ลัคนา", (1, 1): "กดุมภะ", (2, 1): "สหัชชะ", (3, 1): "พันธุ",
        (4, 1): "ปุตตะ", (4, 2): "อริ", (4, 3): "ปัตนิ", (4, 4): "มรณะ",
        (3, 4): "ศุภะ", (2, 4): "กัมมะ", (1, 4): "ลาภะ", (1, 3): "วินาศ"
    }

    html_parts = []
    # กำหนดฟอนต์ Sarabun ให้ตารางด้วย
    html_parts.append('<div style="font-family: \'Sarabun\', sans-serif; display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(4, 1fr); width: 100%; max-width: 600px; margin: 0 auto; border: 3px solid #1e293b; background-color: #f8fafc; aspect-ratio: 1; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">')

    for r in range(1, 5):
        for c in range(1, 5):
            if (r, c) in layout:
                house = layout[(r, c)]
                planets_str = " ".join(selections.get(house, []))
                l_mark = '<span style="color: #ef4444; font-size: 1.2rem; margin-right: 4px;">ล</span>' if house == "ลัคนา" else ''
                
                cell_html = f'<div style="grid-row: {r}; grid-column: {c}; border: 1px solid #cbd5e1; display: flex; flex-direction: column; padding: 8px;"><span style="font-size: 0.85rem; color: #64748b; font-weight: 500;">{house}</span><div style="margin: auto; text-align: center; display: flex; align-items: center; justify-content: center; flex-wrap: wrap;">{l_mark}<span style="font-size: 1.5rem; font-weight: bold; color: #0f172a;">{planets_str}</span></div></div>'
                html_parts.append(cell_html)
                
            elif r == 2 and c == 2:
                center_html = f'<div style="grid-row: 2 / 4; grid-column: 2 / 4; border: 1px solid #cbd5e1; display: flex; align-items: center; justify-content: center; background-color: #ffffff;"><span style="color: #94a3b8; font-size: 1.8rem; font-weight: bold; letter-spacing: 2px;">ดวงราศีจักร</span></div>'
                html_parts.append(center_html)
                
    html_parts.append('</div>')
    return "".join(html_parts)

# --- คอลัมน์ซ้าย: แสดงตารางราศีจักร ---
with col_left:
    st.markdown("<h3 style='text-align: center; color: #334155; margin-bottom: 20px;'>🔮 ดวงราศีจักร</h3>", unsafe_allow_html=True)
    st.markdown(generate_zodiac_grid(selections_thai_nums), unsafe_allow_html=True)

# --- คอลัมน์ขวา: แสดงผลคำทำนาย ---
with col_right:
    st.markdown("<h3 style='text-align: center; color: #334155; margin-bottom: 20px;'>✨ ความหมายดาว</h3>", unsafe_allow_html=True)
    
    if selections_names:
        has_prediction = False
        
        for house, selected_planets in selections_names.items():
            if house in astrology_database:
                has_prediction = True
                db_info = astrology_database[house]
                position_title = db_info["title"]
                
                for planet in selected_planets:
                    if planet in db_info["data"]:
                        result_data = db_info["data"][planet]
                        
                        html_card = (
                            f'<div style="font-family: \'Sarabun\', sans-serif; background-color: {result_data["bg"]}; border: 1px solid {result_data["border"]}; border-left: 6px solid {result_data["color"]}; padding: 24px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">'
                            f'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 12px;">'
                            f'<span style="font-size: 15px; font-weight: 600; color: #64748b; letter-spacing: 0.5px;">{position_title}</span>'
                            f'<span style="background-color: white; color: {result_data["color"]}; padding: 4px 14px; border-radius: 9999px; font-weight: bold; font-size: 14px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">{planet}</span>'
                            f'</div>'
                            f'<p style="font-size: 18px; color: #1e293b; margin: 0; line-height: 1.6;">"{result_data["text"]}"</p>'
                            f'</div>'
                        )
                        st.markdown(html_card, unsafe_allow_html=True)
                    
        if not has_prediction:
            st.info("ท่านได้กรอกดาวลงในตารางราศีจักรแล้ว (คำทำนายในภพที่เลือกจะถูกอัปเดตเข้าระบบในภายหลัง)")
    else:
        st.info("โปรดเลือกดาวที่สถิตในตำแหน่งต่างๆ เพื่อดูผลคำทำนาย")
