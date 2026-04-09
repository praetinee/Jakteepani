# ... existing code ...
from data_zodiac_planets import zodiac_planets_data
from data_special_rules import special_rules
from data_neech import neech_data
from data_ongkeen import ongkeen_rules

st.set_page_config(page_title="Chakkathipani", page_icon="⭐", layout="wide")
# ... existing code ...
house_zodiac_map = {}
zodiac_house_map = {}
ascendant_sign = st.session_state.get("sel_zodiac", "ไม่ระบุ")

# คำนวณหาภพที่เป็นองค์เกณฑ์
ongkeen_target_house = None
if ascendant_sign != "ไม่ระบุ":
    clean_asc = "พิจิก" if "พิจิก" in ascendant_sign else ascendant_sign
    for group, data in ongkeen_rules["ascendant_groups"].items():
        if clean_asc in data["signs"]:
            ongkeen_target_house = data["target_house"]
            break

# --- คอลัมน์กลาง: ตัวเลือกดาว ---
with col_mid:
# ... existing code ...
                        if house == "วินาศ" and ascendant_sign == "พิจิก (กีฏะราศี)":
                            prediction_text = "กลับให้คุณ หาอันตรายมิได้"
                            bg_color, border_color, accent_color = "#ecfdf5", "#a7f3d0", "#059669"
                            
                        zodiac_section = ""
                        neech_badge = ""
                        neech_section = ""
                        ongkeen_badge = ""
                        ongkeen_section = ""
                        
                        if house in house_zodiac_map:
                            current_zodiac = house_zodiac_map[house]
# ... existing code ...
                                neech_section = (
                                    f'<div style="background-color: rgba(255,255,255,0.6); border: 1px solid rgba(0,0,0,0.05); border-radius: 8px; padding: 12px; margin-top: 16px;">'
                                    f'<span style="font-size: 13px; font-weight: 600; color: #64748b; margin-bottom: 4px; display: block;">⬇️ คำทำนายเกณฑ์มาตรฐาน: นิจ (เสื่อมกำลัง)</span>'
                                    f'<p style="font-size: 16px; color: #475569; margin: 0; line-height: 1.5;">{neech_text}</p>'
                                    f'</div>'
                                )

                        # 2.3 ตรวจสอบอุดมเกณฑ์ (องค์เกณฑ์)
                        if house == ongkeen_target_house and planet in ongkeen_rules["predictions"]:
                            ongkeen_text = ongkeen_rules["predictions"][planet]
                            ongkeen_badge = f'<span style="background-color: #fef9c3; color: #854d0e; padding: 2px 8px; border-radius: 9999px; font-size: 12px; border: 1px solid #fde047; display: inline-flex; align-items: center; gap: 4px;"><span>👑</span> องค์เกณฑ์</span>'
                            ongkeen_section = (
                                f'<div style="background-color: rgba(254,249,195,0.4); border: 1px solid rgba(253,224,71,0.5); border-radius: 8px; padding: 12px; margin-top: 16px;">'
                                f'<span style="font-size: 13px; font-weight: 600; color: #a16207; margin-bottom: 4px; display: block;">👑 คำทำนายอุดมเกณฑ์ (องค์เกณฑ์)</span>'
                                f'<p style="font-size: 16px; color: #713f12; margin: 0; line-height: 1.5;">{ongkeen_text}</p>'
                                f'</div>'
                            )
                        
                        html_card = (
                            f'<div style="font-family: \'Sarabun\', sans-serif; background-color: {bg_color}; border: 1px solid {border_color}; border-left: 6px solid {accent_color}; padding: 24px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">'
                            f'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 12px;">'
                            f'<span style="font-size: 15px; font-weight: 600; color: #64748b; letter-spacing: 0.5px;">{position_title}</span>'
                            f'<div style="display: flex; align-items: center; gap: 8px;">'
                            f'{ongkeen_badge}'
                            f'{neech_badge}'
                            f'<span style="background-color: white; color: {accent_color}; padding: 4px 14px; border-radius: 9999px; font-weight: bold; font-size: 14px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">{planet}</span>'
                            f'</div>'
                            f'</div>'
                            f'<span style="font-size: 13px; font-weight: 600; color: {accent_color}; margin-bottom: 4px; display: block; opacity: 0.8;">ความหมายตามภพ ({house})</span>'
                            f'<p style="font-size: 18px; color: #1e293b; margin: 0; line-height: 1.6;">{prediction_text}</p>'
                            f'{zodiac_section}'
                            f'{ongkeen_section}'
                            f'{neech_section}'
                            f'</div>'
                        )
                        st.markdown(html_card, unsafe_allow_html=True)
# ... existing code ...
