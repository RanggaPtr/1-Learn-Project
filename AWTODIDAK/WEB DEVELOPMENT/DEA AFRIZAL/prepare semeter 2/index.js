// const myName = 'rangga putra'
// const myAdress = 'jalan jonggoll'
let i = 0

// myName = 'rnagga'
// myAdress = 'jalan jonggol'

// console.log(myName)
// console.log(myAdress)
// console.log('pemisahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')

// standart function
function getDetailHuman(data1, data2) {
    i += 1
    // console.log(`data 1 adalah ${data1} dan data 2 adalah ${data2}`)
    if (i > 5) {
        console.log(`function dipakai lebih dari 5x`)
    } else {
        console.log(`function dipakai sebanyak ${i}x`)
    }
}
// arrow function
const getDetailHuman2 = () => {
    i += 1
    i > 5 ? console.log('function dipakai lebih dari 5x') : console.log("jatah masih ada")

}
// getDetailHuman(myName, myAdress)

// objek di javascript
const datas = {
    nama: "rangga putra",
    alamat: "jongool",
    usia: "18",
    pekerjaan: "programmer"
}

console.log(datas)
console.log(datas.nama)
console.log(datas.alamat)

const dataz = [
    {
        nama: "rangga putra",
        alamat: "jongool",
        usia: "18",
        pekerjaan: "programmer"
    },
    {
        nama: " putra",
        alamat: "prob",
        usia: "19",
        pekerjaan: "programmer"
    }
]

function callDataz() {
    dataz.forEach(result => {
        console.log(result)
        console.table(dataz)
    });
    // dataz.map(function (result, i) {
    //     console.table(result)
    // })
    // console.log(`ini adalah sekumpulan data yang di tangkap${dataz}`)

}

class hewan {
    warna
    skill

    constructor(nama) {
        this.nama = nama
    }


    set newWarna(color) {
        this.warna=color
    }

    set newSkill(skill) {
        this.skill=skill
    }

    get detail() {
        return `hi saya ${this.nama} , warna saya ${this.warna} dan keahlian saya adalah ${skill}`
    }
}

const kucing = new hewan('black')
console.log(kucing)

kucing.newWarna = 'biru'
kucing.newSkill = 'ngoding'

console.log(kucing.nama)
console.log(kucing.newWarna)
console.log(kucing.newSkill)

console.log(kucing.detail)