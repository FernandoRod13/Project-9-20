
const fs = require('fs');

var logNote = (note) => {
  debugger;
  console.log('---------- ');
  console.log(`Title: ${note.title}`);
  console.log(`Body: ${note.body}`);
};

var fetchNotes = () =>{

  try{
  var noteString =  fs.readFileSync('note_data.json');
  return JSON.parse(noteString);
  }catch(e){
    return []; //Empty Array
  }
};

var saveNotes = (notes) =>{
  fs.writeFileSync('note_data.json', JSON.stringify(notes));
};

var addResource= (name, resource) => {

  var notes = fetchNotes();

  var note = {
    name: name,
    resource: resource
  };
list = fetchNotes();
list.push(note);
saveNotes(list);
};


var removeNote = (title) => {
  var notes = fetchNotes ();

  var toRemove = notes.filter((note) =>  note.title !== title); //Todas las notas que no son tittle
  saveNotes(toRemove);
  return notes.length !== toRemove.length;
};

var readNote = (title) => {
  var notes = fetchNotes ();
  var toread = notes.filter((note) => note.title === title);
  return toread[0];
};


var getAll = () => {
 return fetchNotes ();

};


module.exports = {
  addResource,
  getAll  

};




//
// module.exports.addNote = () => {
//   console.log('addNote');
//   return 'New note';
// };
//
// module.exports.add = (a, b) => {
//   return a+b;
// };
