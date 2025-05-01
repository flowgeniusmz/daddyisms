import streamlit as st
import datetime

def daddyism_prompt():
    
    prompt = """
# 🧠 Daddyism + Meme Generator Prompt

You are to create hilarious, insightful, and visually driven content for a fictional character named **Daddy Trades** — a sarcastic, brutally honest, seasoned trader-dad who delivers one-liner truths about day trading, risk, and market behavior. His voice is like Randy Marsh meets a financial mentor: sarcastic, savage, and secretly wise.

DO NOT USE **PREMARKET** OR ANY VARIATION OF PREMARKET AS A CATEGORY FOR DADDYISMS. 

## 🎯 OBJECTIVE
Generate a daily **Daddyism** and a matching **meme concept** for traders. Your response must include:

### 1. Title  
A clever and short name that reflects the theme of the Daddyism (e.g., “Theta Decay Denial”, “Jerome the Arsonist”).

### 2. Category  
Choose from: `Psychology`, `Risk Management`, `Market Conditions`, `Options`, `Technical Analysis`, `Macro / Fed`, `Community`, `Premarket`, `Fundamentals`, `Discipline`, `FOMO`, or create a fitting category.

### 3. Daddyism  
A one-liner (max 30 words) written in Daddy Trades' sarcastic, meme-worthy style. It should reflect a hard truth or a common trader mistake with a humorous punch.

### 4. Meme Description  
A detailed description for generating a meme image that captures the Daddyism visually.

#### Use this visual style guide:
- Character: Light-skinned cartoon man with black mustache, black sunglasses, golden crown, teal shirt
- Style: Flat, bold line-art, meme aesthetic
- Text layout: Bold top + bottom caption with sarcastic tone
- Scene should exaggerate the concept in a funny or savage way

---

## ✅ FORMAT YOUR OUTPUT LIKE THIS:

Title: Flight Sim Finance  
Category: Risk Management  
Daddyism: “Calling yourself a trader while ignoring risk is like calling yourself a pilot because you’ve played Microsoft Flight Simulator.”  
Meme Description: Daddy Trades, in aviator sunglasses and a pilot’s cap, sits in a cardboard box labeled “JET” holding a broken joystick. A red crashing chart looms behind.  
Top Caption: “I GOT THIS, I’VE PLAYED SIM MODE”  
Bottom Caption: “STILL THINKS RISK MANAGEMENT IS OPTIONAL.”

---

## 🧪 EXAMPLES

### Example 1

Title: Jerome the Arsonist  
Category: Macro / Fed  
Daddyism: “Jerome Powell raised rates so fast my house equity time-traveled back to 2008.”  
Meme Description: Daddy Trades stands in front of a flaming house labeled “Housing Market.” Jerome Powell’s face appears ominously in smoke above.  
Top Caption: “JEROME THE ARSONIST”  
Bottom Caption: “RATES UP. HOME VALUE DOWN.”

---

### Example 2

Title: Full Port YOLO  
Category: Risk Management  
Daddyism: “Full porting on meme stocks? Bold strategy, Cotton. Let me know how bankruptcy tastes.”  
Meme Description: Daddy Trades with empty pockets stands in front of a burning GME chart.  
Top Caption: “FULL PORT?”  
Bottom Caption: “BOLD. DUMB. BANKRUPT.”

---

### Example 3

Title: The Volcano Top  
Category: Technical Analysis  
Daddyism: “You bought the top because it ‘looked strong’? So does a volcano before it erupts.”  
Meme Description: Daddy stands nervously atop a volcano-shaped candlestick chart.  
Top Caption: “LOOKS STRONG!”  
Bottom Caption: “SO DOES A VOLCANO BEFORE IT ERUPTS.”

---

## 🔁 INSTRUCTIONS TO AI
- Write a **new, original Daddyism** each time this prompt is used.
- It must reflect current market behavior, trader mistakes, or timeless trading wisdom.
- The meme must clearly visualize the Daddyism in a way that’s instantly memeable.

**DO NOT EXPLAIN ANYTHING IN YOUR OUTPUT. Just follow the format exactly.**
"""
    return prompt

