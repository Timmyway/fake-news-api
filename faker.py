import json, random
import uuid

fake_users = '''[
    {
      "_id": "6dc07fba-5a7f-42d2-84e4-f0c1eaff9325",
      "type": "users",
      "pseudo": "john_doe",
      "email": "john.doe@example.com",
      "avatar": "/images/avatar-man.jpg"
    },
    {
      "_id": "d23b76c9-ca84-454e-8379-ddfad96ecdc0",
      "type": "users",
      "pseudo": "alice_smith",
      "email": "alice.smith@example.com",
      "avatar": "/images/avatar-woman.jpg"
    },
    {
      "_id": "953d86cd-8a26-47e6-9d5f-40a5128fa332",
      "type": "users",
      "pseudo": "mike_jones",
      "email": "mike.jones@example.com",
      "avatar": "/images/avatar-man.jpg"
    }    
]'''

fake_posts = '''[
	{
	  "_id": 1,
	  "title": "Lorem Ipsum Dolor Sit Amet",
	  "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac interdum lacus.",
	  "author": {
		"_id": 1,
		"pseudo": "john_doe",
		"email": "john.doe@example.com",
		"avatar": "https://example.com/avatar/john_doe.jpg"
	  },
	  "updatedAt": "2023-01-01T12:30:45Z",
	  "createdAt": "2023-01-01T12:30:45Z"
	},
	{
	  "_id": 2,
	  "title": "Aenean Condimentum Eros In Consectetur",
	  "body": "Aenean condimentum eros in consectetur venenatis. Nullam vel nunc ac turpis consequat fringilla.",
	  "author": {
		"_id": 2,
		"pseudo": "alice_smith",
		"email": "alice.smith@example.com",
		"avatar": "https://example.com/avatar/alice_smith.jpg"
	  },
	  "updatedAt": "2023-01-02T08:15:30Z",
	  "createdAt": "2023-01-02T08:15:30Z"
	},
	{
		"_id": 3,
		"title": "Suspendisse Euismod Egestas Ornare",
		"body": "Suspendisse euismod egestas ornare. In in ligula eu arcu aliquet tincidunt nec a enim.",
		"author": {
		  "_id": 3,
		  "pseudo": "mike_jones",
		  "email": "mike.jones@example.com",
		  "avatar": "https://example.com/avatar/mike_jones.jpg"
		},
		"updatedAt": "2023-01-03T16:45:22Z",
		"createdAt": "2023-01-03T16:45:22Z"
	  },
	  {
		"_id": 4,
		"title": "Vivamus Feugiat Nunc Sit Amet",
		"body": "Vivamus feugiat nunc sit amet elit facilisis, vitae lacinia justo gravida. Nullam efficitur justo eget ligula sagittis fermentum.",
		"author": {
		  "_id": 4,
		  "pseudo": "sara_brown",
		  "email": "sara.brown@example.com",
		  "avatar": "https://example.com/avatar/sara_brown.jpg"
		},
		"updatedAt": "2023-01-04T09:12:57Z",
		"createdAt": "2023-01-04T09:12:57Z"
	  },
	  {
		"_id": 5,
		"title": "Duis Diam Mauris, Ultricies Inceptos",
		"body": "Duis diam mauris, ultricies inceptos adipiscing vel, tristique nec libero. Fusce fringilla pharetra velit, vel luctus nulla vestibulum nec.",
		"author": {
		  "_id": 5,
		  "pseudo": "alex_wilson",
		  "email": "alex.wilson@example.com",
		  "avatar": "https://example.com/avatar/alex_wilson.jpg"
		},
		"updatedAt": "2023-01-05T14:28:40Z",
		"createdAt": "2023-01-05T14:28:40Z"
	  },
	  {
		"_id": 6,
		"title": "Pellentesque Mattis Risus At Tellus",
		"body": "Pellentesque mattis risus at tellus feugiat vestibulum. Proin eget hendrerit sem, vitae gravida dui.",
		"author": {
		  "_id": 6,
		  "pseudo": "emily_martin",
		  "email": "emily.martin@example.com",
		  "avatar": "https://example.com/avatar/emily_martin.jpg"
		},
		"updatedAt": "2023-01-06T18:09:15Z",
		"createdAt": "2023-01-06T18:09:15Z"
	  },
	  {
		"_id": 7,
		"title": "Nullam Eu Sagittis Elit",
		"body": "Nullam eu sagittis elit. Duis tincidunt ultrices felis, nec cursus leo hendrerit id. Quisque nec imperdiet dui.",
		"author": {
		  "_id": 7,
		  "pseudo": "peter_clark",
		  "email": "peter.clark@example.com",
		  "avatar": "https://example.com/avatar/peter_clark.jpg"
		},
		"updatedAt": "2023-01-07T11:55:28Z",
		"createdAt": "2023-01-07T11:55:28Z"
	  },
	  {
		"_id": 8,
		"title": "In Ut Semper Mollis",
		"body": "In ut semper mollis. Suspendisse potenti. Vestibulum congue augue vel mauris faucibus, at hendrerit lectus pulvinar.",
		"author": {
		  "_id": 8,
		  "pseudo": "laura_jackson",
		  "email": "laura.jackson@example.com",
		  "avatar": "https://example.com/avatar/laura_jackson.jpg"
		},
		"updatedAt": "2023-01-08T07:36:44Z",
		"createdAt": "2023-01-08T07:36:44Z"
	  },
	  {
		"_id": 9,
		"title": "Aliquam Erat Volutpat",
		"body": "Aliquam erat volutpat. Curabitur a tortor ut neque cursus rhoncus. Sed ut vestibulum odio.",
		"author": {
		  "_id": 9,
		  "pseudo": "kevin_adams",
		  "email": "kevin.adams@example.com",
		  "avatar": "https://example.com/avatar/kevin_adams.jpg"
		},
		"updatedAt": "2023-01-09T15:20:12Z",
		"createdAt": "2023-01-09T15:20:12Z"
	  },
	  {
		"_id": 10,
		"title": "Ut Et Eros Euismod",
		"body": "Ut et eros euismod, suscipit odio vel, fermentum odio. Vestibulum ut efficitur elit.",
		"author": {
		  "_id": 10,
		  "pseudo": "natalie_white",
		  "email": "natalie.white@example.com",
		  "avatar": "https://example.com/avatar/natalie_white.jpg"
		},
		"updatedAt": "2023-01-10T09:45:37Z",
		"createdAt": "2023-01-10T09:45:37Z"
	  },
	  {
		"_id": 11,
		"title": "Fusce Ac Eros Velit",
		"body": "Fusce ac eros velit. Integer vel congue justo. Proin ut ligula quis risus varius venenatis.",
		"author": {
		  "_id": 11,
		  "pseudo": "olivia_morris",
		  "email": "olivia.morris@example.com",
		  "avatar": "https://example.com/avatar/olivia_morris.jpg"
		},
		"updatedAt": "2023-01-11T14:55:22Z",
		"createdAt": "2023-01-11T14:55:22Z"
	  },
	  {
		"_id": 12,
		"title": "Phasellus Feugiat Sapien Odio",
		"body": "Phasellus feugiat sapien odio, in tristique turpis imperdiet vel. Nunc nec urna vel elit faucibus consequat.",
		"author": {
		  "_id": 12,
		  "pseudo": "daniel_brown",
		  "email": "daniel.brown@example.com",
		  "avatar": "https://example.com/avatar/daniel_brown.jpg"
		},
		"updatedAt": "2023-01-12T08:10:45Z",
		"createdAt": "2023-01-12T08:10:45Z"
	  },
	  {
		"_id": 13,
		"title": "Vestibulum Bibendum Consectetur",
		"body": "Vestibulum bibendum consectetur velit, eget tristique arcu fermentum vitae. Suspendisse potenti. Nam non facilisis libero.",
		"author": {
		  "_id": 13,
		  "pseudo": "william_carter",
		  "email": "william.carter@example.com",
		  "avatar": "https://example.com/avatar/william_carter.jpg"
		},
		"updatedAt": "2023-01-13T16:30:18Z",
		"createdAt": "2023-01-13T16:30:18Z"
	  },
	  {
		"_id": 14,
		"title": "Cras Eleifend Tristique Nisi",
		"body": "Cras eleifend tristique nisi, vel vehicula augue tristique at. Aenean in lectus non tortor iaculis fermentum.",
		"author": {
		  "_id": 14,
		  "pseudo": "emma_smith",
		  "email": "emma.smith@example.com",
		  "avatar": "https://example.com/avatar/emma_smith.jpg"
		},
		"updatedAt": "2023-01-14T10:05:33Z",
		"createdAt": "2023-01-14T10:05:33Z"
	  },
	  {
		"_id": 15,
		"title": "Pellentesque Laoreet Justo Ut",
		"body": "Pellentesque laoreet justo ut velit luctus, vel suscipit tortor vestibulum. Sed tincidunt neque vel malesuada vulputate.",
		"author": {
		  "_id": 15,
		  "pseudo": "megan_jones",
		  "email": "megan.jones@example.com",
		  "avatar": "https://example.com/avatar/megan_jones.jpg"
		},
		"updatedAt": "2023-01-15T14:20:47Z",
		"createdAt": "2023-01-15T14:20:47Z"
	  },
	  {
		"_id": 16,
		"title": "Vivamus Tristique Neque Velit",
		"body": "Vivamus tristique neque velit, et dignissim justo eleifend vel. Nam ullamcorper justo ac leo convallis, vel pharetra quam fringilla.",
		"author": {
		  "_id": 16,
		  "pseudo": "nathan_wilson",
		  "email": "nathan.wilson@example.com",
		  "avatar": "https://example.com/avatar/nathan_wilson.jpg"
		},
		"updatedAt": "2023-01-16T08:45:12Z",
		"createdAt": "2023-01-16T08:45:12Z"
	  },
	  {
		"_id": 17,
		"title": "Integer Nec Magna Non",
		"body": "Integer nec magna non mi consectetur sagittis. Duis vel ipsum nec turpis lacinia sollicitudin.",
		"author": {
		  "_id": 17,
		  "pseudo": "grace_anderson",
		  "email": "grace.anderson@example.com",
		  "avatar": "https://example.com/avatar/grace_anderson.jpg"
		},
		"updatedAt": "2023-01-17T12:10:35Z",
		"createdAt": "2023-01-17T12:10:35Z"
	  },
	  {
		"_id": 18,
		"title": "Cras Mattis Eros Euismod Nulla",
		"body": "Cras mattis eros euismod nulla pellentesque, eu consectetur libero aliquet. Sed fringilla, tortor at mattis tincidunt, est lacus congue ligula.",
		"author": {
		  "_id": 18,
		  "pseudo": "ryan_campbell",
		  "email": "ryan.campbell@example.com",
		  "avatar": "https://example.com/avatar/ryan_campbell.jpg"
		},
		"updatedAt": "2023-01-18T18:55:20Z",
		"createdAt": "2023-01-18T18:55:20Z"
	  },
	  {
		"_id": 19,
		"title": "Sed Dignissim Justo Ac",
		"body": "Sed dignissim justo ac tortor congue, eu aliquet mauris aliquam. Vivamus consectetur scelerisque leo, et dapibus odio tempus a.",
		"author": {
		  "_id": 19,
		  "pseudo": "hannah_martin",
		  "email": "hannah.martin@example.com",
		  "avatar": "https://example.com/avatar/hannah_martin.jpg"
		},
		"updatedAt": "2023-01-19T09:30:44Z",
		"createdAt": "2023-01-19T09:30:44Z"
	  },
	  {
		"_id": 20,
		"title": "Maecenas Posuere Magna Nec",
		"body": "Maecenas posuere magna nec felis vestibulum fermentum. Ut vel purus ut purus sollicitudin dignissim.",
		"author": {
		  "_id": 20,
		  "pseudo": "owen_jackson",
		  "email": "owen.jackson@example.com",
		  "avatar": "https://example.com/avatar/owen_jackson.jpg"
		},
		"updatedAt": "2023-01-20T14:15:28Z",
		"createdAt": "2023-01-20T14:15:28Z"
	  }
  ]'''

posts_list = json.loads(fake_posts)
users_list = json.loads(fake_users)

def pick(items):
	# Pick a random index within the range of the list length
	random_index = random.randint(0, len(items) - 1)

	# Access the value at the random index
	random_value = items[random_index]
	return random_value

def generate_uuid():
	unique_id = uuid.uuid4()	
	return str(unique_id)

def generate(posts, authors, n = 50):
	r = []
	for i in range(n):
		picked = pick(posts_list)
		picked = {
			**picked,
			'_id': generate_uuid(),
			'rank': i+1,
			'type': 'posts',
			'author': pick(users_list)
		}
		r.append(picked)
	return r

results = generate(posts_list, users_list, 500)

def to_json(filename, content):
	# Save the results into a JSON file
	with open(f'{filename}.json', 'w') as json_file:
	    json.dump(content, json_file, indent=4)

to_json('fake_posts', results)
to_json('fake_users', users_list)