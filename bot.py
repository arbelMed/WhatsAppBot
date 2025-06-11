# WhatsApp Aesthetic Consultation Bot (Python - using Flask & WATI API)
# Make sure you have Flask installed and a WATI API token.

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WATI_API_URL = "https://app-server.wati.io/api/v1/sendSessionMessage"
WATI_ACCESS_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJmNTg5Yzc3Ny1kY2RiLTQyYTMtOTEwYS04ODNkOTE0ODhiMzIiLCJ1bmlxdWVfbmFtZSI6ImFyYmVsLm1lZGljYWwxQGdtYWlsLmNvbSIsIm5hbWVpZCI6ImFyYmVsLm1lZGljYWwxQGdtYWlsLmNvbSIsImVtYWlsIjoiYXJiZWwubWVkaWNhbDFAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDYvMTEvMjAyNSAxODozODoxOSIsImRiX25hbWUiOiJ3YXRpX2FwcF90cmlhbCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlRSSUFMIiwiZXhwIjoxNzUwMjkxMjAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.eEMDvWz_tzsHU0KowjhxlACOMaPJKqaMjhm-aAfz9vY"  # Example: Bearer eyJhbGciOi...


def send_message(phone, message):
    headers = {
        "Authorization": WATI_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "phone": phone,
        "message": message
    }
    response = requests.post(WATI_API_URL, headers=headers, json=payload)
    return response.status_code, response.text


@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.json.get('message', '').strip().lower()
    phone_number = request.json.get('phone')
    media_url = request.json.get('media', '')

    if not phone_number:
        return jsonify({"error": "Missing phone number"}), 400

    # Handle image
    if media_url:
        send_message(phone_number, "📷 תודה על התמונה! נבדוק אותה וניתן לך המלצה בקרוב 💬")
        return jsonify({"status": "image received"})

    # Handle text responses
    if 'שפתיים' in incoming_msg or '1' == incoming_msg:
        text = "👄 נראה שטיפול פיסול שפתיים יכול להתאים לך. רוצה פרטים נוספים?"
    elif 'אף' in incoming_msg or '2' == incoming_msg:
        text = "👃 פיסול אף ללא ניתוח נשמע מתאים למה שתיארת. תרצי שנשלח עוד מידע?"
    elif 'קמטים' in incoming_msg or '3' == incoming_msg:
        text = "😊 יש לנו טיפולים בקמטים עם חומרי מילוי או לייזר. מעוניינת לדעת מה הכי יתאים לך?"
    elif 'צלקות' in incoming_msg or '4' == incoming_msg:
        text = "✨ טיפול בלייזר לצלקות בפנים יכול לעזור מאוד. רוצה שנזמין אותך לייעוץ?"
    elif '5' == incoming_msg or 'לא בטוחה' in incoming_msg:
        text = "אין בעיה! שלחי לנו תמונה 📷 או ספרי לנו מה הכי מפריע לך – ונתאים טיפול אישי."
    elif '6' == incoming_msg or 'תמונה' in incoming_msg:
        text = "📷 תוכלי לשלוח תמונה של האזור שמפריע לך – ואנחנו נאבחן וניתן המלצה תוך זמן קצר."
    else:
        text = "היי! ✨ ברוכה הבאה לייעוץ האסתטי של Arbel Medical. כתבי מספר או שם תחום לבחירה:\n1️⃣ שפתיים\n2️⃣ אף\n3️⃣ קמטים\n4️⃣ צלקות\n5️⃣ לא בטוחה\n6️⃣ שליחת תמונה"

    status_code, response_text = send_message(phone_number, text)
    return jsonify({"status_code": status_code, "response": response_text})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
