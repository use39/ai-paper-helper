import streamlit as st

st.title("AI文献整理助手")

text = st.text_area("粘贴论文摘要")

if st.button("开始整理"):
    if text:
        st.write("### 分析结果")
        st.write("✅ 与 CNF/CNC/DP 相关")
        st.write("（先做演示版，后面再接真正AI）")
    else:
        st.write("请先粘贴内容")
