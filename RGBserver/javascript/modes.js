const speed = document.getElementById("speed")
const standard = document.getElementById("standard")
const rainbow = document.getElementById("rainbow")
const norway = document.getElementById("norway")
const colorDrip = document.getElementById("colorDrip")
const alarmClock = document.getElementById("alarmClock")
const theaterChase = document.getElementById("theaterChase")
const sliderButtonModes = document.getElementById("phonebutton-slider-modes")

function getJSON(url) {
    var j = []
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
        success: function(data) { j = data},
        async: false
    })
    return j
}

standard.addEventListener("click", (event) => {
    getJSON(`${url}/modes/set?mode=standard`)
})

rainbow.addEventListener("click", (event) => {
    getJSON(`${url}/modes/set?mode=rainbow`)
})

norway.addEventListener("click", (event) => {
    getJSON(`${url}/modes/set?mode=norway`)
})

colorDrip.addEventListener("click", (event) => {
    getJSON(`${url}/modes/set?mode=colorDrip`)
})

alarmClock.addEventListener("click", (event) => {
    getJSON(`${url}/modes/set?mode=alarmClock`)
})

theaterChase.addEventListener("click", (event) => {
    getJSON(`${url}/modes/set?mode=theaterChase`)
})

speed.value = getJSON(`${url}/json/data.json`).speed

sliderButtonModes.addEventListener("click", (event) => {
    getJSON(`${url}/?panel=modes&speed=${speed.value}`)
})

alarmClock.addEventListener("click", (event) => {
    const alarmTime = prompt("What time do you want to wake up?", `${getJSON(`${url}/json/data.json`).alarmClockData.alarmTime}`)
    getJSON(`${url}/?panel=modes&mode=alarmClock&alarmTime=${alarmTime}`)
})

speed.onmouseup = () => {
    getJSON(`${url}/?panel=modes&speed=${speed.value}`)
}
