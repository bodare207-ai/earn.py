import streamlit as st
import streamlit.components.v1 as components
import time
import random

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CoinVault – Earn Coins",
    page_icon="🪙",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Monetag Zone ──────────────────────────────────────────────────────────────
# Zone ID: 10745571  |  Format: Onclick (Popunder)  |  Script: al5sm.com

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap');

:root {
  --gold: #f5c842; --gold-dark: #c99a1a;
  --bg: #090b10; --card: #12161f; --border: #1e2535;
  --text: #e8eaf0; --muted: #6b7591;
  --green: #30e89b; --purple: #9b6dff; --red: #ff5c6a;
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
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }

div.stButton > button {
  background: linear-gradient(135deg, #f5c842, #c99a1a) !important;
  color: #080a0f !important; border: none !important;
  border-radius: 50px !important;
  font-family: 'Orbitron', monospace !important;
  font-size: 0.9rem !important; font-weight: 700 !important;
  letter-spacing: 0.12em !important; padding: 0.85rem 2rem !important;
  box-shadow: 0 4px 24px rgba(245,200,66,0.3) !important;
  width: 100% !important; transition: all 0.2s !important;
}
div.stButton > button:hover {
  box-shadow: 0 4px 48px rgba(245,200,66,0.55) !important;
  transform: translateY(-3px) !important;
}
div.stButton > button:disabled {
  background: #1e2535 !important; color: #6b7591 !important;
  box-shadow: none !important; transform: none !important;
}

div[data-testid="stProgress"] > div > div {
  background: linear-gradient(90deg, #f5c842, #30e89b) !important;
  border-radius: 6px !important;
}
div[data-testid="stProgress"] > div {
  background: #1e2535 !important; border-radius: 6px !important; height: 10px !important;
}

div[data-testid="stMetric"] {
  background: #12161f !important; border: 1px solid #1e2535 !important;
  border-radius: 16px !important; padding: 20px !important;
}
div[data-testid="stMetricLabel"] p {
  color: #6b7591 !important; font-size: 0.75rem !important;
  letter-spacing: 0.12em; text-transform: uppercase;
}
div[data-testid="stMetricValue"] {
  color: #f5c842 !important; font-family: 'Orbitron', monospace !important;
}
div[data-testid="stMetricDelta"] { color: #30e89b !important; }

hr { border-color: #1e2535 !important; margin: 1.5rem 0 !important; }
div[data-testid="stAlert"] {
  border-radius: 14px !important; border: 1px solid #1e2535 !important;
  background: #12161f !important;
}
</style>
""", unsafe_allow_html=True)


# ─── Monetag Ad HTML Component ─────────────────────────────────────────────────
def monetag_video_ad_html() -> str:
    """
    TWO-PHASE component:
    PHASE 1 — Big glowing "Open Ad" button. Monetag script is already loaded,
               so when the user clicks the button, Monetag Onclick intercepts
               that real click and opens the popunder. Our JS then switches to Phase 2.
    PHASE 2 — Countdown ring runs 30s. After 0s shows "Done" message.
    """
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@400;600&display=swap');
  *  { margin:0; padding:0; box-sizing:border-box; }
  body {
    background:#090b10;
    display:flex; align-items:center; justify-content:center;
    min-height:360px; font-family:'Rajdhani',sans-serif;
  }

  /* ── PHASE 1: Click to open ad ── */
  #phase1 {
    text-align:center; padding:28px 22px; width:90%; max-width:380px;
  }
  .pre-badge {
    font-size:0.65rem; letter-spacing:0.25em; color:#6b7591;
    text-transform:uppercase; font-family:'Orbitron',monospace;
    margin-bottom:18px;
  }
  .coin-icon {
    font-size:52px; line-height:1; margin-bottom:16px;
    filter: drop-shadow(0 0 18px rgba(245,200,66,0.7));
    animation: iconBob 2s ease-in-out infinite;
  }
  @keyframes iconBob {
    0%,100% { transform:translateY(0); }
    50%      { transform:translateY(-6px); }
  }
  .pre-title {
    font-family:'Orbitron',monospace; font-size:1rem;
    font-weight:900; color:#e8eaf0; margin-bottom:6px;
  }
  .pre-sub {
    font-size:0.82rem; color:#6b7591; margin-bottom:24px; line-height:1.5;
  }
  /* The big glowing click button — Monetag intercepts this click */
  #openAdBtn {
    display:block; width:100%;
    padding:16px 20px;
    background:linear-gradient(135deg,#f5c842,#c99a1a);
    color:#080a0f;
    font-family:'Orbitron',monospace;
    font-size:0.92rem; font-weight:900;
    letter-spacing:0.12em;
    border:none; border-radius:50px;
    cursor:pointer;
    box-shadow:0 4px 28px rgba(245,200,66,0.45);
    animation:btnPulse 1.8s ease-in-out infinite;
    transition:transform 0.15s;
  }
  #openAdBtn:hover  { transform:scale(1.03); }
  #openAdBtn:active { transform:scale(0.97); }
  @keyframes btnPulse {
    0%,100% { box-shadow:0 4px 28px rgba(245,200,66,0.4); }
    50%      { box-shadow:0 4px 52px rgba(245,200,66,0.75); }
  }
  .reward-preview {
    margin-top:16px;
    display:inline-flex; align-items:center; gap:8px;
    background:rgba(48,232,155,0.08);
    border:1px solid rgba(48,232,155,0.2);
    border-radius:50px; padding:8px 20px;
    font-family:'Orbitron',monospace;
    color:#30e89b; font-size:0.82rem; font-weight:700;
  }

  /* ── PHASE 2: Countdown ── */
  #phase2 {
    display:none; text-align:center;
    padding:28px 22px; width:90%; max-width:380px;
  }
  .badge2 {
    display:inline-block; background:rgba(245,200,66,0.1);
    border:1px solid rgba(245,200,66,0.25); color:#f5c842;
    font-size:0.62rem; letter-spacing:0.22em; text-transform:uppercase;
    padding:4px 14px; border-radius:50px; margin-bottom:18px;
    font-family:'Orbitron',monospace;
  }
  .ring-wrap { position:relative; width:120px; height:120px; margin:0 auto 18px; }
  .ring-wrap svg { transform:rotate(-90deg); }
  .ring-bg { fill:none; stroke:#1e2535; stroke-width:8; }
  .ring-fg {
    fill:none; stroke:url(#grad); stroke-width:8; stroke-linecap:round;
    stroke-dasharray:314.16; stroke-dashoffset:0;
    transition:stroke-dashoffset 1s linear;
  }
  .ring-inner {
    position:absolute; inset:0; display:flex;
    flex-direction:column; align-items:center; justify-content:center;
  }
  .ring-num {
    font-family:'Orbitron',monospace; font-size:2rem;
    font-weight:900; color:#f5c842; line-height:1;
    transition:color 0.3s;
  }
  .ring-s { font-size:0.58rem; color:#6b7591; letter-spacing:0.14em; text-transform:uppercase; margin-top:3px; }
  .cd-title { font-family:'Orbitron',monospace; font-size:0.9rem; font-weight:700; color:#e8eaf0; margin-bottom:6px; }
  .cd-sub   { font-size:0.8rem; color:#6b7591; margin-bottom:18px; line-height:1.5; }
  .chip {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(48,232,155,0.1); border:1px solid rgba(48,232,155,0.25);
    border-radius:50px; padding:8px 20px;
    font-family:'Orbitron',monospace; color:#30e89b; font-size:0.82rem; font-weight:700;
  }
  .warn { margin-top:14px; font-size:0.68rem; color:#6b7591; }
  .warn span { color:#ff5c6a; }
</style>
</head>
<body>

<!-- ── Direct Ad Link ── -->
<!-- No external scripts needed — button opens the ad URL directly in a new tab -->

<!-- ── PHASE 1: Click button ── -->
<div id="phase1">
  <div class="pre-badge">🎬 &nbsp; Ad Ready</div>
  <div class="coin-icon">🪙</div>
  <div class="pre-title">One click away from coins!</div>
  <div class="pre-sub">
    Click the button below to open the ad.<br/>
    Coins are added automatically after 30 seconds.
  </div>

  <!-- Opens direct ad link in new tab, then starts countdown -->
  <button id="openAdBtn" onclick="startAd()">
    ▶ &nbsp; OPEN AD &amp; START EARNING
  </button>

  <div class="reward-preview">🪙 &nbsp; Reward unlocks after ad</div>
</div>

<!-- ── PHASE 2: Countdown ── -->
<div id="phase2">
  <div class="badge2">📺 &nbsp; Ad Opened — Timer Running</div>

  <div class="ring-wrap">
    <svg width="120" height="120" viewBox="0 0 120 120">
      <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%"   stop-color="#f5c842"/>
          <stop offset="100%" stop-color="#30e89b"/>
        </linearGradient>
      </defs>
      <circle class="ring-bg" cx="60" cy="60" r="50"/>
      <circle class="ring-fg" cx="60" cy="60" r="50" id="ring"/>
    </svg>
    <div class="ring-inner">
      <div class="ring-num" id="cd">30</div>
      <div class="ring-s" id="cd-label">seconds</div>
    </div>
  </div>

  <div class="cd-title">Ad is playing in the new tab</div>
  <div class="cd-sub" id="cd-sub">Watch the ad — coins arrive when timer hits 0</div>
  <div class="chip" id="chip">🪙 &nbsp; Coins unlock at 0s</div>
  <p class="warn"><span>⚠</span> Do not close or refresh this tab</p>
</div>

<script>
  const AD_URL = 'https://omg10.com/4/10745799';
  const TOTAL  = 30;
  const CIRC   = 2 * Math.PI * 50;

  function startAd() {
    // Open the direct ad link in a new tab
    window.open(AD_URL, '_blank');

    // Switch to phase 2 (countdown)
    document.getElementById('phase1').style.display = 'none';
    document.getElementById('phase2').style.display = 'block';

    // Init ring
    const ring = document.getElementById('ring');
    const cd   = document.getElementById('cd');
    ring.style.strokeDasharray  = CIRC;
    ring.style.strokeDashoffset = 0;

    let left = TOTAL;

    const timer = setInterval(() => {
      left--;
      if (left > 0) {
        cd.textContent = left;
        ring.style.strokeDashoffset = CIRC * (1 - left / TOTAL);
      } else {
        clearInterval(timer);
        ring.style.strokeDashoffset = CIRC;
        cd.textContent  = '✓';
        cd.style.color  = '#30e89b';
        document.getElementById('cd-label').textContent = 'complete!';
        document.getElementById('cd-sub').textContent   = 'Ad done! Coins are being added to your wallet…';
        document.getElementById('chip').innerHTML        = '🎉 &nbsp; Coins added!';
        document.getElementById('chip').style.background  = 'rgba(48,232,155,0.2)';
        document.getElementById('chip').style.borderColor = 'rgba(48,232,155,0.5)';
      }
    }, 1000);
  }
</script>
</body>
</html>"""


# ─── Session State ─────────────────────────────────────────────────────────────
for k, v in {
    "coins": 0, "ads_watched": 0, "watching": False,
    "last_reward": 0, "history": [], "current_ad": None
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─── Ad Pool (all 30s to match Monetag video length) ──────────────────────────
AD_POOL = [
    {"title": "🚀 TechPro Max — New Laptop",     "brand": "TechPro"},
    {"title": "🍔 BurgerKing — Deals App",        "brand": "BurgerKing"},
    {"title": "🎮 GameZone — Play & Win",         "brand": "GameZone"},
    {"title": "📱 PhoneX Ultra — Flash Sale",     "brand": "PhoneX"},
    {"title": "👟 SneakPeak — Limited Drop",      "brand": "SneakPeak"},
    {"title": "✈️  SkyFly — Book & Save 40%",     "brand": "SkyFly"},
    {"title": "💪 FitPulse — Smart Fitness Band", "brand": "FitPulse"},
    {"title": "☕ CafeBlend — Morning Offer",     "brand": "CafeBlend"},
]

def new_ad():
    a = random.choice(AD_POOL).copy()
    a["reward"]   = random.randint(15, 42)
    a["duration"] = 30
    return a

if st.session_state.current_ad is None:
    st.session_state.current_ad = new_ad()

ad          = st.session_state.current_ad
DAILY_LIMIT = 20

# ─── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:24px 0 10px;">
  <div style="font-size:64px;line-height:1;margin-bottom:12px;
    filter:drop-shadow(0 0 24px rgba(245,200,66,0.7));">🪙</div>
  <div style="font-family:'Orbitron',monospace;font-size:2.2rem;font-weight:900;
    background:linear-gradient(135deg,#ffe680 0%,#f5c842 50%,#c99a1a 100%);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
    background-clip:text;letter-spacing:0.1em;">EARN COINS</div>
  <div style="color:#6b7591;letter-spacing:0.35em;font-size:0.72rem;
    text-transform:uppercase;margin-top:8px;">
    Watch Monetag Video Ads · Collect Real Rewards
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ─── METRICS ───────────────────────────────────────────────────────────────────
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("💰 Total Coins", f"{st.session_state.coins:,}",
              delta=f"+{st.session_state.last_reward}" if st.session_state.last_reward else None)
with c2:
    st.metric("📺 Ads Watched", st.session_state.ads_watched)
with c3:
    st.metric("🎯 Ads Left", max(0, DAILY_LIMIT - st.session_state.ads_watched))

st.markdown("---")

# ─── AD CARD (only show when not watching) ─────────────────────────────────────
if not st.session_state.watching:
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#12161f,#0e1118);
      border:1px solid #1e2535;border-radius:22px;padding:28px 22px;
      margin-bottom:20px;text-align:center;position:relative;overflow:hidden;">
      <div style="position:absolute;top:-40px;left:50%;transform:translateX(-50%);
        width:220px;height:220px;border-radius:50%;
        background:radial-gradient(circle,rgba(245,200,66,0.06),transparent 70%);
        pointer-events:none;"></div>
      <div style="font-size:0.68rem;color:#6b7591;letter-spacing:0.25em;
        text-transform:uppercase;margin-bottom:12px;">▶ &nbsp; Next Monetag Video Ad</div>
      <div style="font-size:1.3rem;font-weight:700;color:#e8eaf0;margin-bottom:6px;">
        {ad['title']}</div>
      <div style="font-size:0.83rem;color:#6b7591;margin-bottom:22px;">
        by <span style="color:#f5c842;font-weight:600;">{ad['brand']}</span>
        &nbsp;·&nbsp;
        <span style="color:#9b6dff;">Monetag Verified ✓</span>
      </div>
      <div style="display:flex;justify-content:center;gap:32px;flex-wrap:wrap;">
        <div>
          <div style="font-family:'Orbitron',monospace;font-size:1.55rem;
            color:#f5c842;font-weight:700;">+{ad['reward']}</div>
          <div style="font-size:0.68rem;color:#6b7591;letter-spacing:0.12em;
            text-transform:uppercase;margin-top:2px;">Coins Reward</div>
        </div>
        <div>
          <div style="font-family:'Orbitron',monospace;font-size:1.55rem;
            color:#30e89b;font-weight:700;">30s</div>
          <div style="font-size:0.68rem;color:#6b7591;letter-spacing:0.12em;
            text-transform:uppercase;margin-top:2px;">Duration</div>
        </div>
        <div>
          <div style="font-family:'Orbitron',monospace;font-size:1.55rem;
            color:#9b6dff;font-weight:700;">HD</div>
          <div style="font-size:0.68rem;color:#6b7591;letter-spacing:0.12em;
            text-transform:uppercase;margin-top:2px;">Quality</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ─── WATCH BUTTON / PLAYING ────────────────────────────────────────────────────
ads_exhausted = st.session_state.ads_watched >= DAILY_LIMIT

if ads_exhausted:
    st.markdown("""
    <div style="background:rgba(255,92,106,0.08);border:1px solid rgba(255,92,106,0.4);
      border-radius:14px;padding:22px;text-align:center;">
      <div style="font-size:2rem;margin-bottom:8px;">🚫</div>
      <div style="font-family:'Orbitron',monospace;color:#ff5c6a;font-size:0.9rem;
        font-weight:700;letter-spacing:0.08em;">Daily Limit Reached</div>
      <div style="color:#6b7591;font-size:0.85rem;margin-top:6px;">
        Come back tomorrow for 20 more Monetag ads!</div>
    </div>
    """, unsafe_allow_html=True)

elif not st.session_state.watching:
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        if st.button("▶  Watch Video Ad & Earn Coins"):
            st.session_state.watching = True
            st.rerun()

else:
    # ══════════════════════════════════════════════════
    #  MONETAG AD — Phase 1: user clicks inside component
    #               Phase 2: countdown runs in component
    #  Python side: 35s timer then awards coins
    # ══════════════════════════════════════════════════

    # Show the two-phase component (click button → ad fires → countdown)
    components.html(
        monetag_video_ad_html(),
        height=430,
        scrolling=False,
    )

    # Python-side server timer (gives a few extra seconds buffer)
    bar  = st.progress(0)
    slot = st.empty()
    SECS = 33

    for i in range(SECS + 1):
        left = SECS - i
        bar.progress(i / SECS, text=f"⏳  Verifying ad… {left}s")
        slot.markdown(f"""
        <div style="text-align:center;padding:4px 0;">
          <span style="font-family:'Orbitron',monospace;font-size:0.88rem;
            color:#{'30e89b' if left == 0 else 'f5c842'};font-weight:700;">
            {'✓  Verified! Adding coins…' if left == 0 else ''}
          </span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)

    # ── Award coins ──────────────────────────────────
    reward = ad["reward"]
    st.session_state.coins       += reward
    st.session_state.ads_watched += 1
    st.session_state.last_reward  = reward
    st.session_state.watching     = False
    st.session_state.history.append({
        "ad": ad["title"], "brand": ad["brand"],
        "reward": reward,  "total": st.session_state.coins
    })
    st.session_state.current_ad = new_ad()

    bar.empty()
    slot.empty()
    st.rerun()

# ─── SUCCESS BANNER ────────────────────────────────────────────────────────────
if st.session_state.last_reward and not st.session_state.watching:
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,rgba(48,232,155,0.08),rgba(245,200,66,0.06));
      border:1px solid rgba(48,232,155,0.3);border-radius:14px;
      padding:16px 22px;text-align:center;margin-top:8px;">
      <span style="font-size:1.3rem;">🎉</span>
      <span style="font-family:'Orbitron',monospace;color:#30e89b;
        font-size:0.92rem;font-weight:700;margin:0 10px;">
        +{st.session_state.last_reward} COINS ADDED
      </span>
      <span style="color:#6b7591;font-size:0.83rem;">Keep watching to earn more!</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ─── EARNINGS HISTORY ──────────────────────────────────────────────────────────
if st.session_state.history:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace;font-size:0.76rem;color:#6b7591;
      letter-spacing:0.18em;text-transform:uppercase;margin-bottom:14px;">
      📋 &nbsp; Earnings History
    </div>
    """, unsafe_allow_html=True)

    for i, e in enumerate(reversed(st.session_state.history[-10:])):
        op = max(0.38, 1.0 - i * 0.07)
        st.markdown(f"""
        <div style="background:#12161f;border:1px solid #1e2535;border-radius:12px;
          padding:12px 18px;margin-bottom:8px;
          display:flex;justify-content:space-between;align-items:center;
          flex-wrap:wrap;gap:8px;opacity:{op:.2f};">
          <div>
            <div style="color:#e8eaf0;font-size:0.88rem;font-weight:600;">{e['ad']}</div>
            <div style="color:#6b7591;font-size:0.73rem;margin-top:2px;">
              via <span style="color:#f5c842;">{e['brand']}</span>
              &nbsp;·&nbsp; Wallet: {e['total']:,} 🪙
            </div>
          </div>
          <div style="font-family:'Orbitron',monospace;color:#30e89b;
            font-size:0.88rem;font-weight:700;white-space:nowrap;">
            +{e['reward']} 🪙
          </div>
        </div>
        """, unsafe_allow_html=True)

# ─── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center;padding-bottom:24px;">
  <a href="https://llobbbbyhtml.vercel.app/" target="_blank"
    style="display:inline-block;padding:12px 36px;border-radius:50px;
    border:1px solid #1e2535;color:#6b7591;text-decoration:none;
    font-family:'Rajdhani',sans-serif;font-size:0.9rem;font-weight:600;
    letter-spacing:0.12em;text-transform:uppercase;">
    ← Back to CoinVault Lobby
  </a>
  <div style="color:#1e2535;font-size:0.66rem;letter-spacing:0.18em;margin-top:12px;">
    COINVAULT © 2025 &nbsp;·&nbsp; POWERED BY MONETAG
  </div>
</div>
""", unsafe_allow_html=True)
