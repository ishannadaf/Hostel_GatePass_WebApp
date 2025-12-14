import requests
import os
import logging

# Optional: log SMS errors
logger = logging.getLogger(__name__)

def send_sms(mobile_number, name1, name2):
    """
    Sends SMS using custom SMS API
    """

    try:
        # ===== YOUR SMS API DETAILS =====
        SMS_API_URL = f"http://vas.mobilogi.com/api.php?username=ISHAAN&password=pass1234&route=1&sender=STIPLS&mobile[]={mobile_number}&message[]=Please%20check%20routine%20of%20{name1}%20{name2},%20he%20left%20the%20campus%20for%201%20hour.%20Kindly%20do%20needful.%20STIPLS&templateid=1007937732269442138"
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(
            SMS_API_URL,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            return True
        else:
            logger.error(f"SMS Failed: {response.text}")
            return False

    except Exception as e:
        logger.error(f"SMS Exception: {str(e)}")
        return False
