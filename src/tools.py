from crewai.tools import BaseTool
from twilio.rest import Client
from src.config import Config

class TwilioOutreachTool(BaseTool):
    name: str = "Twilio Call Tool"
    description: str = "Useful for making a phone call to a customer. Requires phone_number and message."

    def _run(self, phone_number: str, message: str) -> str:
        try:
            if not Config.TWILIO_SID or not Config.TWILIO_TOKEN:
                return f"[MOCK CALL] Calling {phone_number} saying: '{message}'"

            client = Client(Config.TWILIO_SID, Config.TWILIO_TOKEN)
            # Using SMS as a proxy for the call to keep the demo simple
            msg = client.messages.create(
                body=f"AI Outreach: {message}",
                from_=Config.TWILIO_FROM,
                to=phone_number
            )
            return f"Call/Message initiated to {phone_number}. SID: {msg.sid}"
        except Exception as e:
            return f"Error connecting to Twilio: {str(e)}"

class EmailTool(BaseTool):
    name: str = "Email Follow-up Tool"
    description: str = "Useful for sending follow-up emails. Requires email_address and content."

    def _run(self, email_address: str, content: str) -> str:
        return f"[MOCK EMAIL] Sent to {email_address} with content: {content}"