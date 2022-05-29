from collections import deque

graph_friendlist = {
	'me': ['Benjamin', 'Sandra', 'Melissa', 'Joan', 'Bonnie'],
	'Sandra' : [],
	'Bonnie' : [],
	'Billy': [],
	'Benjamin': ['Joyce', 'Andrew', 'Joan', 'Patricia', 'Julia'],
	'Joyce': [],
	'Andrew': [],
	'Patricia': [],
	'Julia': [],
	'Joan': ['Bobby', 'Shawn', 'Joyce'],
	'Bobby': [],
	'Anna': [],
	'Emily': [],
	'Maria': [],
	'Melissa': ['Anna', 'Mark', 'Emily', 'Maria'],
	'Mark': [],
	'Shawn': ['Billy', 'Sharon', 'Donald'],
	'Sharon': ['Wanda', 'Julia'],
	'Teresa': [],
	'Donald': ['Teresa', 'Arthur'],
	'Arthur': [],
}

goal = ['Billy', 'Wanda']


def search(name):
	search_queue = deque()
	search_queue += graph_friendlist['me']
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person in goal:
				print(person + ' is the closest we\'re looking for.')
				return True
			else:
				search_queue += graph_friendlist[person]
				searched.append(person)
	return False

search('me')


