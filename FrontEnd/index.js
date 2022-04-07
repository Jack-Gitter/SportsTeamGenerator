
function callThreePointerAPI(){
    url = "https://jojex5vzdi.execute-api.us-east-1.amazonaws.com/Prod/threepointshooters?birthDay=2&birthMonth=5"
    fetch(url).then(res => res.json()).then(data => console.log(data))
}


document.callThreePointerAPI = callThreePointerAPI