const User = require('../models/User');

exports.getUsers = async (req, res) => {
	try {
		const users = await User.find();
		return res.json(users);
	} catch(error) {
		return res.json({error})
	}	
}

exports.createUsers = async (req, res) => {
	const response = await User.insertAll(users);
	console.log('=====>', response);
	if (response?.status === 'ok') {
		return res.json({ response: response.message })
	}
	return res.json({ error: 'Could not create users' })
}