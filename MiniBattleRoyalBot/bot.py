import discord
from discord.ext import commands
import json
import datetime

# Load tickets
with open("tickets.json", "r") as f:
    tickets_data = json.load(f)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.slash_command(name="email", description="Send a professional support email")
async def email(ctx,
                recipient_name: discord.Option(str, "Recipient Name"),
                reply_message: discord.Option(str, "Reply Message")):

    # Generate internal Ticket ID
    ticket_id = f"MBR-{tickets_data['next_ticket']:03d}"
    tickets_data['next_ticket'] += 1

    # Create professional email
    email_body = f"""
Hello {recipient_name},

{reply_message}

—
Mini Battle Royal Support Team
✉️ support@minibattleroyal.help
© 2025 Mini Battle Royal
[Your Logo]
"""

    # TODO: send email via Gmail API here

    # Log internally
    tickets_data['tickets'].append({
        "ticket_id": ticket_id,
        "recipient_name": recipient_name,
        "reply_message": reply_message,
        "timestamp": str(datetime.datetime.now())
    })
    with open("tickets.json", "w") as f:
        json.dump(tickets_data, f, indent=4)

    await ctx.respond(f"Email sent to {recipient_name} (Ticket logged internally).")

bot.run("MTQyMDkyMzUyNjk2MTAzNzM2Mg.G7zur9.WGmMKI9QNtMppdG1Nzz_RAehDYPUsj8qiTT8UYWc")