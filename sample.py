import decorator

@decorator.push_queue
def send_email(subject, to, html):
    with app.app_context():
        msg = Message(subject, recipients=to)
        msg.html = html
        mail.send(msg)
