# -----------------------------
# STRONG ACTION VERB TOOL
# -----------------------------
ACTION_VERBS = {
    "Manufacturing": [
        "Assembled", "Fabricated", "Operated", "Calibrated", "Inspected",
        "Optimized", "Maintained", "Troubleshot", "Streamlined", "Produced"
    ],
    "Healthcare & Social Assistance": [
        "Assessed", "Coordinated", "Advocated", "Supported", "Documented",
        "Monitored", "Educated", "Facilitated", "Implemented", "Evaluated"
    ],
    "Professional & Technical Services": [
        "Analyzed", "Developed", "Designed", "Audited", "Consulted",
        "Strategized", "Synthesized", "Optimized", "Executed", "Presented"
    ],
    "Retail Trade": [
        "Engaged", "Promoted", "Upsold", "Processed", "Resolved",
        "Restocked", "Demonstrated", "Tracked", "Organized", "Collaborated"
    ],
    "Education": [
        "Instructed", "Guided", "Adapted", "Assessed", "Mentored",
        "Designed", "Facilitated", "Supported", "Evaluated", "Communicated"
    ]
}

def action_verb_tool():
    st.subheader("Strong Action Verb Generator")
    st.write("Select an industry to get résumé‑ready action verbs.")

    for industry in ACTION_VERBS.keys():
        if st.button(industry):
            verbs = ACTION_VERBS[industry]
            st.markdown(f"### Strong Action Verbs for {industry}")
            st.write(", ".join(verbs))

import streamlit as st

# -----------------------------
# STRONG ACTION VERB TOOL
# -----------------------------
ACTION_VERBS = {
    "Manufacturing": [
        "Assembled", "Fabricated", "Operated", "Calibrated", "Inspected",
        "Optimized", "Maintained", "Troubleshot", "Streamlined", "Produced"
    ],
    "Healthcare & Social Assistance": [
        "Assessed", "Coordinated", "Advocated", "Supported", "Documented",
        "Monitored", "Educated", "Facilitated", "Implemented", "Evaluated"
    ],
    "Professional & Technical Services": [
        "Analyzed", "Developed", "Designed", "Audited", "Consulted",
        "Strategized", "Synthesized", "Optimized", "Executed", "Presented"
    ],
    "Retail Trade": [
        "Engaged", "Promoted", "Upsold", "Processed", "Resolved",
        "Restocked", "Demonstrated", "Tracked", "Organized", "Collaborated"
    ],
    "Education": [
        "Instructed", "Guided", "Adapted", "Assessed", "Mentored",
        "Designed", "Facilitated", "Supported", "Evaluated", "Communicated"
    ]
}

def action_verb_tool():
    st.subheader("Strong Action Verb Generator")
    st.write("Select an industry to get résumé‑ready action verbs.")

    for industry in ACTION_VERBS.keys():
        if st.button(industry):
            verbs = ACTION_VERBS[industry]
            st.markdown(f"### Strong Action Verbs for {industry}")
            st.write(", ".join(verbs))

# Call this inside your sidebar or main layout
# Example:
# with st.sidebar:
#     action_verb_tool()
