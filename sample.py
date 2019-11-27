import decorator

@decorator.push_queue
def send_email(subject, to, html):
    with app.app_context():
        msg = Message(subject, recipients=to)
        msg.html = html
        mail.send(msg)


# 1. Run in the background
send_email.delay("Hello", "johndoe@example.com", "Hello, world!")

# 2. Use function normally
send_email("Hello", "johndoe@example.com", "Hello, world!")
