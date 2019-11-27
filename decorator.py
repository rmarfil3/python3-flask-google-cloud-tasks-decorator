class PushQueue:
    def __init__(self, f):
        self.f = f

        # Create a flask endpoint for this task
        app.add_url_rule(
            f"/tasks/{self.f.__name__}",
            methods=["POST"],
            view_func=self.push_queue_handler,
            endpoint=f"task_{self.f.__name__}")

    def __call__(self, *args, **kwargs):
        self.f(*args, **kwargs)
        
    def push_queue_handler(self):
        """The Flask handler that will receive the request made by Google Cloud Tasks"""

        # Validate request: should come from Cloud Tasks
        if request.headers.get('X-Cloudtasks-Taskname') is None:
            raise Exception('Invalid Task, No X-Cloudtasks-Taskname request header found')

        request_data = request.get_data()
        request_data = request_data.decode()
        request_data = json.loads(request_data)

        self.f(*request_data["args"], **request_data["kwargs"])
        return "", 200

    def delay(self, *args, **kwargs):
        """
        Live: Creates a push queue in Google Cloud Tasks using the endpoint above
        Local: Does not do background task, just calls the function directly
        """
        if os.environ.get('GAE_ENV') == 'standard':
            payload = {
                "args": args,
                "kwargs": kwargs
            }
            encoded_payload = json.dumps(payload).encode()

            task = {
                "http_request": {
                    "http_method": "POST",
                    "url": f"{request.host_url}tasks/{self.f.__name__}",
                    "body": encoded_payload
                }
            }

            response = cloud_task_client.create_task(cloud_task_parent, task)
            app.logger.info("Created task {}".format(response.name))
            return response

        else:
            self.f(*args, **kwargs)


def push_queue(f):
    """Decorator for converting functions to push queues
    :type f: function
    :rtype: PushQueue
    """
    push_queue_object = PushQueue(f)
    return push_queue_object
