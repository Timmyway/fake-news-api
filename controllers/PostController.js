const posts = require('../datas/posts.json');

exports.getPosts = (req, res) => {	
	res.json(posts);
}