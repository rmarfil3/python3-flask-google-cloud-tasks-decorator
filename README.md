# Google Cloud Tasks Decorator for Python 3 + Flask
A decorator for Python 3 + Flask that allows a function to run in the background via Google Cloud Tasks.


## Usage
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


## Requirements
```
google-cloud-tasks==1.3.0
```

## Setup
Add this to your Flask application's init file
```python3
from google.cloud import tasks_v2

project=os.environ.get('GOOGLE_CLOUD_PROJECT')  # my-appengine-project
location=os.environ.get('CLOUD_TASK_LOCATION')  # us-central1
queue=os.environ.get('CLOUD_TASK_QUEUE')  # default

cloud_task_client = None
cloud_task_parent = None
if os.environ.get('GAE_ENV') == 'standard':
    cloud_task_client = tasks_v2.CloudTasksClient()
    cloud_task_parent = cloud_task_client.queue_path(project, location, queue)
```


## Notes
The code is set to run in the background only when deployed in Google AppEngine environment. Please see `delay()` function in `decorator.py`, particularly line 34 `if os.environ.get('GAE_ENV') == 'standard'`.

If code is unmodified and ran outside Google AppEngine environment, `.delay()` will simply call the function directly.
