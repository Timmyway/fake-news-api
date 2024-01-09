const users = require('../datas/users.json');

exports.allUsers = (req, res) => {	
	res.json({ users });
}