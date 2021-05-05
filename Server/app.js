const express = require('express')
require('dotenv').config()
const app = express()
const mongoose = require('mongoose')
const bodyParser = require('body-parser')

var port = 3000

// Connect to DB
mongoose.connect(process.env.DATABASE_URL, { useNewUrlParser: true , useUnifiedTopology: true }, () =>
    console.log("Connected to Database")
)

app.use(bodyParser.json())

// Import Routes
const carRoute = require('./routes/carlistings')
app.use('/carListings', carRoute)



app.listen(port, () => console.log("Server Listening on Port: " + port))