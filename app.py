import streamlit as st

# ตั้งค่าหน้าเพจ Streamlit
st.set_page_config(
    page_title="คำทำนายดวงดาวกำเนิด",
    page_icon="⭐",
    layout="centered"
)

# โครงสร้างฐานข้อมูล
# แยกดาวแต่ละดวงออกจากกัน และใส่ตัวเลขกำกับตามหลักโหราศาสตร์
astrology_database = {
    "สถิตย์อยู่กับลัคนา (กุมลัคน์)": {
        "พระอาทิตย์ (1)": {
            "text": "ผู้นั้นจะจากบิดามารดาแต่น้อย จะแกล้วกล้าจักเป็นนักเลงสุรา มีพรรคพวกเผ่าพันธุ์มาก จะได้สมบัติบริวารและยศศักดิ์",
            "color": "#dc2626", "bg": "#fef2f2", "border": "#fecaca"
        },
        "พระจันทร์ (2)": {
            "text": "ผู้นั้นจะมีรูปงาม จะบริบูรณ์ด้วยสมบัติและทาสกรรมกรชายหญิง จะมีภริยาและบุตรมาก แต่มักจะเป็นโรคในท้อง",
            "color": "#f59e0b", "bg": "#fffbeb", "border": "#fde68a"
        },
        "พระอังคาร (3)": {
            "text": "ผู้นั้นจะได้เป็นเสนาบดีมีกำลังมาก จะแกล้วกล้าในสงคราม แต่จะมีรูปชั่ว มักจะตกจากยศ ไม่ยั่งยืน",
            "color": "#e11d48", "bg": "#fff1f2", "border": "#fecdd3"
        },
        "พระพุธ (4)": {
            "text": "ผู้นั้นจะมีโภคสมบัติมาก จะมีศีลและปัญญาเป็นที่รักที่สรรเสริญแก่นักปราชญ์ ฉลาดกล่าวคำไพเราะ แต่จะเป็นโรคในท้องมาก",
            "color": "#059669", "bg": "#ecfdf5", "border": "#a7f3d0"
        },
        "พระพฤหัสบดี (5)": {
            "text": "ผู้นั้นจะมีวิชามาก จะเฉลียวฉลาด ปราศจากเกียจคร้าน จะมีอุตสาหะและตบะเดชะ จะมีทรัพย์และลาภเป็นนิจบมิได้ขาด",
            "color": "#f97316", "bg": "#fff7ed", "border": "#fed7aa"
        },
        "พระศุกร์ (6)": {
            "text": "ผู้นั้นจะมีจิตตั้งอยู่ในสัตย์ธรรมยิ่งนัก จะได้มีภริยามีสกุลอันสูง",
            "color": "#0ea5e9", "bg": "#f0f9ff", "border": "#bae6fd"
        },
        "พระเสาร์ (7)": {
            "text": "ผู้นั้นจะมีปัญญามาก จะเป็นนักปราชญ์ จะมีชัยชนะแก่ศัตรู จะมีทรัพย์มิรู้ขาด",
            "color": "#7c3aed", "bg": "#f5f3ff", "border": "#ddd6fe"
        },
        "พระราหู (8)": {
            "text": "ผู้นั้นจะมีโรคเนื่อง ๆ แต่จะมีปัญญาอันแกล้วกล้า",
            "color": "#475569", "bg": "#f8fafc", "border": "#e2e8f0"
        }
    },
    "เป็นสองกับลัคนา (ภพกดุมภะ)": {
        "พระอาทิตย์ (1)": {
            "text": "ผู้นั้นจะมีทุกข์โศกโรคภัยมาก",
            "color": "#dc2626", "bg": "#fef2f2", "border": "#fecaca"
        },
        "พระจันทร์ (2)": {
            "text": "ผู้นั้นจะมีผู้อื่นเบียดเบียนให้ได้เดือดร้อนเนือง ๆ",
            "color": "#f59e0b", "bg": "#fffbeb", "border": "#fde68a"
        },
        "พระอังคาร (3)": {
            "text": "ผู้นั้นจะมีอายุบมิได้ยืน",
            "color": "#e11d48", "bg": "#fff1f2", "border": "#fecdd3"
        },
        "พระพุธ (4)": {
            "text": "ผู้นั้นจะมีคนบูชานับถือมาก",
            "color": "#0d9488", "bg": "#f0fdfa", "border": "#99f6e4"
        },
        "พระพฤหัสบดี (5)": {
            "text": "ผู้นั้นจะมีคนบูชานับถือมาก",
            "color": "#0d9488", "bg": "#f0fdfa", "border": "#99f6e4"
        },
        "พระศุกร์ (6)": {
            "text": "ผู้นั้นจะไม่รู้สิ้นทรัพย์",
            "color": "#4f46e5", "bg": "#eef2ff", "border": "#c7d2fe"
        },
        "พระเสาร์ (7)": {
            "text": "ผู้นั้นจะไม่รู้สิ้นทรัพย์",
            "color": "#4f46e5", "bg": "#eef2ff", "border": "#c7d2fe"
        },
        "พระราหู (8)": {
            "text": "ผู้นั้นจะมีจิตฟุ้งซ่านขุ่นมัว มักจะเป็นโจร จะเป็นพิกลจริต",
            "color": "#475569", "bg": "#f8fafc", "border": "#e2e8f0"
        }
    }
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
