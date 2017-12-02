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

// // ADD Resources Avalible
// rl.question('# of Resources, name1, description1, name2, description2 ... namen,descriptionn : ', (answer) => {
//   var list = _.split(answer, ',',30);
//   console.log(list);
//   var i = _.trim(list[0]);
//   console.log(`You Added ${i} Resources`);
   
//   for ( var j=1; j <= i*2; j+=2){  
//   //console.log(`test ${list[j]}  ${j}`);
//   //console.log(`tes: ${list[j+1]} ${j+1}`);
//   jsMaker.addResource(_.trim(list[j]),_.trim(list[j+1]),'resources_avaliable_data.json');  
//   }  
//  rl.close();
// });

// ADD Resources Requested
rl.question('# of Resources, name1, description1, name2, description2 ... namen,descriptionn : ', (answer) => {
  var list = _.split(answer, ',',30);
  console.log(list);
  var i = _.trim(list[0]);
  console.log(`You Added ${i} Resources`);

  for ( var j=1; j <= i*2; j+=2){  
  console.log(`test ${list[j]}  ${j}`);
  console.log(`tes: ${list[j+1]} ${j+1}`);
  jsMaker.addResource(_.trim(list[j]),_.trim(list[j+1]),'resources_requested_data.json');  
  }  
 rl.close();
});
