const express = require('express');

const router = express.Router();

const UserController = require('../controllers/UserController');
const PostController = require('../controllers/PostController');

router.get('/api/users', UserController.getUsers);
router.post('/api/users', UserController.createUsers)
router.get('/api/post/:postId', PostController.getPost);
router.get('/api/post', PostController.getPosts);
router.post('/api/post', PostController.bulkInsertPost);

module.exports = router;