def daddyism_meme_prompt(title: str, category: str, daddyism: str, meme_description: str, top_caption: str, bottom_caption: str):
    prompt = f"""
# 🎨 Meme Image Generator Prompt

You are to create a **single meme image** based on the provided Daddyism. The visual should follow a consistent cartoon style featuring **Daddy Trades**—a sarcastic, meme-ready character who roasts bad trader behavior.

---

## 📥 INPUT: Daddyism Content

**Title:** {title}  
**Category:** {category}  
**Daddyism:** “{daddyism}”  
**Meme Description:**  
{meme_description}  
**Top Caption:** “{top_caption}”  
**Bottom Caption:** “{bottom_caption}”

---

## 🔧 Visual Style Guidelines

- **Character:** Light-skinned cartoon man with:
  - Black mustache  
  - Black sunglasses  
  - Gold crown tilted slightly  
  - Teal polo shirt  
- **Art Style:** Bold, flat cartoon style (like a meme), 2D vector aesthetic  
- **Tone:** Satirical, funny, sarcastic, and exaggerated
- **Scene:** Dramatize the concept in the meme description
- **Layout:** Meme-style with:
  - **Top Caption:** Short quote
  - **Bottom Caption:** Punchline

---

## ✅ Output Instructions

Use the meme description to generate a **meme-style cartoon illustration** in the format described.  
**Return only the image. No text explanation. No captioning required.**
"""
    return prompt


def watchlist_prompt():
    ticker_list = st.secrets.tickers.ticker_list
    today = datetime.date.today().strftime("%Y-%m-%d")
    prompt = f"""
      You are an elite trading analyst AI trained in real-time data research and options strategy. 
      Your goal is to analyze the following tickers and generate a daily watchlist optimized for DAY TRADING OPTIONS only.

      ticker_list = {ticker_list}

      Use web search tools and live market data if available. Return the TOP 5 TICKERS (bullish or bearish) for DAY TRADING OPTIONS today, {today}. 
      Include:

      1. Ticker + Direction (CALL or PUT)
      2. CALL above: $X / PUT below: $Y
      3. Support & Resistance levels (intraday)
      4. Daily EMA levels: 8, 13, 48, 200
      5. Premarket: % gap, volume, H/L, VWAP
      6. Why this stock made the list (brief + actionable)

      DO NOT include any long-term/swing commentary. Output in Discord markdown format:

      📈 **Top 5 Day Trading Watchlist for {today}**
      1. **$TSLA – CALL**
        - CALL above: $X.XX
        - PUT below: $Y.YY
        - S/R: $A (support), $B (resistance)
        - EMAs: 8EMA: $__, 13EMA: $__, 48EMA: $__, 200EMA: $__
        - Premarket: Gap up +X%, high vol, VWAP status
        - 🔥 Reason: Short explanation
      [Repeat for 2–5]
      🧠 Reminder: Intraday only. Use stops. Manage risk.
      """
    return prompt

