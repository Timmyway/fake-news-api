const users = require('../datas/users.json');

exports.getUsers = (req, res) => {	
	res.json(users);
}