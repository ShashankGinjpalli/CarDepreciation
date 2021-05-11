const express = require('express');
const carData = require('../models/CarData')


const router = express.Router();

router.get('/', async (req, res) => {
    try{
        const listings = await carData.find({
            "make": req.body.make,
            "title": {'$regex': req.body.title, '$options': 'i'},
            "year": req.body.year
    });
        res.json(listings);
    } catch(err){
        res.json({err});
    }
    
})

router.post('/', async (req, res) => {
    console.log(req.body)
    const listing = new carData({
        make: req.body.make,
        title: req.body.title,
        year: req.body.year,
        price: req.body.price,
        mileage: req.body.mileage,
        condition: req.body.condition,
        specifications: req.body.specifications
    });

    try{
        const savedListing = await listings.save();
        res.json(savedListing)
    }catch(err){
        res.json(err)
    }

    // listing.save()
    //     .then(data => {
    //         res.json(data);
    //     })
    //     .catch(err => {
    //         res.json(err);
    //     });
});


module.exports = router;