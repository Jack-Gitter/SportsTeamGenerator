
document.callThreePointerAPI = callThreePointerAPI


function callThreePointerAPI(){
    var dateControl = document.querySelector('input[type="date"]');
    date = dateControl.value.split("-")
    month = date[1]
    day = date[2]
    url = "https://jojex5vzdi.execute-api.us-east-1.amazonaws.com/Prod/threepointshooters?birthDay="+day+"&birthMonth="+month
    fetch(url).then(res => res.json()).then(data => populateTable(data))
}

function populateTable(data) {
    playerRow = document.getElementById("player-row")
    len = playerRow.cells.length
    for (i = 0; i < len; i++) {
        playerRow.deleteCell(0)
    }
    statRow = document.getElementById("stat-row")
    len = statRow.cells.length
    for (i = 0; i < len; i++) {
        statRow.deleteCell(0)
    }
    
    playerCell = playerRow.insertCell()
    playerText = document.createTextNode('player');
    playerCell.appendChild(playerText);

    statCell = statRow.insertCell()
    statText = document.createTextNode("statline")
    statCell.appendChild(statText)

    for (player in data) {
        playerCell = playerRow.insertCell()
        playerText = document.createTextNode(player)
        playerCell.appendChild(playerText)
    }

    for (player in data) {
        statCell = statRow.insertCell()
        statText = document.createTextNode(data[player])
        statCell.appendChild(statText)
    }
    


  


}


