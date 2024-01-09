const express = require('express');

const router = express.Router();

const UserController = require('../controllers/UserController');
const PostController = require('../controllers/PostController');

router.get('/api/users', UserController.getUsers);
router.get('/api/posts', PostController.getPosts);

module.exports = router;