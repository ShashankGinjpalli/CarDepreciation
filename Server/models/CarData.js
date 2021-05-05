const mongoose = require('mongoose')

const carDataScheme = mongoose.Schema({
    title: {
        type: String, 
        required: true
    },
    price:{
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
    }
})

module.exports = mongoose.model('CarData', carDataScheme)