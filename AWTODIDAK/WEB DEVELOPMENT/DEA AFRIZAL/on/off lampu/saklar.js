// function saklar(action, lamp) {
//     console.log(action);
//     console.log("Your lamp " + lamp + " is " + action);
//     let lampu1 = document.getElementById('lampu1');
//     let lampu2 = document.getElementById('lampu2');
//     let lampu3 = document.getElementById('lampu3');

//     if (action == "on") {
//         // nyala
//         if (lamp == 1) {
//             lampu1.src = 'on.png';
//         } else if (lamp == 2) {
//             lampu2.src = 'on.png';
//         } else {
//             lampu3.src = 'on.png';
//         }
//     } else if (action == "off") {
//         // mati
//         if (lamp == 1) {
//             lampu1.src = 'off.png';
//         } else if (lamp == 2) {
//             lampu2.src = 'off.png';
//         } else {
//             lampu3.src = 'off.png';
//         }
//     }

//     return lampu1;
// }
function saklar(action, lamp) {
    console.log(action);
    console.log("Your lamp " + lamp + " is " + action);
    let lampu1 = document.getElementById('lampu1');
    let lampu2 = document.getElementById('lampu2');
    let lampu3 = document.getElementById('lampu3');

    if (action == "on") {
        // nyala
        if (lamp == 1) {
            lampu1.src = 'on.png';
            document.getElementById('toggle1').checked = true;
        } else if (lamp == 2) {
            lampu2.src = 'on.png';
            document.getElementById('toggle2').checked = true;
        } else {
            lampu3.src = 'on.png';
            document.getElementById('toggle3').checked = true;
        }
    } else if (action == "off") {
        // mati
        if (lamp == 1) {
            lampu1.src = 'off.png';
            document.getElementById('toggle1').checked = false;
        } else if (lamp == 2) {
            lampu2.src = 'off.png';
            document.getElementById('toggle2').checked = false;
        } else {
            lampu3.src = 'off.png';
            document.getElementById('toggle3').checked = false;
        }
    }
}

function toggleLamp(lamp) {
    let lampu = document.getElementById('lampu' + lamp);
    let toggle = document.getElementById('toggle' + lamp);

    if (toggle.checked) {
        lampu.src = 'on.png';
        console.log("Your lamp " + lamp + " is on");
    } else {
        lampu.src = 'off.png';
        console.log("Your lamp " + lamp + " is off");
    }
}
