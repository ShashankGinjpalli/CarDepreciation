const express = require('express');
const carData = require('../models/CarData')


const router = express.Router();

router.get('/specific', async (req, res) => {
    try{
        const listings = await carData.find({
            "make": {'$regex': req.body.make, '$options': 'i'},
            "title": {'$regex': req.body.title, '$options': 'i'},
            "year": {'$regex': req.body.year, '$options': 'i'}
    });
        // const listings = await carData.find({})
        res.json(listings);
    } catch(err){
        res.json({err});
    }
    
})

router.get('/all', async (req, res) => {
    try{
        const listings = await carData.find({});
        res.json(listings);

    }catch(err){
        res.json({err});
    }

})

router.get('/zip', async (req, res) => {
    try{
        const listings = await carData.find({
            "zipcode": req.body.zipcode
        });
        res.json(listings);

    }catch(err){
        res.json({err});
    }

})

router.get('/zip', async (req, res) => {
    try{
        const listings = await carData.find({});
        res.json(listings);

    }catch(err){
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
        specifications: req.body.specifications,
        zipcode: req.body.zipcode
    });

    try{
        const savedListing = await listing.save();
        res.json(savedListing)
    }catch(err){
        res.json(err)
    }

});


module.exports = router;