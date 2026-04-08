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
from data_zodiac_planets import zodiac_planets_data
from data_special_rules import special_rules
from data_neech import neech_data

st.set_page_config(page_title="Chakkathipani", page_icon="⭐", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"], div, span, h1, h2, h3, h4, h5, h6, p, a, label, button, input, select {
    font-family: 'Sarabun', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

planets_map = {
    "พระอาทิตย์ (1)": "๑", "พระจันทร์ (2)": "๒", "พระอังคาร (3)": "๓", "พระพุธ (4)": "๔",
    "พระพฤหัสบดี (5)": "๕", "พระศุกร์ (6)": "๖", "พระเสาร์ (7)": "๗", "พระราหู (8)": "๘",
}

houses = ["ลัคนา", "กดุมภะ", "สหัชชะ", "พันธุ", "ปุตตะ", "อริ", 
          "ปัตนิ", "มรณะ", "ศุภะ", "กัมมะ", "ลาภะ", "วินาศ"]

zodiac_signs = ["ไม่ระบุ", "เมษ", "พฤษภ", "เมถุน", "กรกฎ", "สิงห์", "กันย์", 
                "ตุลย์", "พิจิก (กีฏะราศี)", "ธนู", "มังกร", "กุมภ์", "มีน"]

def clear_selections():
    for house in houses:
        st.session_state[f"sel_{house}"] = []
    if "sel_zodiac" in st.session_state:
        st.session_state["sel_zodiac"] = "ไม่ระบุ"

house_labels = {
    "ลัคนา": "สถิตร่วมกับลัคนา", "กดุมภะ": "สองจากลัคนา (กดุมภะ)", "สหัชชะ": "สามจากลัคนา (สหัชชะ)",
    "พันธุ": "สี่จากลัคนา (พันธุ)", "ปุตตะ": "ห้าจากลัคนา (ปุตตะ)", "อริ": "หกจากลัคนา (อริ)",
    "ปัตนิ": "เจ็ดจากลัคนา (ปัตนิ)", "มรณะ": "แปดจากลัคนา (มรณะ)", "ศุภะ": "เก้าจากลัคนา (ศุภะ)",
    "กัมมะ": "สิบจากลัคนา (กัมมะ)", "ลาภะ": "สิบเอ็ดจากลัคนา (ลาภะ)", "วินาศ": "สิบสองจากลัคนา (วินาศ)"
}

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

st.markdown("<h1 style='text-align: center;'>⭐ คำทำนายดวงดาวกำเนิด</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 30px;'>ระบุดาวลงในภพต่างๆ เพื่อสร้างผังราศีจักรและอ่านคำทำนายจากคัมภีร์จักรทีปนี</p>", unsafe_allow_html=True)
st.divider()

col_left, col_mid, col_right = st.columns([1.2, 1, 1.5], gap="large")

for house in houses:
    if f"sel_{house}" not in st.session_state:
        st.session_state[f"sel_{house}"] = []

all_selected_planets = []
for house in houses:
    all_selected_planets.extend(st.session_state[f"sel_{house}"])

selections_names = {}
selections_thai_nums = {}

house_zodiac_map = {}
zodiac_house_map = {}
ascendant_sign = st.session_state.get("sel_zodiac", "ไม่ระบุ")

# --- คอลัมน์กลาง: ตัวเลือกดาว ---
with col_mid:
    st.markdown("<h3 style='text-align: center; color: #334155; margin-bottom: 20px;'>📝 ระบุดาวสถิต</h3>", unsafe_allow_html=True)
    
    ascendant_sign = st.selectbox("ลัคนาสถิตราศี", options=zodiac_signs, key="sel_zodiac")
    
    if ascendant_sign != "ไม่ระบุ":
        asc_idx = zodiac_signs.index(ascendant_sign) - 1 
        for i, h in enumerate(houses):
            z_idx = (asc_idx + i) % 12
            sign_name = zodiac_signs[z_idx + 1]
            mapped_sign = "พิจิก" if "พิจิก" in sign_name else sign_name
            house_zodiac_map[h] = mapped_sign
            zodiac_house_map[mapped_sign] = h

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
    
    for house in houses:
        current_selection = st.session_state[f"sel_{house}"]
        other_houses_selection = [p for p in all_selected_planets if p not in current_selection]
        available_options = [p for p in list(planets_map.keys()) if p not in other_houses_selection]

        selected = st.multiselect(
            f"{house_labels[house]}", 
            options=available_options, 
            key=f"sel_{house}",
            placeholder="เลือกดาว..."
        )
        if selected:
            selections_names[house] = selected
            selections_thai_nums[house] = [planets_map[p] for p in selected]

def generate_zodiac_grid(selections):
    layout = {
        (1, 2): "ลัคนา", (1, 1): "กดุมภะ", (2, 1): "สหัชชะ", (3, 1): "พันธุ",
        (4, 1): "ปุตตะ", (4, 2): "อริ", (4, 3): "ปัตนิ", (4, 4): "มรณะ",
        (3, 4): "ศุภะ", (2, 4): "กัมมะ", (1, 4): "ลาภะ", (1, 3): "วินาศ"
    }
    html_parts = []
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
                html_parts.append(f'<div style="grid-row: 2 / 4; grid-column: 2 / 4; border: 1px solid #cbd5e1; display: flex; align-items: center; justify-content: center; background-color: #ffffff;"><span style="color: #94a3b8; font-size: 1.8rem; font-weight: bold; letter-spacing: 2px;">ดวงราศีจักร</span></div>')
    html_parts.append('</div>')
    return "".join(html_parts)

# --- คอลัมน์ซ้าย: แสดงตารางราศีจักร ---
with col_left:
    st.markdown("<h3 style='text-align: center; color: #334155; margin-bottom: 20px;'>🔮 ดวงราศีจักร</h3>", unsafe_allow_html=True)
    st.markdown(generate_zodiac_grid(selections_thai_nums), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🔄 ล้างข้อมูลทั้งหมด", on_click=clear_selections, use_container_width=True)

# --- คอลัมน์ขวา: แสดงผลคำทำนาย ---
with col_right:
    st.markdown("<h3 style='text-align: center; color: #334155; margin-bottom: 20px;'>✨ ความหมายดาว</h3>", unsafe_allow_html=True)
    
    # 1. เช็คเกณฑ์พิเศษ (Special Rules)
    if selections_names:
        matched_rules = []
        for rule in special_rules:
            is_match = True
            cond_type = rule.get("condition_type", "house")
            
            if cond_type == "house":
                for req_house, req_planets in rule["conditions"].items():
                    user_planets_in_house = selections_names.get(req_house, [])
                    for p in req_planets:
                        if p not in user_planets_in_house:
                            is_match = False
                            break
                    if not is_match: break

            elif cond_type == "zodiac":
                if ascendant_sign == "ไม่ระบุ":
                    is_match = False
                else:
                    for req_zodiac, req_planets in rule["conditions"].items():
                        target_house = zodiac_house_map.get(req_zodiac)
                        if not target_house:
                            is_match = False
                            break
                        user_planets_in_house = selections_names.get(target_house, [])
                        for p in req_planets:
                            if p not in user_planets_in_house:
                                is_match = False
                                break
                        if not is_match: break
            
            # --- ตรรกะใหม่สำหรับ "คู่อสีติร่วมธาตุ" ที่เช็คทั้งลัคนาและราศี ---
            elif cond_type == "ascendant_and_house":
                mapped_ascendant = "พิจิก" if "พิจิก" in ascendant_sign else ascendant_sign
                if mapped_ascendant != rule.get("req_ascendant"):
                    is_match = False
                else:
                    for req_house, req_planets in rule["conditions"].items():
                        user_planets_in_house = selections_names.get(req_house, [])
                        for p in req_planets:
                            if p not in user_planets_in_house:
                                is_match = False
                                break
                        if not is_match: break

            if is_match:
                matched_rules.append(rule)
                
        if matched_rules:
            for match in matched_rules:
                if match.get("type") == "good":
                    bg_color, border_color, accent_color, text_color = "#f0fdf4", "#bbf7d0", "#16a34a", "#14532d"
                    icon, title_text = "🌟", "เกณฑ์ให้คุณ (สิริมงคล/โยคเกณฑ์)"
                else:
                    bg_color, border_color, accent_color, text_color = "#fef2f2", "#f87171", "#dc2626", "#7f1d1d"
                    icon, title_text = "🚨", "คำทำนายเกณฑ์พิเศษ (พินทุบาทว์ / ดาวผสม)"

                special_html = (
                    f'<div style="font-family: \'Sarabun\', sans-serif; background-color: {bg_color}; border: 2px solid {border_color}; border-left: 8px solid {accent_color}; padding: 20px; border-radius: 10px; margin-bottom: 24px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);">'
                    f'<h4 style="color: {accent_color}; margin-top: 0; margin-bottom: 12px; font-size: 18px;">{icon} {title_text}</h4>'
                    f'<span style="background-color: white; color: {accent_color}; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 14px; margin-bottom: 10px; display: inline-block; border: 1px solid {border_color};">{match["name"]}</span>'
                    f'<p style="font-size: 18px; color: {text_color}; margin: 0; line-height: 1.6; margin-top: 8px;"><strong>คำทำนาย:</strong> {match["text"]}</p>'
                    f'</div>'
                )
                st.markdown(special_html, unsafe_allow_html=True)
    
    # 2. แสดงผลคำทำนายรายภพ, ราศี และ นิจ
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
                        bg_color = result_data["bg"]
                        border_color = result_data["border"]
                        accent_color = result_data["color"]
                        prediction_text = result_data["text"]
                        
                        if planet == "พระอังคาร (3)":
                            bg_color, border_color, accent_color = "#fdf2f8", "#fbcfe8", "#ec4899"
                            
                        if house == "วินาศ" and ascendant_sign == "พิจิก (กีฏะราศี)":
                            prediction_text = "กลับให้คุณ หาอันตรายมิได้"
                            bg_color, border_color, accent_color = "#ecfdf5", "#a7f3d0", "#059669"
                            
                        zodiac_section = ""
                        neech_badge = ""
                        neech_section = ""
                        
                        if house in house_zodiac_map:
                            current_zodiac = house_zodiac_map[house]
                            
                            zodiac_pred_info = zodiac_planets_data.get(current_zodiac, {}).get(planet)
                            if zodiac_pred_info:
                                zodiac_text = zodiac_pred_info["text"]
                                zodiac_section = (
                                    f'<div style="border-top: 1px dashed rgba(0,0,0,0.1); margin: 12px 0; padding-top: 12px;"></div>'
                                    f'<span style="font-size: 13px; font-weight: 600; color: {accent_color}; margin-bottom: 4px; display: block; opacity: 0.8;">ความหมายดาวสถิตราศี{current_zodiac}</span>'
                                    f'<p style="font-size: 18px; color: #1e293b; margin: 0; line-height: 1.6;">{zodiac_text}</p>'
                                )

                            if planet in neech_data and current_zodiac == neech_data[planet]["sign"]:
                                neech_text = neech_data[planet]["text"]
                                neech_badge = f'<span style="background-color: #f1f5f9; color: #64748b; padding: 2px 8px; border-radius: 9999px; font-size: 12px; border: 1px solid #cbd5e1; display: inline-flex; align-items: center; gap: 4px;"><span>⬇️</span> นิจ</span>'
                                neech_section = (
                                    f'<div style="background-color: rgba(255,255,255,0.6); border: 1px solid rgba(0,0,0,0.05); border-radius: 8px; padding: 12px; margin-top: 16px;">'
                                    f'<span style="font-size: 13px; font-weight: 600; color: #64748b; margin-bottom: 4px; display: block;">⬇️ คำทำนายเกณฑ์มาตรฐาน: นิจ (เสื่อมกำลัง)</span>'
                                    f'<p style="font-size: 16px; color: #475569; margin: 0; line-height: 1.5;">{neech_text}</p>'
                                    f'</div>'
                                )
                        
                        html_card = (
                            f'<div style="font-family: \'Sarabun\', sans-serif; background-color: {bg_color}; border: 1px solid {border_color}; border-left: 6px solid {accent_color}; padding: 24px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">'
                            f'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 12px;">'
                            f'<span style="font-size: 15px; font-weight: 600; color: #64748b; letter-spacing: 0.5px;">{position_title}</span>'
                            f'<div style="display: flex; align-items: center; gap: 8px;">'
                            f'{neech_badge}'
                            f'<span style="background-color: white; color: {accent_color}; padding: 4px 14px; border-radius: 9999px; font-weight: bold; font-size: 14px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">{planet}</span>'
                            f'</div>'
                            f'</div>'
                            f'<span style="font-size: 13px; font-weight: 600; color: {accent_color}; margin-bottom: 4px; display: block; opacity: 0.8;">ความหมายตามภพ ({house})</span>'
                            f'<p style="font-size: 18px; color: #1e293b; margin: 0; line-height: 1.6;">{prediction_text}</p>'
                            f'{zodiac_section}'
                            f'{neech_section}'
                            f'</div>'
                        )
                        st.markdown(html_card, unsafe_allow_html=True)
                    
        if not has_prediction:
            st.info("ท่านได้กรอกดาวลงในตารางราศีจักรแล้ว (คำทำนายในภพที่เลือกจะถูกอัปเดตเข้าระบบในภายหลัง)")
    else:
        st.info("โปรดเลือกดาวที่สถิตในตำแหน่งต่างๆ เพื่อดูผลคำทำนาย")