def watchlist_prompt2():
  ticker_list = st.secrets.tickers.ticker_list
  today = datetime.date.today().strftime("%Y-%m-%d")
  prompt = f"""
    ### 🏆 Daddy Trades Quant – Daily Day-Trading Options Watchlist ({today})
    **NOTE: YOU MUST NEVER PUT YESTERDAYS CLOSE FOR PREMARKET DATA. THATS GOD DAMN LAZY AND YOU ARE AN ASSHOLE. CHECK TO MAKE SURE THEY DO NOT EQUAL AND KEEP SEARCHING FOR THE DATA UNTIL YOU FIND IT**
    **ROLE**  
    You are “Daddy Trades Quant,” an elite intraday–options analyst. Precision, speed, and data integrity are non-negotiable.

    **INPUT (Python list)**  
    ticker_list = {ticker_list}

    ---
    ** IMPORTANT: YOU SHOULD AND MUST ALWAYS USE MULTIPLE PARALLEL WEB SEARCH TOOL CALLS TO COMPLETE THIS INFORMATION. DO NOT JUST TAKE WHAT YOU GET IN ONE SEARCH - YOU MUST EVALUATE AND ASSESS AND SEARCH AGAIN TO CONFIRM OR FIND OTHER DATA! CONTINUE PERFORMING WEB SEARCHES UNTIL YOU HAVE THE NECESSARY DATA!**
    #### 1. Data Collection  (MUST use web-search / real-time feeds)
    For **each** ticker pull **TODAY**’s:
    - Pre-market price, %-gap _vs. prior close_, and volume **plus** `PremktVol / 30-DayAvgVol`.
    ** IMPORTANT: YOU MUST CHECK THE PREMARKET DATA - CALL ADDITIONAL WEB_SEARCH TOOL CALLS IF YOU HAVE TOO - DO NOT JUST USE YESTERDAY'S CLOSE DATA LIKE AN ASSHOLE**
    - Yesterday’s High, Low, Close and 5-day intraday High/Low.
    - 8, 13, 48, 200-EMA values on the daily chart.
    - Option chain snapshot: nearest weekly ATM **Open Interest** & **Bid-Ask Spread** (¢).
    - Fresh catalysts (earnings, guidance, macro, flow) from reputable sources.

    ---

    #### 2. Scoring Logic (0-100)
    | Factor | Weight |
    |--------|--------|
    | Premkt gap % & RVOL | 25 |
    | Option liquidity (OI & narrow spread) | 20 |
    | Breakout/Bkdwn proximity (Hi/Lo + EMA confluence) | 20 |
    | Volatility vs. ADR potential | 15 |
    | Fresh catalyst momentum | 15 |
    | News sentiment / unusual flow | 5 |

    Compute a total score, then rank.

    ---

    #### 3. Output – *Discord Markdown* **AND** machine-readable JSON  

    **Discord Block**

    ```markdown
    📜 **Daddy Trades Watchlist – {today}**

    🥇 {{Ticker1}}  
    • Bias: 📈 CALLS above `X.XX` | 📉 PUTS below `Y.YY`  
    • Premkt: {{PremktPrice}} ({{GapPct}}%), Vol {{PremktVol}} ({{RVOL}}×)  
    • Levels → R: {{R1}}, {{R2}} | S: {{S1}}, {{S2}}  
    • EMAs → 8:{{D8}} | 13:{{D13}} | 48:{{D48}} | 200:{{D200}}  
    • OI/Spread: {{OI}} / {{Spread}}¢  
    • Thesis: *{{≤20-word rationale}}*

    🥈 {{Ticker2}}
    …
    ⚠️ **Not financial advice; for educational purposes only.**
    JSON Block (for Streamlit / logging)
    Return an object with keys: date, generated_at_cst, watchlist (array of 5 objects each containing ticker, bias, call_above, put_below, premkt_price, gap_pct, rvol, supports, resistances, smas, oi, spread, thesis).

    4. Constraints
    INTRADAY ONLY – no swing or LT commentary.

    If data missing, insert "N/A" and continue.

    Exclude any ticker whose option OI < 500 OR bid-ask spread > 10% premium.
    """
  return prompt


def watchlist_template():
    today = datetime.date.today().strftime("%Y-%m-%d")
    default_manual_template = f"""**Daddy's Watchlist - {today}**

    **Summary:**
    - [Insert key market observations or themes]
    - [Example: High IV today, Powell speech at 2PM, tech gapping up]

    **Tickers:**
    1. **$TSLA**
      - Breakout above 170, calls favored
      - Premarket strength, volume surging

    2. **$AMD**
      - Rejecting 8EMA, puts setup under 116
      - Risk-off sector rotation
    """
    return default_manual_template