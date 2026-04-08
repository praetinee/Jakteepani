import streamlit as st
from data_gumluk import gumluk_data
from data_kadumpa import kadumpa_data
from data_sahatcha import sahatcha_data
from data_puntu import puntu_data
from data_putta import putta_data
from data_ari import ari_data

# ตั้งค่าหน้าเพจ Streamlit
st.set_page_config(
    page_title="คำทำนายดวงดาวกำเนิด",
    page_icon="⭐",
    layout="centered"
)

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

# 2. รายชื่อภพทั้ง 12 ภพ และการเชื่อมโยงกับฐานข้อมูลคำทำนาย
houses = ["ลัคนา", "กดุมภะ", "สหัชชะ", "พันธุ", "ปุตตะ", "อริ", 
          "ปัตนิ", "มรณะ", "ศุภะ", "กัมมะ", "ลาภะ", "วินาศ"]

# ดึงข้อมูลจากไฟล์โมดูลมาผูกกับชื่อภพ
astrology_database = {
    "ลัคนา": {"title": "สถิตย์อยู่กับลัคนา (กุมลัคน์)", "data": gumluk_data},
    "กดุมภะ": {"title": "เป็นสองกับลัคนา (ภพกดุมภะ)", "data": kadumpa_data},
    "สหัชชะ": {"title": "เป็นสามกับลัคนา (ภพสหัชชะ)", "data": sahatcha_data},
    "พันธุ": {"title": "เป็นสี่กับลัคนา (ภพพันธุ)", "data": puntu_data},
    "ปุตตะ": {"title": "เป็นห้ากับลัคนา (ภพปุตตะ)", "data": putta_data},
    "อริ": {"title": "เป็นหกกับลัคนา (ภพอริ)", "data": ari_data},
    # ภพที่ 7-12 ยังไม่มีข้อมูลฐานข้อมูล แต่เปิดให้กรอกเพื่อโชว์ในตารางได้
}

# ส่วนหัวของแอปพลิเคชัน
st.markdown("<h1 style='text-align: center;'>⭐ คำทำนายดวงดาวกำเนิด</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 30px;'>ระบุดาวลงในภพต่างๆ เพื่อสร้างผังราศีจักรและอ่านคำทำนายจากคัมภีร์จักรทีปนี</p>", unsafe_allow_html=True)

# พื้นที่สำหรับเก็บค่าที่ผู้ใช้เลือก (แยกเก็บเป็นชื่อดาว และ เลขไทย)
selections_names = {}
selections_thai_nums = {}

# สร้างตัวแปร Placeholder เพื่อวาดตารางราศีจักรไว้ด้านบนสุด
grid_placeholder = st.empty()

st.divider()
st.subheader("📝 ระบุดาวลงในภพต่างๆ")

# สร้างช่องกรอกข้อมูลแบบ Multiselect (แสดงครบ 12 ภพ)
cols = st.columns(2)
for i, house in enumerate(houses):
    with cols[i % 2]:
        selected = st.multiselect(
            f"**{house}**", 
            options=list(planets_map.keys()), 
            key=f"sel_{house}",
            placeholder="เพิ่มดาวที่สถิต..."
        )
        if selected:
            selections_names[house] = selected
            selections_thai_nums[house] = [planets_map[p] for p in selected]

# ฟังก์ชันสำหรับสร้าง HTML ตาราง 12 ช่อง (ล็อคสัดส่วน 100%)
def generate_zodiac_grid(selections):
    layout = {
        (1, 1): "วินาศ", (1, 2): "ลัคนา", (1, 3): "กดุมภะ", (1, 4): "สหัชชะ",
        (2, 1): "ลาภะ",                                     (2, 4): "พันธุ",
        (3, 1): "กัมมะ",                                    (3, 4): "ปุตตะ",
        (4, 1): "ศุภะ",   (4, 2): "มรณะ",   (4, 3): "ปัตนิ",   (4, 4): "อริ"
    }

    html = '''
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(4, 1fr); 
                width: 100%; max-width: 500px; margin: 0 auto; border: 3px solid #1e293b; 
                background-color: #f8fafc; aspect-ratio: 1; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">
    '''

    for r in range(1, 5):
        for c in range(1, 5):
            if (r, c) in layout:
                house = layout[(r, c)]
                planets_str = " ".join(selections.get(house, []))
                l_mark = '<span style="color: #ef4444; font-size: 1.2rem; margin-right: 4px;">ล</span>' if house == "ลัคนา" else ''
                
                html += f'''
                <div style="grid-row: {r}; grid-column: {c}; border: 1px solid #cbd5e1; display: flex; flex-direction: column; padding: 6px;">
                    <span style="font-size: 0.75rem; color: #64748b; font-weight: 500;">{house}</span>
                    <div style="margin: auto; text-align: center; display: flex; align-items: center; justify-content: center; flex-wrap: wrap;">
                        {l_mark}
                        <span style="font-size: 1.25rem; font-weight: bold; color: #0f172a;">{planets_str}</span>
                    </div>
                </div>
                '''
            elif r == 2 and c == 2:
                html += f'''
                <div style="grid-row: 2 / 4; grid-column: 2 / 4; border: 1px solid #cbd5e1; display: flex; align-items: center; justify-content: center; background-color: #ffffff;">
                    <span style="color: #94a3b8; font-size: 1.5rem; font-weight: bold; letter-spacing: 2px;">ดวงราศีจักร</span>
                </div>
                '''
    html += '</div>'
    return html

# วาดตารางราศีจักรลงใน Placeholder
grid_placeholder.markdown(generate_zodiac_grid(selections_thai_nums), unsafe_allow_html=True)

st.divider()

# แสดงผลการทำนาย (กรองเฉพาะภพที่มีทั้งการเลือกดาว และมีข้อมูลในฐานข้อมูล)
if selections_names:
    st.subheader("✨ ผลการทำนาย")
    has_prediction = False
    
    # วนลูปตามภพที่ผู้ใช้เลือกมา
    for house, selected_planets in selections_names.items():
        # ตรวจสอบว่าภพนั้นมีข้อมูลคำทำนายในระบบหรือไม่
        if house in astrology_database:
            has_prediction = True
            db_info = astrology_database[house]
            position_title = db_info["title"]
            
            for planet in selected_planets:
                # ตรวจสอบว่าดาวดวงนั้นมีคำทำนายในภพนั้นหรือไม่
                if planet in db_info["data"]:
                    result_data = db_info["data"][planet]
                    
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
                            <span style="font-size: 14px; font-weight: 600; color: #64748b; letter-spacing: 0.5px;">{position_title}</span>
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
                
    if not has_prediction:
        st.info("💡 ท่านได้กรอกดาวลงในตารางราศีจักรแล้ว (คำทำนายในภพที่เลือกจะถูกอัปเดตเข้าระบบในภายหลัง)")
else:
    st.info("💡 โปรดเลือกดาวที่สถิตในตำแหน่งต่างๆ อย่างน้อย 1 ดวง เพื่อดูตารางและผลคำทำนาย")
