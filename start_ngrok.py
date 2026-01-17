from pyngrok import ngrok
import time

# Set ngrok auth token (you can get a free one from https://dashboard.ngrok.com)
# ngrok.set_auth_token("YOUR_AUTH_TOKEN")

# Start ngrok tunnel to local Gradio app
public_url = ngrok.connect(7860)
print(f"\n{'='*60}")
print(f"🌍 PUBLIC NGROK LINK:")
print(f"{public_url}")
print(f"{'='*60}\n")

# Keep the tunnel alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Closing ngrok tunnel...")
    ngrok.disconnect(public_url)
