import streamlit as st
from huggingface_hub import InferenceClient

st.title("AI文献整理助手")

# 这里填你的 Hugging Face token
HF_TOKEN = "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"

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN,
)

text = st.text_area("粘贴论文摘要")

if st.button("开始分析"):
    if text:
        prompt = f"""
请分析下面论文摘要：
1. 是否与 CNF（纳米纤维素纤丝）有关？
2. 是否与 CNC（纳米纤维素晶体）有关？
3. 是否与 DP（聚合度）有关？
4. 简短说明理由。

摘要：
{text}
"""

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
        )

        result = response.choices[0].message.content
        st.write("### 分析结果")
        st.write(result)
    else:
        st.warning("请先粘贴摘要")
