
const mongoose = require('mongoose')

const carDataScheme = mongoose.Schema({
    make:{
        type: String, 
        required: true
    },
    title: {
        type: String,
        required: true
    },
    year: {
        type: String,
        required: true
    },
    price: {
        type: String,
        required: true
    },
    mileage: {
        type: String,
        required: true
    },
    condition: {
        type: String,
        required: true
    },
    specifications: {
        type: String,
        required: true
    },
    zipcode: {
        type: Number,
        required: true
    }
})

module.exports = mongoose.model('listings_collection', carDataScheme)