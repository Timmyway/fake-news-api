const express = require('express');

const router = express.Router();

const UserController = require('../controllers/UserController');
const PostController = require('../controllers/PostController');

router.get('/users', UserController.getUsers);
router.get('/posts', PostController.getPosts);

module.exports = router;