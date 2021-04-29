function alarmTimes() {
    const alarmTimeDay = document.getElementById("alarmTimeDay")
    const alarmTimeHour = document.getElementById("alarmTimeHour")
    const alarmTimeMinute = document.getElementById("alarmTimeMinute")
    const saveButton = document.getElementById("saveAlarmTimeButton")
    const activeAlarmsContainer = document.getElementById("activeAlarmsContainer")

    const alarms = getJSON(`${url}/json/alarmTimes.json`).times

    for (let i = 0; i < alarms.length; i++) {
        const alarmDiv = document.createElement("div")
        alarmDiv.classList.add("Content-subBox")

        const alarmText = document.createElement("p")
        alarmText.classList.add("Body-Text")
        alarmText.innerHTML = alarms[i]
        alarmDiv.appendChild(alarmText)

        const deleteButton = document.createElement("button")
        deleteButton.classList.add("button")

        const deleteIcon = document.createElement("i")
        deleteIcon.classList.add("fa fa-trash")
        deleteButton.appendChild(deleteIcon)
        alarmDiv.appendChild(deleteButton)
        activeAlarmsContainer.appendChild(alarmDiv)
    }

    let i = 0
    while (i < 24) {
        let option = document.createElement("option")
        if (i < 10) {
            option.value = `0${i}`
            option.innerHTML = `0${i}`
        }else {
            option.value = `${i}`
            option.innerHTML = `${i}`
        }
        alarmTimeHour.appendChild(option)
        i++
    }

    i = 0
    while (i < 60) {
        let option = document.createElement("option")
        if (i < 10) {
            option.value = `0${i}`
            option.innerHTML = `0${i}`
        }else {
            option.value = `${i}`
            option.innerHTML = `${i}`
        }
        alarmTimeMinute.appendChild(option)
        i++
    }

    saveButton.addEventListener("click", (event) => {
        const alarmTime = `${alarmTimeDay.value}-${alarmTimeHour.value}-${alarmTimeMinute.value}`
        alarms = getJSON(`${url}/json/alarmTimes.json`).times

        if (alarms.includes(alarmTime)) {
            alert("Alarm time already exists")
        }
        else {
            getJSON(`${url}/alarmTimes/edit?mode=new&alarmTime=${alarmTime}`)
        }
    })
}

alarmTimes()