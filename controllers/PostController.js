const User = require('../models/User');
const Post = require('../models/Post');
const postList = require('../datas/posts.json');

exports.getPosts = async (req, res) => {
	console.log('==> Get list of posts...');
	try {
		const posts = await Post.find({}, 5);
		console.log(`Found ${posts?.docs?.length} posts.`);
		return res.json(posts);
	} catch(error) {
		return res.json({error})
	}	
}

exports.getPost = async (req, res) => {
	const response = await User.getDoc(postId);
	console.log('=====>', response);
	return res.json(response);
}

exports.bulkInsertPost = async (req, res) => {	
	const response = await Post.bulkInsert(postList);
	console.log(`Post has been recorded ! ${response?.status}`);		
	res.json({'status': 'finished'});
	console.log(postList);
}