import streamlit as st

def daddyism_prompt():
    prompt = """
# 🧠 Daddyism + Meme Generator Prompt

You are to create hilarious, insightful, and visually driven content for a fictional character named **Daddy Trades** — a sarcastic, brutally honest, seasoned trader-dad who delivers one-liner truths about day trading, risk, and market behavior. His voice is like Randy Marsh meets a financial mentor: sarcastic, savage, and secretly wise.

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