
const fs = require('fs');



var fetchData= (file) =>{

  try{
  var noteString =  fs.readFileSync(file);
  console.log(file);
  return JSON.parse(noteString);
  }catch(e){
    return []; //Empty Array
  }
};


var saveNotes = (notes,file) =>{
  fs.writeFileSync(file, JSON.stringify(notes));
};

var addResource= (name, resource, file) => {

  var notes = fetchData();

  var note = {
    name: name,
    resource: resource
  };
list = fetchData(file);
list.push(note);
saveNotes(list,file);
};


var removeNote = (title) => {
  var notes = fetchData ();

  var toRemove = notes.filter((note) =>  note.title !== title); //Todas las notas que no son tittle
  saveNotes(toRemove);
  return notes.length !== toRemove.length;
};

var readNote = (title) => {
  var notes = fetchData ();
  var toread = notes.filter((note) => note.title === title);
  return toread[0];
};


var getAll = () => {
 return fetchData ();

};


module.exports = {
  addResource,
  getAll  

};



