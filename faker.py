import json, random

datas = '''[
	{
	  "id": 1,
	  "title": "Lorem Ipsum Dolor Sit Amet",
	  "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac interdum lacus.",
	  "author": {
		"id": 1,
		"pseudo": "john_doe",
		"email": "john.doe@example.com",
		"avatar": "https://example.com/avatar/john_doe.jpg"
	  },
	  "updatedAt": "2023-01-01T12:30:45Z",
	  "createdAt": "2023-01-01T12:30:45Z"
	},
	{
	  "id": 2,
	  "title": "Aenean Condimentum Eros In Consectetur",
	  "body": "Aenean condimentum eros in consectetur venenatis. Nullam vel nunc ac turpis consequat fringilla.",
	  "author": {
		"id": 2,
		"pseudo": "alice_smith",
		"email": "alice.smith@example.com",
		"avatar": "https://example.com/avatar/alice_smith.jpg"
	  },
	  "updatedAt": "2023-01-02T08:15:30Z",
	  "createdAt": "2023-01-02T08:15:30Z"
	},
	{
		"id": 3,
		"title": "Suspendisse Euismod Egestas Ornare",
		"body": "Suspendisse euismod egestas ornare. In in ligula eu arcu aliquet tincidunt nec a enim.",
		"author": {
		  "id": 3,
		  "pseudo": "mike_jones",
		  "email": "mike.jones@example.com",
		  "avatar": "https://example.com/avatar/mike_jones.jpg"
		},
		"updatedAt": "2023-01-03T16:45:22Z",
		"createdAt": "2023-01-03T16:45:22Z"
	  },
	  {
		"id": 4,
		"title": "Vivamus Feugiat Nunc Sit Amet",
		"body": "Vivamus feugiat nunc sit amet elit facilisis, vitae lacinia justo gravida. Nullam efficitur justo eget ligula sagittis fermentum.",
		"author": {
		  "id": 4,
		  "pseudo": "sara_brown",
		  "email": "sara.brown@example.com",
		  "avatar": "https://example.com/avatar/sara_brown.jpg"
		},
		"updatedAt": "2023-01-04T09:12:57Z",
		"createdAt": "2023-01-04T09:12:57Z"
	  },
	  {
		"id": 5,
		"title": "Duis Diam Mauris, Ultricies Inceptos",
		"body": "Duis diam mauris, ultricies inceptos adipiscing vel, tristique nec libero. Fusce fringilla pharetra velit, vel luctus nulla vestibulum nec.",
		"author": {
		  "id": 5,
		  "pseudo": "alex_wilson",
		  "email": "alex.wilson@example.com",
		  "avatar": "https://example.com/avatar/alex_wilson.jpg"
		},
		"updatedAt": "2023-01-05T14:28:40Z",
		"createdAt": "2023-01-05T14:28:40Z"
	  },
	  {
		"id": 6,
		"title": "Pellentesque Mattis Risus At Tellus",
		"body": "Pellentesque mattis risus at tellus feugiat vestibulum. Proin eget hendrerit sem, vitae gravida dui.",
		"author": {
		  "id": 6,
		  "pseudo": "emily_martin",
		  "email": "emily.martin@example.com",
		  "avatar": "https://example.com/avatar/emily_martin.jpg"
		},
		"updatedAt": "2023-01-06T18:09:15Z",
		"createdAt": "2023-01-06T18:09:15Z"
	  },
	  {
		"id": 7,
		"title": "Nullam Eu Sagittis Elit",
		"body": "Nullam eu sagittis elit. Duis tincidunt ultrices felis, nec cursus leo hendrerit id. Quisque nec imperdiet dui.",
		"author": {
		  "id": 7,
		  "pseudo": "peter_clark",
		  "email": "peter.clark@example.com",
		  "avatar": "https://example.com/avatar/peter_clark.jpg"
		},
		"updatedAt": "2023-01-07T11:55:28Z",
		"createdAt": "2023-01-07T11:55:28Z"
	  },
	  {
		"id": 8,
		"title": "In Ut Semper Mollis",
		"body": "In ut semper mollis. Suspendisse potenti. Vestibulum congue augue vel mauris faucibus, at hendrerit lectus pulvinar.",
		"author": {
		  "id": 8,
		  "pseudo": "laura_jackson",
		  "email": "laura.jackson@example.com",
		  "avatar": "https://example.com/avatar/laura_jackson.jpg"
		},
		"updatedAt": "2023-01-08T07:36:44Z",
		"createdAt": "2023-01-08T07:36:44Z"
	  },
	  {
		"id": 9,
		"title": "Aliquam Erat Volutpat",
		"body": "Aliquam erat volutpat. Curabitur a tortor ut neque cursus rhoncus. Sed ut vestibulum odio.",
		"author": {
		  "id": 9,
		  "pseudo": "kevin_adams",
		  "email": "kevin.adams@example.com",
		  "avatar": "https://example.com/avatar/kevin_adams.jpg"
		},
		"updatedAt": "2023-01-09T15:20:12Z",
		"createdAt": "2023-01-09T15:20:12Z"
	  },
	  {
		"id": 10,
		"title": "Ut Et Eros Euismod",
		"body": "Ut et eros euismod, suscipit odio vel, fermentum odio. Vestibulum ut efficitur elit.",
		"author": {
		  "id": 10,
		  "pseudo": "natalie_white",
		  "email": "natalie.white@example.com",
		  "avatar": "https://example.com/avatar/natalie_white.jpg"
		},
		"updatedAt": "2023-01-10T09:45:37Z",
		"createdAt": "2023-01-10T09:45:37Z"
	  },
	  {
		"id": 11,
		"title": "Fusce Ac Eros Velit",
		"body": "Fusce ac eros velit. Integer vel congue justo. Proin ut ligula quis risus varius venenatis.",
		"author": {
		  "id": 11,
		  "pseudo": "olivia_morris",
		  "email": "olivia.morris@example.com",
		  "avatar": "https://example.com/avatar/olivia_morris.jpg"
		},
		"updatedAt": "2023-01-11T14:55:22Z",
		"createdAt": "2023-01-11T14:55:22Z"
	  },
	  {
		"id": 12,
		"title": "Phasellus Feugiat Sapien Odio",
		"body": "Phasellus feugiat sapien odio, in tristique turpis imperdiet vel. Nunc nec urna vel elit faucibus consequat.",
		"author": {
		  "id": 12,
		  "pseudo": "daniel_brown",
		  "email": "daniel.brown@example.com",
		  "avatar": "https://example.com/avatar/daniel_brown.jpg"
		},
		"updatedAt": "2023-01-12T08:10:45Z",
		"createdAt": "2023-01-12T08:10:45Z"
	  },
	  {
		"id": 13,
		"title": "Vestibulum Bibendum Consectetur",
		"body": "Vestibulum bibendum consectetur velit, eget tristique arcu fermentum vitae. Suspendisse potenti. Nam non facilisis libero.",
		"author": {
		  "id": 13,
		  "pseudo": "william_carter",
		  "email": "william.carter@example.com",
		  "avatar": "https://example.com/avatar/william_carter.jpg"
		},
		"updatedAt": "2023-01-13T16:30:18Z",
		"createdAt": "2023-01-13T16:30:18Z"
	  },
	  {
		"id": 14,
		"title": "Cras Eleifend Tristique Nisi",
		"body": "Cras eleifend tristique nisi, vel vehicula augue tristique at. Aenean in lectus non tortor iaculis fermentum.",
		"author": {
		  "id": 14,
		  "pseudo": "emma_smith",
		  "email": "emma.smith@example.com",
		  "avatar": "https://example.com/avatar/emma_smith.jpg"
		},
		"updatedAt": "2023-01-14T10:05:33Z",
		"createdAt": "2023-01-14T10:05:33Z"
	  },
	  {
		"id": 15,
		"title": "Pellentesque Laoreet Justo Ut",
		"body": "Pellentesque laoreet justo ut velit luctus, vel suscipit tortor vestibulum. Sed tincidunt neque vel malesuada vulputate.",
		"author": {
		  "id": 15,
		  "pseudo": "megan_jones",
		  "email": "megan.jones@example.com",
		  "avatar": "https://example.com/avatar/megan_jones.jpg"
		},
		"updatedAt": "2023-01-15T14:20:47Z",
		"createdAt": "2023-01-15T14:20:47Z"
	  },
	  {
		"id": 16,
		"title": "Vivamus Tristique Neque Velit",
		"body": "Vivamus tristique neque velit, et dignissim justo eleifend vel. Nam ullamcorper justo ac leo convallis, vel pharetra quam fringilla.",
		"author": {
		  "id": 16,
		  "pseudo": "nathan_wilson",
		  "email": "nathan.wilson@example.com",
		  "avatar": "https://example.com/avatar/nathan_wilson.jpg"
		},
		"updatedAt": "2023-01-16T08:45:12Z",
		"createdAt": "2023-01-16T08:45:12Z"
	  },
	  {
		"id": 17,
		"title": "Integer Nec Magna Non",
		"body": "Integer nec magna non mi consectetur sagittis. Duis vel ipsum nec turpis lacinia sollicitudin.",
		"author": {
		  "id": 17,
		  "pseudo": "grace_anderson",
		  "email": "grace.anderson@example.com",
		  "avatar": "https://example.com/avatar/grace_anderson.jpg"
		},
		"updatedAt": "2023-01-17T12:10:35Z",
		"createdAt": "2023-01-17T12:10:35Z"
	  },
	  {
		"id": 18,
		"title": "Cras Mattis Eros Euismod Nulla",
		"body": "Cras mattis eros euismod nulla pellentesque, eu consectetur libero aliquet. Sed fringilla, tortor at mattis tincidunt, est lacus congue ligula.",
		"author": {
		  "id": 18,
		  "pseudo": "ryan_campbell",
		  "email": "ryan.campbell@example.com",
		  "avatar": "https://example.com/avatar/ryan_campbell.jpg"
		},
		"updatedAt": "2023-01-18T18:55:20Z",
		"createdAt": "2023-01-18T18:55:20Z"
	  },
	  {
		"id": 19,
		"title": "Sed Dignissim Justo Ac",
		"body": "Sed dignissim justo ac tortor congue, eu aliquet mauris aliquam. Vivamus consectetur scelerisque leo, et dapibus odio tempus a.",
		"author": {
		  "id": 19,
		  "pseudo": "hannah_martin",
		  "email": "hannah.martin@example.com",
		  "avatar": "https://example.com/avatar/hannah_martin.jpg"
		},
		"updatedAt": "2023-01-19T09:30:44Z",
		"createdAt": "2023-01-19T09:30:44Z"
	  },
	  {
		"id": 20,
		"title": "Maecenas Posuere Magna Nec",
		"body": "Maecenas posuere magna nec felis vestibulum fermentum. Ut vel purus ut purus sollicitudin dignissim.",
		"author": {
		  "id": 20,
		  "pseudo": "owen_jackson",
		  "email": "owen.jackson@example.com",
		  "avatar": "https://example.com/avatar/owen_jackson.jpg"
		},
		"updatedAt": "2023-01-20T14:15:28Z",
		"createdAt": "2023-01-20T14:15:28Z"
	  }
  ]'''

l = json.loads(datas)

def pick():
	return random.choice(l)

r = []
def generate(n = 50):	
	for i in range(n):
		picked = pick()
		author_details = picked.get('author', {})  # Ensure 'author' is available in picked data
		picked = {
			**picked,
			'id': i+1,
			'author': {
				'id': i+1,
				'pseudo': author_details.get('pseudo', ''),
				'email': author_details.get('email', ''),
				'avatar': random.choice(['/images/avatar-man.jpg', '/images/avatar-woman.jpg'])
			}
		}
		r.append(picked)	
	return r

results = generate(501)

for result in results:
	print(result, '\n')

# Save the results into a JSON file
with open('fake-posts.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)