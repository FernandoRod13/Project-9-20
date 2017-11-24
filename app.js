var express = require('express')
var app = express()

app.get('/', (req, res) => {
    res.status(200).send('Project 9-20').end();
});

app.post('/login', (req, res) => {
    res.status(200).send('login success').end();
});

app.post('/register/supplier', (req, res) => {
    res.status(200).send('new supplier registered successfully').end();
});

app.post('/register/user', (req, res) => {
    res.status(200).send('new user registered successfully').end();
});

app.post('/register/admin', (req, res) => {
    res.status(200).send('new admin registered successfully').end();
});

app.post('/request/resource', (req, res) => {
    res.status(200).send('resource requested successfully').end();
});

app.post('/notification/new_resource/:resourceID', (req, res) => {
    res.status(200).send('Sent new notification to users requesting this resource').end();
});

app.post('/notification/new_resource/:resourceID', (req, res) => {
    res.status(200).send('Sent new notification to users requesting this resource').end();
});

app.post('/purchase/resource/:reosurceID', (req, res) => {
    res.status(200).send('Sent new notification to users requesting this resource').end();
});

app.get('/resources/available', (req, res) => {
    res.status(200).send('Requested al available resources').end();
});

app.get('/resources/requested', (req, res) => {
    res.status(200).send('Requested al available resources').end();
});
  
app.get('/resources/requested/keyword/:keywords', (req, res) =>{
    res.status(200).send('Here are all resources with the keyword').end();
}); 

app.get('/resources/available/keyword/:keywords', (req, res) =>{
    res.status(200).send('Here are all resources with the keyword').end();
});

app.get('/statistics/day/:startDate', (req, res) =>{
    res.status(200).send('Here are the statiscis for this day').end();
});

app.get('/statistics/week/:startDate', (req, res) =>{
    res.status(200).send('Here are the statiscis for this week').end();
});
app.get('/statistics/region/:regionID', (req, res) =>{
    res.status(200).send('Here are the statiscis for this region').end();
});

  // Start the server
  const PORT = process.env.PORT || 8080;
  app.listen(PORT, () => {
    console.log(`App listening on port ${PORT}`);
    console.log('Press Ctrl+C to quit.');
  });
  
