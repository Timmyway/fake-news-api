const db = require('../db/connection');
const Model = require('./Model');

class Post extends Model {
    constructor() {
        super()
        this.setName('posts');        
    }
}

module.exports = new Post();