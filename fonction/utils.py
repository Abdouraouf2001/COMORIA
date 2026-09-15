
import streamlit as st

import streamlit as st


def afficher_footer():
    st.divider()

    with st.container(horizontal_alignment="center"):
        st.markdown("### ComorIA")
        
    st.caption(
        "ComorIA — L'IA au service de l'éducation aux Comores"
    )

    st.caption(
        "Une initiative portée par Abdouraouf Ahamada Saroumaya (Guilbert)"
    )

    st.caption(
        "© 2026 ComorIA • Tous droits réservés"
    )





# def afficher_footer():
#     st.divider()

#     col1, col2, col3 = st.columns([1, 2, 1])

#     with col2:
#         st.markdown(
#             """
#             <div style="text-align: center;">
#                 <div style="font-size: 18px; font-weight: bold;">
#                     🇰🇲 ComorIA
#                 </div>

#                 <div style="font-size: 14px; margin-top: 6px;">
#                     L'IA au service de l'éducation aux Comores
#                 </div>

#                 <div style="font-size: 13px; margin-top: 6px;">
#                     Une initiative portée par
#                     <strong>Abdouraouf Ahamada Saroumaya (Guilbert)</strong>
#                 </div>

#                 <div style="font-size: 12px; margin-top: 8px;">
#                     © 2026 ComorIA • Tous droits réservés
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )




    
# # def afficher_footer():
# #     st.markdown(
# #         """
# #         <div style="text-align:center; margin-top:40px; padding:20px; border-top:1px solid #dddddd;">
# #             <div style="font-size:18px; font-weight:bold; color:#00843D;">
# #                 🇰🇲 ComorIA
# #             </div>

# #             <div style="font-size:14px; color:#6B7280; margin-top:5px;">
# #                 L'IA au service de l'éducation aux Comores
# #             </div>

# #             <div style="font-size:13px; color:#6B7280; margin-top:5px;">
# #                 Une initiative portée par
# #                 <strong>Abdouraouf Ahamada Saroumaya (Guilbert)</strong>
# #             </div>

# #             <div style="font-size:12px; color:#9CA3AF; margin-top:8px;">
# #                 © 2026 ComorIA • Tous droits réservés
# #             </div>
# #         </div>
# #         """,
# #         unsafe_allow_html=True
# #     )
