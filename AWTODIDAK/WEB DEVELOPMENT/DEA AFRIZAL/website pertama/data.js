const namaSaya = "rangga putra"
let umur = 20
let biodata=document.getElementById('biodata')
    
console.log(biodata)
console.log(namaSaya+" "+umur)
console.log("umur anda adalah"+" "+umur)
if (umur>=17) {
    console.log("selamat "+ namaSaya +" memenuhi kriteria")
} else {
    console.log("maaf "+namaSaya+" tidak memenuhi kriteria")
}
function generateName() {
    console.log(namaSaya + " " + umur)
    // return biodata innerHtml = umur
}

generateName()
