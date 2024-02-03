const http = require('http')
const rupiah = require("rupiah-format")

const host = "127.0.0.1"
const port = 3002

const server = http.createServer(function (request, response) {

    const nama = "rangga putra"
    let uang = "100000"
    let jajan = "50000"
    let sisa = uang - jajan

    uang = rupiah.convert(uang)
    jajan = rupiah.convert(jajan)
    sisa = rupiah.convert(sisa)

    const hasil = "halo nama saya " + nama + "tadi saya membawa uang " + uang + " dan saya jajan " + jajan + " dan uang ku bersisa " + sisa


    response.statusCode = 200
    response.end(hasil)
})

server.listen(port, host, null, function () {
    console.log("server on : " + host + ":" + port)
})




// const namaSaya = "rangga putra"

// function getName() {
//     for (let i = 0; i < 100; i++){
//         console.log("nama saya adalah"+namaSaya)

//     }
// }

// getName()

// create server |request data masuk|response data keluar