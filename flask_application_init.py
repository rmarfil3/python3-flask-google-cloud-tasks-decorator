# Add this to your Flask application's init file

from google.cloud import tasks_v2


project=os.environ.get('GOOGLE_CLOUD_PROJECT')  # my-appengine-project
location=os.environ.get('CLOUD_TASK_LOCATION')  # us-central1
queue=os.environ.get('CLOUD_TASK_QUEUE')  # default

cloud_task_client = None
cloud_task_parent = None
if os.environ.get('GAE_ENV') == 'standard':
    cloud_task_client = tasks_v2.CloudTasksClient()
    cloud_task_parent = cloud_task_client.queue_path(project, location, queue)
