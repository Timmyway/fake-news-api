const remoteDb = require('../db/connection');
const util = require('util');

class Model {    
    constructor() {
      this.db = remoteDb; // Replace with your CouchDB instance URL      
      this.createIndex(['type', 'rank']);
      this.name = 'model';
    }

    createIndex(indexFields) {
        this.db.createIndex({
            index: {fields: indexFields}
        });
    }

    getName() {
        return this.name;
    }

    setName(name) {
        this.name = name;
    }    
  
    async find(query = {}, limit = 100) {
      try {
        const response = await this.db.find({
            selector: {
              type: this.name,
              ...query
            },
            sort: [{ 'rank': 'desc' }],
            limit
        });        
        console.log('===========> Record found: ', response?.length);
        return response;
      } catch (error) {
        throw error;
      }
    }    

    async bulkInsert(docs) {
        const bulkDocsAsync = util.promisify(this.db.bulkDocs.bind(this.db));
        try {
            const response = await bulkDocsAsync(docs);
            console.log('Documents created Successfully');
            return { status: 'ok', message: 'Users created Successfully' };
          } catch (err) {
                console.error(err);
            throw err;
          }
      }
  }
  
  module.exports = Model;