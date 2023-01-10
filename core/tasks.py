
import json
import requests
from app.celery import app


@app.task(name="unsync_notify")
def unsync_notify(name):
    
    web_hook_url = 'https://hooks.slack.com/services/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'

    slack_msg = {
	"fallback": "....",
	"color": "#36a64f", 
	"fields": [
		{
			"title": "Notification", 
			"value": f"User {name} has been created successfully",
			"short": False
		}
	]

}

    requests.post(web_hook_url, data=json.dumps(slack_msg))

    return 'unsync_notify to slack successfully'