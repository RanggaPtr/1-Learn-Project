function saklar(params) {
    console.log(params);
    console.log("Your lamp is " + params)
    let lampu1 = document.getElementById('lampu1')

    if (params == "on") {
        // nyala
        lampu1.src = 'on.png'
    }
    if (params == "off") {
        // mati
        lampu1.src = 'off.png'
    }
    return lampu1;
}