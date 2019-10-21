'use strict';
const admin = require('firebase-admin');
const fs = require('fs');
const functions = require('firebase-functions');
var serviceAccount = require('./pingu-c43b5-firebase-adminsdk-51hbn-8382c08afc.json');
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://pingu-c43b5.firebaseio.com"
  });


let db = admin.firestore();
// db.collection('locations').get()
//   .then((snapshot) => {
//     snapshot.forEach((doc) => {
//       console.log(doc.id, '=>', doc.data());
//     });
//   })
//   .catch((err) => {
//     console.log('Error getting documents', err);
//   });
let citiesRef = db.collection('locations');
let query = citiesRef.where('flag', '==', "v").get()
  .then(snapshot => {
    if (snapshot.empty) {
      console.log('No matching documents.');
      return;
    }  
    fs.writeFileSync('data.json','{')
    snapshot.forEach(doc => {
      var data = JSON.stringify(doc.data(), null, 2);
      console.log(data)
      fs.appendFileSync('data.json', data);
      fs.appendFileSync('data.json', ',');

      //console.log(doc.data());
    });
    fs.appendFileSync('data.json','}')
  })
  .catch(err => {
    console.log('Error getting documents', err);
  });