# Google Cloud Tasks Decorator for Google AppEngine Python 3 + Flask
A decorator for Flask + Python 3 which can be used to wrap a function and make it run in the background when called by sending it to Google Cloud Tasks

## Sample
```python3
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
```

## Note
The code is set to run in the background only when deployed in Google AppEngine environment. Please see `delay()` function in `decorator.py`, particularly line 34 `if os.environ.get('GAE_ENV') == 'standard'`.

If ran locally, it will simply call the function directly.
