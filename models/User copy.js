const db = require('../db/connection');
const util = require('util');
const Model = require('./Model');

class User extends Model {
  async insertAll(users) {
    const bulkDocsAsync = util.promisify(this.db.bulkDocs.bind(this.db));
    try {
        const response = await bulkDocsAsync(users);
        console.log('Documents created Successfully');
        return { status: 'ok', message: 'Users created Successfully' };
      } catch (err) {
        console.error(err);
        throw err;
      }
  }
  
  async getDoc(docId) {
    const getDocAsync = util.promisify(this.db.get.bind(this.db));
    try {
        const response = await getDocAsync(docId);
        console.log('Documents created Successfully');
        return response;
      } catch (err) {
        console.error(err);
        throw err;
      }
  }

  async all() {
    try {
      const response = await this.db.allDocs();
      return response;
    } catch (error) {
      throw error;
    }
  }
}

module.exports = new User(db);