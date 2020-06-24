class user():
	 def __init__(self, name, password):
	 	self.name = name 
	 	self.password = password
	 	self.login_attempts = 0
	 	self.repos = 0

	 def update_repos(self):
	 	self.repos +=1

	 def update_login_attempts(self):
	 	self.login_attempts+=1

class Admin(user):
	def __init__(self):
		super().__init__('colin', 'fritz')
		self.priviliges=priviliges()

	


class priviliges():
	def __init__(self):
		self.priviliges=['make_post', 'delete_post', 'delete_reviews']


	def show_privileges(self):
		print(self.priviliges)
		

admin=Admin()
admin.update_login_attempts()
print(admin.login_attempts)
admin.priviliges.show_privileges()


