
function processCarData(data){
    console.log("Processing Data")

    //def set of models
    const modelsSet = new Set([]);
    const prices = []
    const miles = []
    var conditionDict = {}

    for (const entry in data) {
        console.log(data[entry])
        modelsSet.add(data[entry].title)
        if(data[entry].price != "Not Priced" && data[entry].mileage != "-- mi."){
            let psubstr = data[entry].price.substring(1);
            let price = parseInt(psubstr.replace(/,/g, ''))
            prices.push(price)

            let msubstr = data[entry].mileage;
            msubstr = msubstr.substring(0, msubstr.length - 3);
            let mile = parseInt(msubstr.replace(/,/g, ''))
            miles.push(mile)

            if(data[entry].condition in conditionDict){
                conditionDict[data[entry].condition] += 1
            }else{
                conditionDict[data[entry].condition] = 0
            }
        }
    }

    console.log(modelsSet)
    console.log(prices)
    console.log(miles)
    console.log(conditionDict)
}

async function getCarDataRequest(selectedMake, selectedModel, selectedYear, selectedZip){
    var url = new URL('http://localhost:3000/carListings/getSpecificListing')
    var params = {make:selectedMake, title:selectedModel, year:selectedYear, zipcode:selectedZip}
    url.search = new URLSearchParams(params).toString();

    fetch(url)
    .then(res => {
        return res.json()
    })
    .then(data => processCarData(data))
    .catch(err => {
        console.log(err)
    })

}



var values = getCarDataRequest("Honda", "Pilot", "2018", 95123)


   


/*
async function getData(url = '', ) {
    const response = await fetch(url,{mode: 'no-cors'});
    console.log(response.data)
    return response.json();
};

getData();
*/

/*
const Http = new XMLHttpRequest();
const url='http://localhost:3000/carListings/getSpecificListing?make=Honda&title=Accord&year=2017&zipcode=95123';
Http.open("GET", url);

Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}
*/