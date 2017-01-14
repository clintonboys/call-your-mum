from person import Person, load_people, save_people
from config import *
import time
import datetime
import json
import numpy as np
import sendgrid
from copy import email_copy
import random
from sendgrid.helpers.mail import *


def send_message(timestamp, person, birthday = False):
	sg = sendgrid.SendGridAPIClient(apikey = sendgrid_key)
	if birthday:
		birthday_message = "; it'\s their birthday!"
	else:
		birthday_message = ""
	data = { "personalizations": [
	    {
	      "to": [
	        {
	          "email": "cdsboys@gmail.com"
	        }
	      ],
	      "subject": "Get in touch with {0}".format(person._name) + birthday_message
	    }
	  ],
	  "from": {
	    "email": "cdsboys@gmail.com",
	  },
	  "content": [
	    {
	      "type": "text/plain",
	      "value": random.choice(email_copy).format(person._name, person._service)
	    }
	  ]
	}

	response = sg.client.mail.send.post(request_body = data)

	print(response.status_code)
	print(response.body)
	print(response.headers)


def main():
	people_list = load_people('people.json')

	current_time = datetime.datetime.utcnow()
	hour = current_time.hour
	hour_local = hour + local_time

	if hour_local >= min_contact_hour and hour_local <= max_contact_hour:

		for person in people_list:
			X = np.random.uniform(0,30*24*(60/service_frequency)/person.freq())
			if X <= 1:
				person._is_contacted = True

		for person in people_list:
			if person._is_contacted == True and (current_time - person.last_contact()).days > 0:
				person_hour_local = (hour + person.timezone())%24
				if person_hour_local >= min_contact_hour and person_hour_local <= max_contact_hour:
					send_message(current_time, person)
					person._last_contact = current_time
			elif person.is_birthday() and (current_time - person.last_contact()).days > 0:
				send_message(current_time, person, True)
				person._last_contact = current_time

	save_people(people_list, 'people.json')

if __name__ == '__main__':
	main()