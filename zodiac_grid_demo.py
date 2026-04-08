import streamlit as st

st.set_page_config(page_title="ระบบตารางราศีจักร", page_icon="🔮", layout="centered")

st.markdown("<h2 style='text-align: center;'>🔮 ตารางผังราศีจักร (ดวงอีแปะ)</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 30px;'>เลือกดาวจากเมนูด้านล่าง ตัวเลขจะไปปรากฏบนตารางโดยอัตโนมัติ</p>", unsafe_allow_html=True)

# 1. ฐานข้อมูลดาว และ การแปลงเป็นเลขไทย
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

# รายชื่อภพทั้ง 12 ภพ (เรียงตามลำดับโหราศาสตร์ไทย)
houses = ["ลัคนา", "กดุมภะ", "สหัชชะ", "พันธุ", "ปุตตะ", "อริ", 
          "ปัตนิ", "มรณะ", "ศุภะ", "กัมมะ", "ลาภะ", "วินาศ"]

# 2. พื้นที่สำหรับเก็บค่าที่ผู้ใช้เลือก
selections = {}

# สร้างตัวแปร Placeholder เพื่อให้วาดตารางราศีจักรไว้ "ด้านบน" ก่อนที่จะเรนเดอร์ช่องเลือกดาว
grid_placeholder = st.empty()

st.divider()
st.subheader("📝 ระบุดาวลงในภพต่างๆ")

# 3. สร้างช่องกรอกข้อมูลแบบ Multiselect แบ่งเป็น 2 คอลัมน์ให้ดูสวยงาม
cols = st.columns(2)
for i, house in enumerate(houses):
    with cols[i % 2]:
        # ถ้ายังไม่มีข้อมูลในภพนั้น ให้ใส่รายการว่างๆ ไปก่อน (รองรับภพที่ยังไม่ได้ดึงข้อมูลมา)
        selected = st.multiselect(
            f"{house}", 
            options=list(planets_map.keys()), 
            key=f"grid_sel_{house}",
            placeholder="เพิ่มดาว..."
        )
        # แปลงดาวที่เลือกเป็นเลขไทย
        selections[house] = [planets_map[p] for p in selected]

# 4. ฟังก์ชันสำหรับสร้าง HTML ตาราง 12 ช่อง (ล็อคสัดส่วน 100% ไม่บิดเบี้ยว)
def generate_zodiac_grid(selections):
    # ตำแหน่งของภพบนตาราง 4x4 (Row, Column)
    layout = {
        (1, 1): "วินาศ", (1, 2): "ลัคนา", (1, 3): "กดุมภะ", (1, 4): "สหัชชะ",
        (2, 1): "ลาภะ",                                     (2, 4): "พันธุ",
        (3, 1): "กัมมะ",                                    (3, 4): "ปุตตะ",
        (4, 1): "ศุภะ",   (4, 2): "มรณะ",   (4, 3): "ปัตนิ",   (4, 4): "อริ"
    }

    # CSS Grid โครงสร้างหลัก
    html = '''
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(4, 1fr); 
                width: 100%; max-width: 450px; margin: 0 auto; border: 3px solid #1e293b; 
                background-color: #f8fafc; aspect-ratio: 1; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">
    '''

    for r in range(1, 5):
        for c in range(1, 5):
            if (r, c) in layout:
                house = layout[(r, c)]
                # นำตัวเลขดาวมาเรียงต่อกัน
                planets_str = " ".join(selections.get(house, []))
                
                # ถ้าเป็นช่องลัคนา ให้ใส่สัญลักษณ์ 'ล' สีแดงไว้เสมอ
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
                # สร้างช่องว่างตรงกลางขนาด 2x2
                html += f'''
                <div style="grid-row: 2 / 4; grid-column: 2 / 4; border: 1px solid #cbd5e1; display: flex; align-items: center; justify-content: center; background-color: #ffffff;">
                    <span style="color: #94a3b8; font-size: 1.5rem; font-weight: bold; letter-spacing: 2px;">ราศีจักร</span>
                </div>
                '''
    html += '</div>'
    return html

# 5. วาดตารางราศีจักรลงใน Placeholder ที่เตรียมไว้ด้านบนสุด
grid_placeholder.markdown(generate_zodiac_grid(selections), unsafe_allow_html=True)
