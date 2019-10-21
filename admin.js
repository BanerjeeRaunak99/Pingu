'use strict';
const admin = require('firebase-admin');
const fs = require('fs');
const functions = require('firebase-functions');
var serviceAccount = require('./pingu-86df8-firebase-adminsdk-h9v0s-08ef71bae2.json');
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://pingu-86df8.firebaseio.com"
  });


let db = admin.firestore();

let citiesRef = db.collection('connections');
console.log(citiesRef)
let query = citiesRef.where('flag', '==', 1).get()
  .then(snapshot => {
    if (snapshot.empty) {
      console.log('No matching documents.');
      return;
    }  
    fs.writeFileSync('data.json','{')
    snapshot.forEach(doc => {
      var data = JSON.stringify(doc.data(), null, 2);
      //console.log(data)
      fs.appendFileSync('data.json',JSON.stringify(doc.id)+':'+ data);
      fs.appendFileSync('data.json', ',');

      //console.log(doc.data());
    });
    fs.appendFileSync('data.json','}')

  })
  .catch(err => {
    console.log('Error getting documents', err);
  });