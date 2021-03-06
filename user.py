''' This library defines classes, methods and attributes for the online bidding user'''

from database import *

DB = DATABASE

class User(Model):
	''' This is the model for the user '''
	username = CharField(max_length = 140, unique = True, primary_key = True)
	email = CharField(max_length = 140, unique = True)
	password = CharField(max_length = 140)
	national_id = CharField(max_length = 140)
	phone_number = IntegerField()
	is_admin = BooleanField(default = False)
	suspended = BooleanField(default = False)
	
	class Meta:
		database = DB
		order_by = ('-username',)
	
	@classmethod
	def create_user(cls, **kwargs):
		try:
			cls.create(**kwargs)
		except IntegrityError:
			raise ValueError('username, email, Nationa ID or phone number already exists')

if __name__ == '__main__':
	DB.connect()
	DB.create_tables([User])
