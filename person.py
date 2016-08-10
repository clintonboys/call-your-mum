'''
person.py
---------
Contains the class for a person
'''


class Person(object):

    def __init__(self, name, relationship, frequency, birthday, timezone, service):
        self._fullname = name      ## String
        self._name = relationship  ## String (Mum, Dad, Brother)
        self._freq = frequency     ## Float (times per month)
        self._birthday = birthday  ## Date 1980-08-30
        self._timezone = timezone  ## String GMT +10
        self._service = service    ## String iMessage
        
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