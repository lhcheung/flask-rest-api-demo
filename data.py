import pickle as pk

arts = [
	{
		"name":"abc"
	},
	{
		"name":"def"
	}

]


with open('data.pkl','wb') as load:
	pk.dump(arts, load)