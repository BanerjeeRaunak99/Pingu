const admin = require('firebase-admin');
const functions = require('firebase-functions');
var serviceAccount = require('./pingu-c43b5-firebase-adminsdk-51hbn-8382c08afc.json');
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://pingu-c43b5.firebaseio.com"
  });


let db = admin.firestore();
db.collection('locations').get()
  .then((snapshot) => {
    snapshot.forEach((doc) => {
      console.log(doc.id, '=>', doc.data());
    });
  })
  .catch((err) => {
    console.log('Error getting documents', err);
  });
 
