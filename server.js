const express = require('express')
const app = express()
const books = require('./db')

app.get('/books', (req, res) => {
  res.json(books)
})
app.get('/', (req, res) => {
  res.send('Hello World')
})

app.listen(3000, () => {
  console.log('Start server at port 3000.')
})