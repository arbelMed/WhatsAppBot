from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    media_url = request.values.get('MediaUrl0', '')
    response = MessagingResponse()
    msg = response.message()

    if media_url:
        msg.body("📷 תודה על התמונה! נבדוק אותה וניתן לך המלצה בקרוב 💬")
        return str(response)

    if 'שפתיים' in incoming_msg or '1' == incoming_msg:
        msg.body("👄 נראה שטיפול פיסול שפתיים יכול להתאים לך. רוצה פרטים נוספים?")
    elif 'אף' in incoming_msg or '2' == incoming_msg:
        msg.body("👃 פיסול אף ללא ניתוח נשמע מתאים למה שתיארת. תרצי שנשלח עוד מידע?")
    elif 'קמטים' in incoming_msg or '3' == incoming_msg:
        msg.body("😊 יש לנו טיפולים בקמטים עם חומרי מילוי או לייזר. מעוניינת לדעת מה הכי יתאים לך?")
    elif 'צלקות' in incoming_msg or '4' == incoming_msg:
        msg.body("✨ טיפול בלייזר לצלקות בפנים יכול לעזור מאוד. רוצה שנזמין אותך לייעוץ?")
    elif '5' == incoming_msg or 'לא בטוחה' in incoming_msg:
        msg.body("אין בעיה! שלחי לנו תמונה 📷 או ספרי לנו מה הכי מפריע לך – ונתאים טיפול אישי.")
    elif '6' == incoming_msg or 'תמונה' in incoming_msg:
        msg.body("📷 תוכלי לשלוח תמונה של האזור שמפריע לך – ואנחנו נאבחן וניתן המלצה תוך זמן קצר.")
    else:
        msg.body("היי! ✨ ברוכה הבאה לייעוץ האסתטי של Arbel Medical. כתבי מספר או שם תחום לבחירה:\n1️⃣ שפתיים\n2️⃣ אף\n3️⃣ קמטים\n4️⃣ צלקות\n5️⃣ לא בטוחה\n6️⃣ שליחת תמונה")

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
