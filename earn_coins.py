import streamlit as st
import time
import random

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CoinVault – Earn Coins",
    page_icon="🪙",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap');

/* ── Root ── */
:root {
  --gold: #f5c842;
  --gold-dark: #c99a1a;
  --bg: #090b10;
  --card: #12161f;
  --border: #1e2535;
  --text: #e8eaf0;
  --muted: #6b7591;
  --green: #30e89b;
  --purple: #9b6dff;
  --red: #ff5c6a;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
  background-color: #090b10 !important;
  color: #e8eaf0 !important;
  font-family: 'Rajdhani', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
  background-image:
    linear-gradient(rgba(245,200,66,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(245,200,66,0.03) 1px, transparent 1px);
  background-size: 60px 60px;
}

[data-testid="stHeader"] { background: transparent !important; }

/* Hide streamlit default elements */
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }

/* Buttons */
div.stButton > button {
  background: linear-gradient(135deg, #f5c842, #c99a1a) !important;
  color: #080a0f !important;
  border: none !important;
  border-radius: 50px !important;
  font-family: 'Orbitron', monospace !important;
  font-size: 0.85rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.1em !important;
  padding: 0.7rem 2rem !important;
  transition: all 0.2s !important;
  box-shadow: 0 4px 20px rgba(245,200,66,0.25) !important;
  width: 100% !important;
}
div.stButton > button:hover {
  box-shadow: 0 4px 40px rgba(245,200,66,0.5) !important;
  transform: translateY(-2px) !important;
}
div.stButton > button:disabled {
  background: #1e2535 !important;
  color: #6b7591 !important;
  box-shadow: none !important;
  transform: none !important;
}

/* Progress bar */
div[data-testid="stProgress"] > div > div {
  background: linear-gradient(90deg, #f5c842, #30e89b) !important;
  border-radius: 4px !important;
}
div[data-testid="stProgress"] > div {
  background: #1e2535 !important;
  border-radius: 4px !important;
}

/* Metric */
div[data-testid="stMetric"] {
  background: #12161f !important;
  border: 1px solid #1e2535 !important;
  border-radius: 16px !important;
  padding: 20px !important;
}
div[data-testid="stMetricLabel"] p { color: #6b7591 !important; font-size: 0.8rem !important; letter-spacing: 0.1em; }
div[data-testid="stMetricValue"] { color: #f5c842 !important; font-family: 'Orbitron', monospace !important; }
div[data-testid="stMetricDelta"] { color: #30e89b !important; }

/* Divider */
hr { border-color: #1e2535 !important; margin: 1.5rem 0 !important; }

/* Info/Success/Warning boxes */
div[data-testid="stAlert"] {
  border-radius: 12px !important;
  border: 1px solid #1e2535 !important;
  background: #12161f !important;
}
</style>
""", unsafe_allow_html=True)


# ─── State Init ────────────────────────────────────────────────────────────────
if "coins" not in st.session_state:
    st.session_state.coins = 0
if "ads_watched" not in st.session_state:
    st.session_state.ads_watched = 0
if "watching" not in st.session_state:
    st.session_state.watching = False
if "cooldown" not in st.session_state:
    st.session_state.cooldown = False
if "last_reward" not in st.session_state:
    st.session_state.last_reward = 0
if "history" not in st.session_state:
    st.session_state.history = []


# ─── Ad content pool ───────────────────────────────────────────────────────────
AD_POOL = [
    {"title": "🚀 TechPro Max — New Laptop",      "brand": "TechPro",   "reward": random.randint(10, 30), "duration": 10},
    {"title": "🍔 BurgerKing — Deals App",         "brand": "BurgerKing","reward": random.randint(8,  25), "duration": 8 },
    {"title": "🎮 GameZone — Play & Win",          "brand": "GameZone",  "reward": random.randint(15, 35), "duration": 12},
    {"title": "📱 PhoneX Ultra — Flash Sale",      "brand": "PhoneX",    "reward": random.randint(10, 28), "duration": 10},
    {"title": "👟 SneakPeak — Limited Drop",       "brand": "SneakPeak", "reward": random.randint(12, 30), "duration": 9 },
    {"title": "☕ CafeBlend — Morning Offer",      "brand": "CafeBlend", "reward": random.randint(5,  20), "duration": 7 },
    {"title": "✈️ SkyFly — Book & Save 40%",       "brand": "SkyFly",    "reward": random.randint(20, 40), "duration": 15},
    {"title": "💪 FitPulse — Smart Fitness Band",  "brand": "FitPulse",  "reward": random.randint(10, 25), "duration": 11},
]

# Pick a random ad for this session if not picked
if "current_ad" not in st.session_state:
    st.session_state.current_ad = random.choice(AD_POOL)


# ─── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding: 20px 0 10px;">
  <div style="font-size:60px; margin-bottom:8px; filter: drop-shadow(0 0 20px rgba(245,200,66,0.6));">🪙</div>
  <div style="font-family:'Orbitron',monospace; font-size:2rem; font-weight:900;
    background:linear-gradient(135deg,#ffe680,#f5c842,#c99a1a);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">
    EARN COINS
  </div>
  <div style="color:#6b7591; letter-spacing:0.3em; font-size:0.8rem; text-transform:uppercase; margin-top:6px;">
    Watch Ads · Collect Rewards
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ─── Balance Row ───────────────────────────────────────────────────────────────
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("💰 Total Coins", f"{st.session_state.coins:,}", delta=f"+{st.session_state.last_reward}" if st.session_state.last_reward else None)
with c2:
    st.metric("📺 Ads Watched", st.session_state.ads_watched)
with c3:
    daily_limit = 20
    remaining = max(0, daily_limit - st.session_state.ads_watched)
    st.metric("⏳ Ads Left Today", remaining)

st.markdown("---")

# ─── Current Ad Card ───────────────────────────────────────────────────────────
ad = st.session_state.current_ad

st.markdown(f"""
<div style="background:#12161f; border:1px solid #1e2535; border-radius:20px; padding:28px 24px; margin-bottom:20px; text-align:center;">
  <div style="font-size:0.75rem; color:#6b7591; letter-spacing:0.2em; text-transform:uppercase; margin-bottom:8px;">FEATURED AD</div>
  <div style="font-size:1.4rem; font-weight:700; color:#e8eaf0; margin-bottom:6px;">{ad['title']}</div>
  <div style="font-size:0.85rem; color:#6b7591; margin-bottom:16px;">by <span style="color:#f5c842">{ad['brand']}</span></div>
  <div style="display:flex; justify-content:center; gap:30px; flex-wrap:wrap;">
    <div style="text-align:center;">
      <div style="font-family:'Orbitron',monospace; font-size:1.5rem; color:#f5c842; font-weight:700;">+{ad['reward']}</div>
      <div style="font-size:0.75rem; color:#6b7591; letter-spacing:0.1em;">COINS REWARD</div>
    </div>
    <div style="text-align:center;">
      <div style="font-family:'Orbitron',monospace; font-size:1.5rem; color:#30e89b; font-weight:700;">{ad['duration']}s</div>
      <div style="font-size:0.75rem; color:#6b7591; letter-spacing:0.1em;">DURATION</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─── Watch Ad Button + Logic ────────────────────────────────────────────────────
ads_exhausted = st.session_state.ads_watched >= daily_limit

if ads_exhausted:
    st.markdown("""
    <div style="background:rgba(255,92,106,0.1); border:1px solid #ff5c6a; border-radius:12px;
      padding:20px; text-align:center; color:#ff5c6a; font-family:'Orbitron',monospace; font-size:0.9rem;">
      ⚠️ Daily limit reached! Come back tomorrow for more ads.
    </div>
    """, unsafe_allow_html=True)

elif not st.session_state.watching:
    if st.button("▶  Watch Ad & Earn Coins"):
        st.session_state.watching = True
        st.rerun()

else:
    # ── Ad is playing ──
    ad_placeholder = st.empty()
    progress_bar = st.progress(0)

    with ad_placeholder.container():
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#12161f,#0e1118);
            border:2px solid #f5c842; border-radius:20px;
            padding:40px 24px; text-align:center;
            box-shadow: 0 0 40px rgba(245,200,66,0.15);">
          <div style="font-size:3rem; margin-bottom:12px; animation:pulse 1s infinite;">📺</div>
          <div style="font-family:'Orbitron',monospace; color:#f5c842; font-size:1rem; font-weight:700; margin-bottom:8px;">
            AD PLAYING
          </div>
          <div style="color:#e8eaf0; font-size:1.1rem; font-weight:600; margin-bottom:4px;">{ad['title']}</div>
          <div style="color:#6b7591; font-size:0.85rem;">Do not close this page during the ad</div>
        </div>
        """, unsafe_allow_html=True)

    duration = ad["duration"]
    for i in range(duration + 1):
        progress_bar.progress(i / duration, text=f"⏱️ {duration - i}s remaining...")
        time.sleep(1)

    # ── Reward ──
    reward = ad["reward"]
    st.session_state.coins += reward
    st.session_state.ads_watched += 1
    st.session_state.last_reward = reward
    st.session_state.watching = False
    st.session_state.history.append({
        "ad": ad["title"],
        "reward": reward,
        "total": st.session_state.coins
    })
    # Pick new ad
    st.session_state.current_ad = random.choice(AD_POOL)
    st.session_state.current_ad["reward"] = random.randint(8, 40)

    ad_placeholder.empty()
    progress_bar.empty()
    st.rerun()


# ─── Success banner after watching ────────────────────────────────────────────
if st.session_state.last_reward and not st.session_state.watching:
    st.success(f"🎉 +{st.session_state.last_reward} Coins earned! Keep watching to earn more.")


st.markdown("---")

# ─── History Table ─────────────────────────────────────────────────────────────
if st.session_state.history:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:0.85rem; color:#6b7591;
      letter-spacing:0.15em; text-transform:uppercase; margin-bottom:12px;">
      📋 Earnings History
    </div>
    """, unsafe_allow_html=True)

    for entry in reversed(st.session_state.history[-8:]):
        st.markdown(f"""
        <div style="background:#12161f; border:1px solid #1e2535; border-radius:12px;
          padding:12px 18px; margin-bottom:8px; display:flex; justify-content:space-between;
          align-items:center; flex-wrap:wrap; gap:8px;">
          <span style="color:#e8eaf0; font-size:0.9rem;">{entry['ad']}</span>
          <span style="color:#30e89b; font-family:'Orbitron',monospace; font-size:0.85rem; font-weight:700;">
            +{entry['reward']} 🪙
          </span>
        </div>
        """, unsafe_allow_html=True)

# ─── Back to Lobby ─────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center;">
  <a href="https://bodare207-ai.github.io/index.html/" target="_blank"
    style="display:inline-block; padding:12px 32px; border-radius:50px;
    border:1px solid #1e2535; color:#6b7591; text-decoration:none;
    font-family:'Rajdhani',sans-serif; font-size:0.9rem; letter-spacing:0.1em;
    text-transform:uppercase; transition:all 0.2s;">
    ← Back to Lobby
  </a>
</div>
<div style="text-align:center; margin-top:20px; color:#1e2535; font-size:0.7rem; letter-spacing:0.15em;">
  COINVAULT © 2025
</div>
""", unsafe_allow_html=True)
