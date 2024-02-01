function saklar(action, lamp) {
    let toggle = document.getElementById('default-toggle')
    console.log("testing is " + toggle.value);
    console.log(action);
    console.log("Your lamp " + lamp + " is " + action)
    let lampu1 = document.getElementById('lampu1')
    let lampu2 = document.getElementById('lampu2')
    let lampu3 = document.getElementById('lampu3')

    if (action == "on") {
        // nyala
        if (lamp == 1) {
            lampu1.src = 'on.png'
        } else if (lamp == 2) {
            lampu2.src = 'on.png'
        } else {
            lampu3.src = 'on.png'
        }

    }
    if (action == "off") {
        // mati
        if (lamp == 1) {
            lampu1.src = 'off.png'
        } else if (lamp == 2) {
            lampu2.src = 'off.png'
        } else {
            lampu3.src = 'off.png'
        }
    }

    return lampu1;
}