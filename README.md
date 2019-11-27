# Google Cloud Tasks Decorator for Python 3 + Flask
A decorator for Flask + Python 3 that allows a function to run in the background via Google Cloud Tasks.

## Sample
```python3
@decorator.push_queue
def send_email(subject, to, html):
    msg = Message(subject, recipients=to)
    msg.html = html
    msg.send()


# 1. Run in the background
send_email.delay("Hello", "johndoe@example.com", "Hello, world!")

# 2. Use function normally
send_email("Hello", "johndoe@example.com", "Hello, world!")
```

## Note
The code is set to run in the background only when deployed in Google AppEngine environment. Please see `delay()` function in `decorator.py`, particularly line 34 `if os.environ.get('GAE_ENV') == 'standard'`.

When ran locally, it will simply call the function directly.
