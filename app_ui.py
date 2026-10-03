import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="HealthSync | Digital Telehealth Network",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Styling
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* Top Bar Features */
    .top-bar-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-top: 3px solid #38bdf8;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
    }
    .top-bar-title {
        color: #38bdf8;
        font-weight: 700;
        font-size: 13px;
    }
    .top-bar-desc {
        color: #94a3b8;
        font-size: 11px;
    }

    /* Landing Banners */
    .hero-patient {
        background: linear-gradient(135deg, #0284c7 0%, #0f172a 100%);
        border: 1px solid #0369a1;
        border-radius: 16px;
        padding: 35px 20px;
        text-align: center;
        margin-bottom: 25px;
    }
    .hero-doctor {
        background: linear-gradient(135deg, #0d9488 0%, #0f172a 100%);
        border: 1px solid #0f766e;
        border-radius: 16px;
        padding: 35px 20px;
        text-align: center;
        margin-bottom: 25px;
    }
    .hero-title {
        font-size: 30px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 8px;
    }
    .hero-subtitle {
        font-size: 15px;
        color: #e2e8f0;
        max-width: 600px;
        margin: 0 auto;
    }

    /* Homepage Feature Box */
    .home-feature-box {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if "logged_in_role" not in st.session_state:
    st.session_state.logged_in_role = None  # None, "Patient", or "Doctor"
if "patient_symptoms" not in st.session_state:
    st.session_state.patient_symptoms = ""
if "patient_need" not in st.session_state:
    st.session_state.patient_need = ""
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "🏠 Home Page"
if "wallet_balance" not in st.session_state:
    st.session_state.wallet_balance = 200.00
if "escrow_locked" not in st.session_state:
    st.session_state.escrow_locked = 0.00
if "doctor_wallet" not in st.session_state:
    st.session_state.doctor_wallet = 0.00

# =====================================================================
# 1. FEATURES AT THE VERY TOP OF THE APP
# =====================================================================
st.markdown("##### 🏥 HealthSync Global Network Status")

tb1, tb2, tb3, tb4 = st.columns(4)

with tb1:
    st.markdown("""
    <div class="top-bar-card">
        <div class="top-bar-title">🔒 Escrow Protected</div>
        <div class="top-bar-desc">Payments locked until consultation complete</div>
    </div>
    """, unsafe_allow_html=True)

with tb2:
    st.markdown("""
    <div class="top-bar-card">
        <div class="top-bar-title">🚨 Emergency SOS</div>
        <div class="top-bar-desc">Automated AI emergency triage routing</div>
    </div>
    """, unsafe_allow_html=True)

with tb3:
    st.markdown("""
    <div class="top-bar-card">
        <div class="top-bar-title">👨‍⚕️ Restricted Doctor Portal</div>
        <div class="top-bar-desc">Mandatory MDCN regulatory checks</div>
    </div>
    """, unsafe_allow_html=True)

with tb4:
    st.markdown("""
    <div class="top-bar-card">
        <div class="top-bar-title">💊 Smart Pharmacy</div>
        <div class="top-bar-desc">Dynamic stock locator & doorstep delivery</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Sidebar Financial Ledger & Status
st.sidebar.header("💳 Financial Overview")
st.sidebar.metric("Patient Balance", f"${st.session_state.wallet_balance:.2f}")
st.sidebar.metric("Escrow Locked", f"${st.session_state.escrow_locked:.2f}")
st.sidebar.metric("Doctor Wallet", f"${st.session_state.doctor_wallet:.2f}")

if st.session_state.logged_in_role:
    st.sidebar.divider()
    st.sidebar.success(f"Logged in as: **{st.session_state.logged_in_role}**")
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in_role = None
        st.session_state.active_tab = "🏠 Home Page"
        st.rerun()

# Navigation Router
nav_options = ["🏠 Home Page", "🩺 Patient Landing Page", "👨‍⚕️ Doctor Landing Page"]
if st.session_state.logged_in_role == "Patient":
    nav_options.extend(["Step 1: Clinical Triage", "Step 2: Specialist Match", "Step 3: Escrow Booking", "Step 4: Virtual Consultation", "Step 5: Pharmacy & Prescriptions"])
elif st.session_state.logged_in_role == "Doctor":
    nav_options.extend(["Doctor Dashboard", "Patient Queue & E-Prescribe", "Practitioner Earnings"])

selected_tab = st.selectbox("📌 Select Portal View", nav_options, index=nav_options.index(st.session_state.active_tab) if st.session_state.active_tab in nav_options else 0)
st.session_state.active_tab = selected_tab

st.divider()

# =====================================================================
# 2. MAIN HOME PAGE (FEATURES SECTION INSIDE HOME PAGE)
# =====================================================================
if st.session_state.active_tab == "🏠 Home Page":
    st.markdown("## Welcome to HealthSync Telehealth")
    st.write("Connecting patients with verified medical practitioners in minutes.")
    
    st.subheader("✨ Key Features & Capabilities")
    
    hf1, hf2, hf3 = st.columns(3)
    with hf1:
        st.markdown("""
        <div class="home-feature-box">
            <h4>🩺 Patient Symptom Intake</h4>
            <p>Direct triage screening allowing patients to detail medical needs and symptom severity upfront.</p>
        </div>
        """, unsafe_allow_html=True)
    with hf2:
        st.markdown("""
        <div class="home-feature-box">
            <h4>🔐 Restricted Doctor Licensing</h4>
            <p>Strict access portal verifying MDCN license credentials before practitioner authentication.</p>
        </div>
        """, unsafe_allow_html=True)
    with hf3:
        st.markdown("""
        <div class="home-feature-box">
            <h4>💰 Integrated Escrow Ledger</h4>
            <p>Guaranteed safety where patient funds remain protected until consultation completion.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.write("### Choose Your Access Portal")
    
    col_p, col_d = st.columns(2)
    with col_p:
        if st.button("Go to Patient Portal Landing Page", type="primary", use_container_width=True):
            st.session_state.active_tab = "🩺 Patient Landing Page"
            st.rerun()

    with col_d:
        if st.button("Go to Doctor Restricted Landing Page", use_container_width=True):
            st.session_state.active_tab = "👨‍⚕️ Doctor Landing Page"
            st.rerun()

# =====================================================================
# 3. SEPARATE LANDING PAGE FOR PATIENTS
# =====================================================================
elif st.session_state.active_tab == "🩺 Patient Landing Page":
    st.markdown("""
    <div class="hero-patient">
        <div class="hero-title">Patient Portal Landing Page</div>
        <div class="hero-subtitle">
            Get matched with top medical specialists. Complete intake details to log in.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🩺 Patient Intake & Login")
    
    p_email = st.text_input("Patient Email / Username", "patient@healthsync.com")
    
    # 1. What do you need help for?
    p_need = st.selectbox("What do you need help for?", [
        "General Medical Consultation",
        "Eye / Vision Concern (Ophthalmology)",
        "Skin Care & Rashes (Dermatology)",
        "Sinus or Respiratory Issues",
        "Urgent Medical Triage"
    ])
    
    # 2. Describe your symptoms
    p_symptoms = st.text_area("Describe your symptoms:", placeholder="e.g., Redness in eyes, blurred vision, and slight itching since yesterday.")
    
    # 3. Password
    p_password = st.text_input("Enter Account Password", type="password")

    if st.button("Log In as Patient", type="primary"):
        if not p_symptoms.strip():
            st.warning("⚠️ Please describe your symptoms before logging in.")
        elif not p_password:
            st.error("❌ Password is required.")
        else:
            st.session_state.patient_need = p_need
            st.session_state.patient_symptoms = p_symptoms
            st.session_state.logged_in_role = "Patient"
            st.session_state.active_tab = "Step 1: Clinical Triage"
            st.success("✅ Patient authentication successful! Redirecting to triage...")
            st.rerun()

# =====================================================================
# 4. SEPARATE RESTRICTED LANDING PAGE FOR DOCTORS
# =====================================================================
elif st.session_state.active_tab == "👨‍⚕️ Doctor Landing Page":
    st.markdown("""
    <div class="hero-doctor">
        <div class="hero-title">Medical Practitioner Portal</div>
        <div class="hero-subtitle">
            Restricted portal for registered medical doctors and specialists.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("👨‍⚕️ Restricted Doctor Access Login")
    st.warning("🔒 **Restricted Access Notice:** Doctors must verify their official regulatory license prefix (**MDCN/**) to gain access.")

    d_license = st.text_input("Medical License Number (MDCN Reg No.)", placeholder="MDCN/2023/1054")
    d_email = st.text_input("Practitioner Professional Email", "dr.samuel@hospital.org")
    d_password = st.text_input("Practitioner Password", type="password")

    if st.button("Verify Credentials & Log In as Doctor", type="primary"):
        if not d_license.startswith("MDCN/"):
            st.error("❌ ACCESS DENIED: Invalid license number format. Must start with official prefix ('MDCN/').")
        elif not d_password:
            st.error("❌ Password is required.")
        else:
            st.session_state.logged_in_role = "Doctor"
            st.session_state.active_tab = "Doctor Dashboard"
            st.success(f"✅ CREDENTIALS VERIFIED: Welcome, Doctor ({d_license})!")
            st.rerun()

# =====================================================================
# PATIENT WORKFLOW STEPS
# =====================================================================
elif st.session_state.active_tab == "Step 1: Clinical Triage":
    st.header("Step 1: Symptom Triage Check")
    st.info(f"**Medical Need:** {st.session_state.patient_need}")
    st.write(f"**Symptom Description:** {st.session_state.patient_symptoms}")

    if st.button("Run AI Triage Check", type="primary"):
        if "chest pain" in st.session_state.patient_symptoms.lower():
            st.error("🚨 CRITICAL EMERGENCY SOS DETECTED! Bypassing standard booking to emergency services.")
        else:
            st.success("Triage Complete: Specialty matched based on reported symptoms.")

elif st.session_state.active_tab == "Step 2: Specialist Match":
    st.header("Step 2: Specialist Match")
    st.write("Matched Specialist: **Dr. Alice Vance** - Consultation Fee: **$120.00**")

elif st.session_state.active_tab == "Step 3: Escrow Booking":
    st.header("Step 3: Escrow Payment Lock")
    if st.button("Lock $120.00 in Escrow", type="primary"):
        if st.session_state.wallet_balance >= 120.00:
            st.session_state.wallet_balance -= 120.00
            st.session_state.escrow_locked = 120.00
            st.success("✅ $120.00 successfully locked in Escrow!")

elif st.session_state.active_tab == "Step 4: Virtual Consultation":
    st.header("Step 4: Consultation Room")
    st.success("Virtual call active.")

elif st.session_state.active_tab == "Step 5: Pharmacy & Prescriptions":
    st.header("Step 5: Pharmacy Fulfillment")
    st.write("Prescription active: Prednisone Eye Drops.")

# =====================================================================
# DOCTOR WORKFLOW STEPS
# =====================================================================
elif st.session_state.active_tab == "Doctor Dashboard":
    st.header("👨‍⚕️ Doctor Dashboard")
    st.success("Status: Online & License Verified.")
    st.write("Active Queue: **1 Patient Ready**")

elif st.session_state.active_tab == "Patient Queue & E-Prescribe":
    st.header("✍️ Sign E-Prescription & Trigger Payout")
    st.text_area("Patient Symptoms:", st.session_state.patient_symptoms if st.session_state.patient_symptoms else "Eye pain & redness")
    st.text_area("Prescription Details:", "Prednisone Eye Drops - 2 drops twice daily")
    
    if st.button("Sign E-Prescription & Release Escrow", type="primary"):
        if st.session_state.escrow_locked > 0:
            st.session_state.doctor_wallet += st.session_state.escrow_locked
            st.session_state.escrow_locked = 0.00
            st.balloons()
            st.success("✅ E-Prescription signed! Escrow funds released to Doctor Wallet.")

elif st.session_state.active_tab == "Practitioner Earnings":
    st.header("💳 Practitioner Earnings Ledger")
    st.metric("Total Earnings Balance", f"${st.session_state.doctor_wallet:.2f}")