import gradio as gr
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from huggingface_hub import InferenceClient
import json
import datetime
import csv
import os

# Load dataset
df = pd.read_csv("data/vendors_final.csv")

# Prepare text for recommender
df["text"] = (
    df["name"].fillna("") + " " +
    df["category"].fillna("") + " " +
    df["location"].fillna("") + " " +
    df["services"].fillna("")
)

# TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(df["text"])

# Booking database file
BOOKINGS_FILE = "bookings.csv"

def init_bookings_file():
    """Initialize bookings CSV if it doesn't exist"""
    if not os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Event Type', 'Guest Count', 'Budget', 'Location', 'Email', 'Description', 'Status'])

def save_booking(event_type, guest_count, budget_level, location, email, description):
    """Save booking to CSV"""
    init_bookings_file()
    with open(BOOKINGS_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            event_type,
            guest_count,
            budget_level,
            location,
            email,
            description,
            "Pending"
        ])
    return True

def recommend_vendors(query, top_n=5):
    query_vec = vectorizer.transform([query])
    sims = cosine_similarity(query_vec, X)[0]
    top_idx = sims.argsort()[-top_n:][::-1]
    return df.iloc[top_idx][["name", "category", "location", "services"]]

# HuggingFace client
client = InferenceClient(
    model="microsoft/Phi-3-mini-4k-instruct",
    token="hf_YOUR_HF_TOKEN_HERE"  # Replace with your actual HuggingFace token
)

def estimate_budget(event_type, guest_count, budget_level):
    """Smart budget estimation"""
    base_costs = {
        "wedding": 150,
        "birthday": 50,
        "corporate": 100,
        "conference": 200,
        "graduation": 75,
        "other": 80
    }
    
    multiplier = {"budget": 0.8, "standard": 1.0, "luxury": 1.8}
    
    base = base_costs.get(event_type.lower(), 80)
    per_guest = base * multiplier.get(budget_level.lower(), 1.0)
    total = per_guest * guest_count
    
    return {
        "per_guest": f"${per_guest:.2f}",
        "total_estimate": f"${total:.2f}",
        "breakdown": {
            "Venue/Catering": f"${total * 0.55:.2f}",
            "Decorations": f"${total * 0.15:.2f}",
            "Entertainment": f"${total * 0.15:.2f}",
            "Misc/Contingency": f"${total * 0.15:.2f}"
        }
    }

def generate_smart_plan(event_description, event_type, guest_count, budget_level, location):
    """Enhanced event planning with smart recommendations"""
    
    smart_query = f"{event_type} {location} {guest_count} guests {budget_level} {event_description}"
    vendors = recommend_vendors(smart_query, 5)
    budget = estimate_budget(event_type, int(guest_count) if guest_count else 50, budget_level)
    
    vendors_text = "\n".join(
        f"• {row['name']} ({row['category']}) - {row['location']}"
        for _, row in vendors.iterrows()
    )

    prompt = f"""
You are EventEcho, a professional event planner with 20+ years of experience.

EVENT DETAILS:
- Type: {event_type}
- Guest Count: {guest_count}
- Budget Level: {budget_level}
- Location: {location}
- Special Request: {event_description}

RECOMMENDED VENDORS:
{vendors_text}

Create a CREATIVE and DETAILED event plan with:
1. Event Concept & Theme
2. Detailed Timeline
3. Vendor Coordination Strategy
4. Creative Decorations Ideas
5. Guest Experience Flow
6. Contingency Plans

Be inspiring and actionable!
"""

    try:
        response = client.text_generation(prompt, max_new_tokens=500, temperature=0.7)
        event_plan = response
    except:
        event_plan = f"""🎉 CREATIVE EVENT PLAN FOR YOUR {event_type.upper()}

TOP VENDORS:
{vendors_text}

BUDGET BREAKDOWN:
{json.dumps(budget['breakdown'], indent=2)}

TIMELINE:
• 8 weeks: Secure venue and caterer
• 4 weeks: Confirm vendors and guest list
• 2 weeks: Final planning
• Day before: Setup
• Day of: 2 hours early
"""
    
    return {
        "plan": event_plan,
        "budget": budget,
        "vendors": vendors_text
    }

# Gradio UI
with gr.Blocks(theme=gr.themes.Soft(primary_hue="orange")) as demo:
    
    gr.Markdown("# 🎉 EventEcho – AI Event Planner Pro")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📋 Event Details")
            event_type = gr.Dropdown(["Wedding", "Birthday", "Corporate", "Conference", "Graduation", "Other"], label="Event Type", value="Wedding")
            guest_count = gr.Number(label="Expected Guests", value=50, minimum=1, maximum=10000)
            budget_level = gr.Dropdown(["Budget", "Standard", "Luxury"], label="Budget Level", value="Standard")
            location = gr.Textbox(label="Location/City", value="City Center")
            event_description = gr.Textbox(label="Special Requests/Theme", lines=4, value="Intimate and elegant celebration")
            submit_btn = gr.Button("✨ Generate Smart Plan", variant="primary")
        
        with gr.Column(scale=1.2):
            with gr.Tabs():
                with gr.TabItem("🎯 Event Plan"):
                    plan_output = gr.Textbox(label="Creative Event Plan", lines=18, interactive=False)
                
                with gr.TabItem("💰 Budget"):
                    budget_output = gr.JSON(label="Budget Breakdown")
                
                with gr.TabItem("🏢 Vendors"):
                    vendors_output = gr.Textbox(label="Recommended Vendors", lines=15, interactive=False)
                
                with gr.TabItem("📅 Booking"):
                    gr.Markdown("### 🔖 Flag & Book Your Event")
                    booking_email = gr.Textbox(label="Your Email", type="email")
                    booking_notes = gr.Textbox(label="Additional Notes", lines=3)
                    booking_btn = gr.Button("🚀 Flag for Booking", variant="primary")
                    booking_status = gr.Textbox(label="Status", interactive=False)
    
    def process_event(event_type, guest_count, budget_level, location, event_description):
        result = generate_smart_plan(event_description, event_type, guest_count, budget_level, location)
        return result["plan"], result["budget"], result["vendors"]
    
    def process_booking(event_type, guest_count, budget_level, location, event_description, booking_email, booking_notes):
        if not booking_email or "@" not in booking_email:
            return "❌ Please enter a valid email address"
        try:
            save_booking(event_type, guest_count, budget_level, location, booking_email, event_description)
            return f"""✅ SUCCESS! Your event has been flagged for booking.

📧 Email: {booking_email}
📋 Event: {event_type}
👥 Guests: {int(guest_count)}
💰 Budget: {budget_level}
📍 Location: {location}

Our team will contact you within 24 hours!"""
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    submit_btn.click(fn=process_event, inputs=[event_type, guest_count, budget_level, location, event_description], outputs=[plan_output, budget_output, vendors_output])
    booking_btn.click(fn=process_booking, inputs=[event_type, guest_count, budget_level, location, event_description, booking_email, booking_notes], outputs=[booking_status])

if __name__ == "__main__":
    demo.launch(share=True)
