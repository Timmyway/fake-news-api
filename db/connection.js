const pouchDB = require("pouchdb");
pouchDB.plugin(require('pouchdb-find'));

// CouchDB credentials
const username = 'timmy';
const password = '123456';

// URL with authentication information
const url = `http://${username}:${password}@localhost:5984/remote_livenews`;

// Create a new database instance with authentication
const db = new pouchDB(url);

// Export the database instance
module.exports = db;