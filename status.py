import time
import requests
import subprocess
import os, datetime

# Discord Webhook URL
webhook_url = "https://discord.com/api/webhooks/1171221013585997835/KgOlISz-EkXsPuJoF6yZIzvLoJPlRdjZMHmFi5E3i3lYao_P3eX51fRMaBJ9VciydbTY"

# Function to send a message to Discord
def send_discord_message(message):
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print(f"Message sent to Discord: {message}")
    else:
        print(f"Failed to send message to Discord: {response.status_code}")

# send_discord_message("rerun: message should now only be sent once every 10 minutes")

# Main loop
while True:
    current_time = time.time()
    # Check if the current Unix time is divisible by 60
    if int(current_time) % 600 == 0:
        # Send the message
        send_discord_message(f"status: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        # Refresh the Git repository
        # os.chdir("/path/to/your/git/repo")  # Change to the directory of your Git repository
        subprocess.run(["git", "pull"])
        # Rerun the script
        subprocess.run(["python", "status.py"])  # Replace with your script's filename
    # time.sleep(60)  # Sleep for 60 seconds before checking again