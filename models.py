from django.db import models

# TODO(diopib) : handle the timestamp
# TODO(diopib) : handle message types (sms, mms, call)
# TODO(diopib) : handle action = outgoing
# TODO(diopib) : handle action = forward_send
# TODO(diopib) : handle action = amqp_started
# TODO(diopib) : handle event = cancel
# TODO(diopib) : handle event = cancel_all
# TODO(diopib) : handle event = settings

class Request(models.Model):
	"""model describing the connection with envaya server"""

	created_at = models.DateTimeField(auto_now_add = True)

class Response(models.Model):
	"""model describing the connection with envaya server"""


class Rule(models.Model):
	"""different rules to handle request from envaya server"""

	in_request = models.ForeignKey(Request)
	out_response = models.ForeignKey(Response)


# BEG : defining requests ###############################################################

class Incoming(Request):
	"""defining model for an incoming sms"""

	from_number = models.CharField(max_length=15)
	message_content = models.CharField(max_length=1000)


class Message_status(Request):
	"""defining models for send status com"""

	# choices defining the message send status
	SEND_STATUS_CHOICES = (
		('QUEUED', 'queued'),
		('FAILED', 'failed'),
		('CANCEL', 'cancelled'),
		('SENT' , 'sent'),
		)

	mess_id = models.CharField(max_length=100)
	mess_status = models.CharField(max_length=6, choices=SEND_STATUS_CHOICES)
	error = models.CharField(max_length=500)


class Device_status(Request):
	"""defining models for device status com"""

	# choices defining the device status
	DEVICE_STATUS_CHOICES = (
		('POW_CON', 'Power Connected'),
		('POW_DIS', 'Power Disconnected'),
		('BAT_OK', 'Battery OK'),
		('BAT_LOW' , 'Battery Low'),
		('SEND_LIM', 'send Limit Exceeded'),
		)

	dev_status = models.CharField(max_length=8, choices=DEVICE_STATUS_CHOICES)

# END : defining requests ###############################################################

# BEG : defining responses ##############################################################

class Send(Response):
	"""model for sending message com"""

	to_number = models.CharField(max_length=15)
	message_content = models.CharField(max_length=160)

class Log(Response):
	"""models for printing a log message in envaya server"""

	log_message = models.CharField(max_length=100)

class Error(Response):
	"""semding an error message to be displayed in envaya"""

	error_message = models.CharField(max_length=100)

# END : defining responses ##############################################################