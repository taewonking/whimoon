import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# ── 밤하늘의 별 배경 스타일 ────────────────────────────────
st.markdown("""
<style>
    @keyframes twinkle {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 1; }
    }
    
    /* 밤하늘 배경 */
    .stApp {
        background: linear-gradient(180deg, #0a0e27 0%, #1a1f3a 50%, #2d1b4e 100%);
        position: relative;
        overflow: hidden;
    }
    
    /* 별 생성 */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20% 30%, #eee, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 60% 70%, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 50% 50%, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 80% 10%, #fff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 90% 60%, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 30% 80%, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 10% 40%, #fff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 40% 90%, #eee, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 70% 40%, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 85% 85%, #fff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 15% 60%, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 55% 25%, #eee, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 75% 75%, #fff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 25% 15%, #fff, rgba(0,0,0,0));
        background-repeat: repeat;
        background-size: 100% 100%;
        background-position: 0 0;
        pointer-events: none;
        animation: twinkle 3s ease-in-out infinite;
    }
    
    /* 메인 컨텐츠 배경 - 더 밝고 명확하게 */
    .main {
        background: rgba(20, 15, 50, 0.9) !important;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7), 0 0 40px rgba(147, 112, 219, 0.5);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(147, 112, 219, 0.6);
    }
    
    /* 제목 스타일 */
    h1 {
        background: linear-gradient(135deg, #a78bfa, #c4b5fd, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3em !important;
        font-weight: 900 !important;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 0 0 30px rgba(167, 139, 250, 0.8);
    }
    
    /* 부제목 스타일 */
    h2, h3 {
        color: #c4b5fd !important;
        font-weight: 700 !important;
        text-shadow: 0 0 15px rgba(196, 181, 253, 0.5) !important;
    }
    
    /* 버튼 스타일 */
    .stButton > button {
        background: linear-gradient(135deg, #a78bfa, #c4b5fd) !important;
        color: #0f0f23 !important;
        border: 2px solid rgba(196, 181, 253, 0.8) !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        font-weight: 700 !important;
        box-shadow: 0 8px 20px rgba(167, 139, 250, 0.6), 0 0 30px rgba(167, 139, 250, 0.5) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 30px rgba(167, 139, 250, 0.8), 0 0 40px rgba(167, 139, 250, 0.7) !important;
    }
    
    /* 입력창 스타일 */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextInput > div > div > input {
        border: 2px solid #a78bfa !important;
        border-radius: 10px !important;
        padding: 12px !important;
        background: rgba(30, 27, 80, 0.8) !important;
        color: #f3e8ff !important;
        font-weight: 500 !important;
    }
    
    .stNumberInput > div > div > input::placeholder,
    .stTextInput > div > div > input::placeholder {
        color: #c4b5fd !important;
    }
    
    /* 라벨 텍스트 */
    label {
        color: #e9d5ff !important;
        font-weight: 600 !important;
    }
    
    /* 성공 메시지 */
    .stSuccess {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(96, 165, 250, 0.15)) !important;
        border-left: 5px solid #22c55e !important;
        border-radius: 10px !important;
        border: 2px solid rgba(34, 197, 94, 0.5) !important;
        color: #86efac !important;
    }
    
    /* 에러 메시지 */
    .stError {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(249, 115, 22, 0.15)) !important;
        border-left: 5px solid #ef4444 !important;
        border-radius: 10px !important;
        border: 2px solid rgba(239, 68, 68, 0.5) !important;
        color: #fca5a5 !important;
    }
    
    /* 구분선 */
    .stDivider {
        border-color: #a78bfa !important;
        opacity: 0.7 !important;
    }
    
    /* 메트릭 박스 */
    .stMetric {
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.15), rgba(196, 181, 253, 0.15)) !important;
        border-radius: 10px !important;
        padding: 20px !important;
        border-left: 5px solid #a78bfa !important;
        border: 2px solid rgba(167, 139, 250, 0.4) !important;
        box-shadow: 0 0 20px rgba(167, 139, 250, 0.3) !important;
    }
    
    /* 메트릭 텍스트 */
    .stMetric label {
        color: #c4b5fd !important;
    }
    
    .stMetric > div {
        color: #f3e8ff !important;
    }
    
    /* 확장 박스 */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.15), rgba(196, 181, 253, 0.15)) !important;
        border-radius: 10px !important;
        color: #c4b5fd !important;
        border: 2px solid rgba(167, 139, 250, 0.3) !important;
        font-weight: 600 !important;
    }
    
    /* 테이블 스타일 */
    table {
        color: #e9d5ff !important;
    }
    
    thead {
        background: rgba(167, 139, 250, 0.2) !important;
    }
    
    tbody tr {
        border-bottom: 1px solid rgba(167, 139, 250, 0.2) !important;
    }
    
    /* 일반 텍스트 */
    p, span {
        color: #e9d5ff !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧮 Calculator")
st.markdown("사칙연산 · 모듈러 · 지수 · 로그 연산을 지원합니다.")

# ── 연산 선택 ──────────────────────────────────────────────
operation = st.selectbox(
    "연산 선택",
    [
        "➕ 덧셈 (a + b)",
        "➖ 뺄셈 (a - b)",
        "✖️ 곱셈 (a × b)",
        "➗ 나눗셈 (a ÷ b)",
        "🔢 모듈러 (a mod b)",
        "📈 지수 (a ^ b)",
        "📉 로그 (log_b(a))",
    ],
)

st.divider()

# ── 입력 ──────────────────────────────────────────────────
is_log = "로그" in operation

if is_log:
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("진수 (a)", value=100.0, format="%.6f")
    with col2:
        b = st.number_input("밑 (b)", value=10.0, format="%.6f")
else:
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("a", value=0.0, format="%.6f")
    with col2:
        b = st.number_input("b", value=1.0, format="%.6f")

# ── 계산 ──────────────────────────────────────────────────
if st.button("계산", use_container_width=True, type="primary"):
    result = None
    error = None

    try:
        if "덧셈" in operation:
            result = a + b
            expr = f"{a} + {b}"
        elif "뺄셈" in operation:
            result = a - b
            expr = f"{a} - {b}"
        elif "곱셈" in operation:
            result = a * b
            expr = f"{a} × {b}"
        elif "나눗셈" in operation:
            if b == 0:
                error = "0으로 나눌 수 없습니다."
            else:
                result = a / b
                expr = f"{a} ÷ {b}"
        elif "모듈러" in operation:
            if b == 0:
                error = "모듈러의 제수는 0이 될 수 없습니다."
            else:
                result = math.fmod(a, b)
                expr = f"{a} mod {b}"
        elif "지수" in operation:
            result = a ** b
            expr = f"{a} ^ {b}"
        elif "로그" in operation:
            if a <= 0:
                error = "진수(a)는 양수여야 합니다."
            elif b <= 0 or b == 1:
                error = "밑(b)은 양수이고 1이 아니어야 합니다."
            else:
                result = math.log(a, b)
                expr = f"log_{b}({a})"
    except OverflowError:
        error = "결과값이 너무 커서 표현할 수 없습니다."
    except Exception as e:
        error = f"오류: {e}"

    st.divider()
    if error:
        st.error(f"❌ {error}")
    else:
        st.success(f"**{expr} = {result:g}**")
        st.metric(label="결과", value=f"{result:g}")

# ── 도움말 ────────────────────────────────────────────────
with st.expander("연산 설명"):
    st.markdown(
        """
| 연산 | 설명 | 예시 |
|------|------|------|
| 덧셈 | a + b | 3 + 4 = 7 |
| 뺄셈 | a - b | 10 - 3 = 7 |
| 곱셈 | a × b | 3 × 4 = 12 |
| 나눗셈 | a ÷ b | 10 ÷ 4 = 2.5 |
| 모듈러 | a를 b로 나눈 나머지 | 10 mod 3 = 1 |
| 지수 | a의 b제곱 | 2 ^ 8 = 256 |
| 로그 | 밑이 b인 a의 로그 | log₁₀(100) = 2 |
"""
    )

st.divider()

# ── 그래프 ────────────────────────────────────────────────
st.subheader("📊 함수 그래프")

PRESETS = {
    "직접 입력": "",
    "y = x²": "x**2",
    "y = x³": "x**3",
    "y = √x": "np.sqrt(x)",
    "y = |x|": "np.abs(x)",
    "y = sin(x)": "np.sin(x)",
    "y = cos(x)": "np.cos(x)",
    "y = tan(x)": "np.tan(x)",
    "y = eˣ": "np.exp(x)",
    "y = ln(x)": "np.log(x)",
    "y = log₁₀(x)": "np.log10(x)",
    "y = 1/x": "1/x",
}

preset = st.selectbox("프리셋 함수", list(PRESETS.keys()))

if preset == "직접 입력":
    func_input = st.text_input(
        "함수 입력 (x를 변수로 사용)",
        value="x**2",
        placeholder="예: x**2 + 2*x + 1, np.sin(x), np.exp(-x)"
    )
else:
    func_input = st.text_input(
        "함수 입력 (x를 변수로 사용)",
        value=PRESETS[preset],
    )

col1, col2 = st.columns(2)
with col1:
    x_min = st.number_input("x 최솟값", value=-10.0)
with col2:
    x_max = st.number_input("x 최댓값", value=10.0)

if st.button("그래프 그리기", use_container_width=True):
    if x_min >= x_max:
        st.error("❌ x 최솟값은 최댓값보다 작아야 합니다.")
    elif not func_input.strip():
        st.error("❌ 함수를 입력해주세요.")
    else:
        try:
            x = np.linspace(x_min, x_max, 1000)
            # 허용된 함수만 사용
            allowed = {
                "np": np, "x": x,
                "sin": np.sin, "cos": np.cos, "tan": np.tan,
                "exp": np.exp, "log": np.log, "log10": np.log10,
                "log2": np.log2, "sqrt": np.sqrt, "abs": np.abs,
                "pi": np.pi, "e": np.e,
            }
            y = eval(func_input, {"__builtins__": {}}, allowed)
            y = np.where(np.isfinite(y), y, np.nan)

            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(x, y, color="#ea580c", linewidth=2)
            ax.axhline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.5)
            ax.axvline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.5)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title(f"y = {func_input}")
            ax.grid(True, alpha=0.3)
            ax.set_xlim(x_min, x_max)

            # y축 범위 자동 조정 (이상값 제외)
            y_finite = y[np.isfinite(y)]
            if len(y_finite) > 0:
                y_range = np.percentile(y_finite, [2, 98])
                margin = (y_range[1] - y_range[0]) * 0.1 or 1
                ax.set_ylim(y_range[0] - margin, y_range[1] + margin)

            st.pyplot(fig)
            plt.close(fig)

        except Exception as e:
            st.error(f"❌ 함수 오류: {e}\n\n힌트: numpy 함수는 np.sin(x) 형태로 입력하세요.")

st.caption("사용 가능: x, np.sin, np.cos, np.tan, np.exp, np.log, np.log10, np.sqrt, np.abs, np.pi, np.e")
