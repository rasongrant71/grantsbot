import streamlit as st
from datetime import datetime

# -----------------------------
# APP CONFIG
# -----------------------------
st.set_page_config(
    page_title="GrantsBot – Prompt Engineering Trainer",
    page_icon="💼",
    layout="wide"
)

# -----------------------------
# STYLES
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f4ff;
    }
    .title-text {
        font-size: 32px;
        font-weight: 700;
        color: #3b1b6b;
    }
    .subtitle-text {
        font-size: 16px;
        color: #4b4b4b;
    }
    .role-badge {
        background-color: #e6ddff;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        color: #3b1b6b;
        display: inline-block;
        margin-bottom: 8px;
    }
    .chat-bubble-user {
        background-color: #3b1b6b;
        color: white;
        padding: 10px 14px;
        border-radius: 12px;
        margin-bottom: 6px;
        max-width: 80%;
    }
    .chat-bubble-bot {
        background-color: #ffffff;
        color: #222222;
        padding: 10px 14px;
        border-radius: 12px;
        margin-bottom: 6px;
        border: 1px solid #e0d7ff;
        max-width: 80%;
    }
    .chat-meta {
        font-size: 11px;
        color: #777777;
        margin-bottom: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# KNOWLEDGE MODULES
# -----------------------------
BASICS_POINTS = [
    "Use clear roles: e.g., “You are a workforce development specialist helping write a grant narrative.”",
    "Specify audience and purpose: who will read this and why it matters.",
    "Give structure: ask for bullet points, sections, or tables instead of vague answers.",
    "Provide context: include program goals, target population, and constraints.",
    "Ask for step-by-step reasoning when you need transparency."
]

INTERMEDIATE_POINTS = [
    "Use examples: show ‘before’ and ‘after’ prompts to guide the model.",
    "Iterate: refine prompts based on what you get back—treat it like a conversation, not a one-shot request.",
    "Constrain style: specify tone (formal, neutral, plain language), length, and formatting.",
    "Use variables: design reusable prompt templates for different grants or RFPs.",
    "Ask for multiple options: e.g., “Give me 3 variations of this outreach paragraph.”"
]

ADVANCED_POINTS = [
    "Chain prompts: break complex tasks into stages (outline → draft → refine → proofread).",
    "Use critique loops: ask the model to critique its own answer against criteria (equity, clarity, compliance).",
    "Role ensembles: ask it to respond as multiple perspectives (grant reviewer, program director, case manager).",
    "Guardrails: explicitly tell the model what NOT to do (no made-up data, no fake citations).",
    "Documentation: keep a prompt library for your team with tested, high-performing prompts."
]

# -----------------------------
# HELPER: GENERATE BOT RESPONSE
# -----------------------------
def generate_bot_response(message: str, level: str) -> str:
    message_lower = message.lower()

    # Simple intent routing based on level + keywords
    if "example" in message_lower or "prompt" in message_lower:
        if level == "Basics":
            return (
                "Here’s a basic workforce prompt example:\n\n"
                "**Prompt:**\n"
                "You are a workforce development specialist. Help me write a short, plain-language description "
                "of a job training program for adults who have been unemployed for 6+ months. "
                "Use a hopeful, respectful tone and keep it under 150 words."
            )
        elif level == "Intermediate":
            return (
                "Here’s an intermediate prompt template for grants:\n\n"
                "**Prompt:**\n"
                "You are a grant writer supporting a workforce development agency. Using the information below, "
                "draft a needs statement for a federal grant application. \n\n"
                "Context:\n"
                "- Target population: [insert]\n"
                "- Local labor market challenges: [insert]\n"
                "- Barriers faced by participants: [insert]\n\n"
                "Requirements:\n"
                "- 2–3 paragraphs\n"
                "- Formal, neutral tone\n"
                "- Emphasize equity and access\n"
                "- Avoid exaggeration or unsupported claims."
            )
        else:
            return (
                "Here’s an advanced, chained prompt approach:\n\n"
                "Step 1 – Outline:\n"
                "“You are a senior grant strategist. Create an outline for a workforce development grant narrative "
                "with sections for: Needs, Program Design, Partnerships, Outcomes, and Evaluation. Include 3–5 bullet "
                "points under each section.”\n\n"
                "Step 2 – Draft:\n"
                "“Using the outline above and the following local data, draft the Program Design section in 400–600 words: [insert data].”\n\n"
                "Step 3 – Critique:\n"
                "“Review the draft above as if you are a federal grant reviewer. Identify gaps, vague claims, or missing equity considerations.”"
            )

    if "tips" in message_lower or "how do i" in message_lower or "help" in message_lower:
        if level == "Basics":
            return "Basics tip: Start every prompt with role, audience, and purpose. Then say what format you want (bullets, sections, etc.)."
        elif level == "Intermediate":
            return "Intermediate tip: Reuse strong prompts as templates. Change only the program details or funder requirements."
        else:
            return "Advanced tip: Design prompt workflows—outline → draft → critique → refine—so your team can follow a repeatable process."

    # Default: reflective, teaching-oriented answer
    return (
        f"You’re working at the **{level}** level of prompt engineering.\n\n"
        "Try this:\n"
        "- Restate what you’re trying to accomplish (e.g., draft a grant section, design a workshop, summarize an RFP).\n"
        "- Add who the audience is (funder, board, participants, employers).\n"
        "- Specify tone, length, and format.\n\n"
        "If you tell me your exact scenario (for example, “I’m writing a grant for a youth apprenticeship program”), "
        "I can help you design a tailored prompt you can reuse with any AI tool."
    )

# -----------------------------
# SESSION STATE FOR CHAT
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_level" not in st.session_state:
    st.session_state.current_level = "Basics"

# -----------------------------
# LAYOUT
# -----------------------------
col_left, col_right = st.columns([2, 3])

with col_left:
    st.markdown('<div class="role-badge">Workforce Development · AI Prompt Training</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-text">GrantsBot</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle-text">'
        'A teaching chatbot for workforce development professionals learning prompt engineering '
        'for grants, program design, and communication.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.subheader("Learning Level")

    # Level buttons
    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        if st.button("Basics", type="primary"):
            st.session_state.current_level = "Basics"
    with col_b2:
        if st.button("Intermediate"):
            st.session_state.current_level = "Intermediate"
    with col_b3:
        if st.button("Advanced"):
            st.session_state.current_level = "Advanced"

    st.write(f"**Current level:** {st.session_state.current_level}")

    # Show key concepts for the selected level
    st.markdown("### Key Concepts")
    points = {
        "Basics": BASICS_POINTS,
        "Intermediate": INTERMEDIATE_POINTS,
        "Advanced": ADVANCED_POINTS
    }[st.session_state.current_level]

    for p in points:
        st.markdown(f"- {p}")

    st.markdown("---")
    st.markdown("### Quick Practice Buttons")

    if st.button("Show an example prompt for my level"):
        example_msg = "Give me an example prompt at my current level."
        st.session_state.messages.append(
            {"role": "user", "content": example_msg, "time": datetime.now()}
        )
        bot_reply = generate_bot_response("example prompt", st.session_state.current_level)
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply, "time": datetime.now()}
        )

    if st.button("Give me 3 tips for better prompts"):
        tips_msg = "Give me tips for better prompts."
        st.session_state.messages.append(
            {"role": "user", "content": tips_msg, "time": datetime.now()}
        )
        bot_reply = generate_bot_response("tips for better prompts", st.session_state.current_level)
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply, "time": datetime.now()}
        )

with col_right:
    st.subheader("Chat with GrantsBot")

    # Chat history
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            time_str = msg["time"].strftime("%H:%M")
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-meta">You · {time_str}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="chat-bubble-user">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-meta">GrantsBot · {time_str}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="chat-bubble-bot">{msg["content"]}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Input area
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_area(
            "Type a question, scenario, or grant-related task:",
            placeholder="Example: “Help me design a prompt to summarize a WIOA RFP in plain language.”",
            height=100
        )
        submitted = st.form_submit_button("Send")

    if submitted and user_input.strip():
        st.session_state.messages.append(
            {"role": "user", "content": user_input.strip(), "time": datetime.now()}
        )
        bot_reply = generate_bot_response(user_input, st.session_state.current_level)
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply, "time": datetime.now()}
        )
        st.experimental_rerun()
