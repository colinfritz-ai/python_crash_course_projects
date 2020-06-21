import requests 
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

"""
Interactive visualization of the most popular repos on github.  Click thru a bar to the repo.  
"""
# Make an API call and store the response 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
rate_limit = 'https://api.github.com/rate_limit'
r = requests.get(url)
print("Status code:", r.status_code)
response_dict=r.json()
print(response_dict.keys())
total_count=response_dict['total_count']
print('Total repositories: ' + str(total_count))
repo_dicts=response_dict['items']
print('repos returned: ' + str(len(repo_dicts))) 
repo_dict=repo_dicts[0]
print("\n Keys:", len(repo_dict))

names,plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	description = (repo_dict['description'])
	if not description: 
		description = "No description provided"

	plot_dict = {'value': repo_dict['stargazers_count'], 
				'label': description,
				'xlink': repo_dict['html_url'] }

	plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)
my_style.title_font_size=24
my_style.label_font_size=14 
my_style.major_label_font_size = 18 

my_config= pygal.Config()
my_config.x_label_rotation=45 
my_config.show_legend=False
my_config.truncate_label = 15
my_config.show_y_guides = False 
my_config.width = 1000


chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names 

chart.add('', plot_dicts)
chart.render_to_file('Python_repos.svg')


# for key in sorted(repo_dict.keys()):
# 	print(key)

# for repo_dict in repo_dicts:
# 	print('Name:', repo_dict['name'])
# 	print('Owner', repo_dict['owner']['login'])
# 	print('Stars:', repo_dict['stargazers_count'])
# 	print('Repository:', repo_dict['html_url'])
# 	print('Created', repo_dict['created_at'])
# 	print('Updated', repo_dict['updated_at'])
# 	print('Description:', repo_dict['description'])
# 	print("")
# limit=requests.get(rate_limit)
# limit = limit.json()
# print(limit)


