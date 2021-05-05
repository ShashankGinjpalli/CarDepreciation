const express = require('express');
const carData = require('../models/CarData')


const router = express.Router();

router.get('/', (req, res) =>{
    res.send('This is the cars route')
})

router.post('/', (req,res) =>{
    console.log(req.body)
    const listing = new carData({
        title: req.body.title,
        price: req.body.price,
        mileage: req.body.mileage, 
        condition: req.body.condition, 
        specifications: req.body.specifications
    });

    listing.save()
    .then(data => {
        res.json(data);
    })
    .catch(err => {
        res.json(err);
    });
});


module.exports = router;  