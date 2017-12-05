const fs = require('fs'); //Load Modules Functionalistes of NODEJS
const os = require('os');
const _ = require('lodash'); // Common Untiilies Needs
const jsMaker = require('./jsonMaker.js'); //Anadir file mio
const yargs = require('yargs');
const readline = require('readline');


const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Please selet the type of resource to add by de-Commeting that porcion of code

// // ADD Resources Avalible
// rl.question('# of Resources, Name, Category, Subcategory:  : ', (answer) => {
//   var list = _.split(answer, ',',30);
//  // console.log(list);
//   var i = _.trim(list[0]);
//   console.log(`You Added ${i} Resources`);
   
//   for ( var j=1; j < i*4; j+=4){  
//     //console.log(`test ${list[j]}  ${j}`);
//     //console.log(`tes: ${list[j+1]} ${j+1}`);
//     jsMaker.addResource(_.trim(list[j]),_.trim(list[j+1]),'resources_avaliable_data.json','avalible',_.trim(list[j+2]),_.trim(list[j+3]));  
//     } 
//  rl.close();
// });

// // ADD Resources Requested
// rl.question('# of Resources, Name, Category, Subcategory: ', (answer) => {
//   var list = _.split(answer, ',',30);
//   //console.log(list);
//   var i = _.trim(list[0]);
//   console.log(`You Added ${i} Resources`);

//   for ( var j=1; j <= i*4; j+=4){  
//   //console.log(`test ${list[j]}  ${j}`);
//   //console.log(`tes: ${list[j+1]} ${j+1}`);
//   jsMaker.addResource(_.trim(list[j]),_.trim(list[j+1]),'resources_requested_data.json','requested',_.trim(list[j+2]),_.trim(list[j+3]));  
//   }  
//  rl.close();
// });

// ADD User, in the mark area change the type and file has need
rl.question('# of Users, type,file, Name, Municipality: ', (answer) => {
  var list = _.split(answer, ',');
  var i = _.trim(list[0]);
  console.log(`You Added ${i} Resources`);

  for ( var j=3; j <= i*4; j+=2){  
 
  jsMaker.addUser(_.trim(list[j]),_.trim(list[j+1]),'user.json');  
  }  
 rl.close();
});


