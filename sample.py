import decorator

@decorator.push_queue
def send_email(subject, to, html):
    msg = Message(subject, recipients=to)
    msg.html = html
    msg.send()


# 1. Run in the background
send_email.delay("Hello", "johndoe@example.com", "Hello, world!")

# 2. Use function normally
send_email("Hello", "johndoe@example.com", "Hello, world!")
