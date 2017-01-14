import datetime
import json

'''
person.py
---------
Contains the class for a person
'''

def load_people(filename):
    with open(filename) as data_file:    
        people = json.load(data_file)
    people_list = []
    for person in people[u'people']:
        people_list.append(Person(person[u'name'], person[u'relationship'],
                                  person[u'frequency'], person[u'birthday'],
                                  person[u'timezone'], person[u'service'],
                                  person[u'last_contact']))
    return people_list

def save_people(people_list, filename):
    to_json = {"people":[]}
    for person in people_list:
        to_json["people"].append({"name":person._fullname,
                        "frequency": person._freq,
                        "relationship":person._name,
                        "birthday":datetime.datetime.strftime(person._birthday, "%Y-%m-%d"),
                        "timezone":person._timezone,
                        "service":person._service,
                        "last_contact":datetime.datetime.strftime(person.last_contact(),"%Y-%m-%d")})
    with open(filename,'w') as data_file:
        json.dump(to_json, data_file)

class Person(object):

    def __init__(self, name, relationship, frequency, birthday, timezone, service, last_contact, is_contacted = False):
        self._fullname = name      ## String
        self._name = relationship  ## String (Mum, Dad, Brother)
        self._freq = frequency     ## Float (times per month)
        self._birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d") ## Date 1980-08-30
        self._timezone = timezone  ## String GMT +10
        self._service = service    ## String iMessage
        self._is_contacted = is_contacted
        self._last_contact = datetime.datetime.strptime(last_contact, "%Y-%m-%d")

    @property
    def fullname(self):
        return self._fullname

    def name(self):
        return self._name

    def freq(self):
        return self._freq

    def birthday(self):
        return self._birthday

    def timezone(self):
    	return self._timezone

    def service(self):
    	return self._service

    def is_contacted(self):
        return self._is_contacted

    def birthday(self):
        return datetime.datetime.strftime(self.birthday, "%Y-%m-%d")

    def is_birthday(self):
        current_date = datetime.datetime.utcnow()
        if current_date.month == self._birthday.month and current_date.day == self._birthday.day:
            return True
        else:
            return False

    def last_contact(self):
        return self._last_contact

