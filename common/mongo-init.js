// init-script.js
var dbName = process.env.MONGO_INITDB_DATABASE || 'default_database';
var collectionName = process.env.MONGO_INITDB_COLLECTION || 'default_collection';

db = db.getSiblingDB(dbName);

// Create a collection (optional)
db.createCollection(collectionName);

print('Initialization script completed.');