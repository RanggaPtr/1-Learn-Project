let passwordLength = document.getElementById('passwordLength')
let password = document.getElementById('password')
let buttonSave = document.getElementById('buttonSave')


function generatePassword(length) {
    const lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
    const upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    const numerik = "0123456789"
    const symbol = "!@#$%^&*()_+=-[]~.,<>;:'|"

    const data = lowerAlphabet + upperAlphabet + numerik + symbol
    let generator = ""

    for (let index = 0; index < length; index++) {
        generator += data[Math.floor(Math.random() * data.length)]
    }
    // console.log("result of generating :" + generator)
    return generator
}

function getPassword() {
    const newPassword = generatePassword(passwordLength.value)
    password.value = newPassword
    setTimeout(() => {
        alert('password has been generated!!!')
    }, 100);
}

function savePassword() {
    // mengganti title web menggunakan value of password
    document.title = password.value

    // auto download password
    buttonSave.setAttribute('href', 'data:text/plain;charset=utf-8,' +encodeURIComponent(`password saya :  ${document.title}`))
    buttonSave.setAttribute('download', 'myPasswordGeneratorLog.txt')

    // copy ke clipboard
    navigator.clipboard.writeText(password.value)
    setTimeout(() => {
        alert('password already saved')
    }, 500);
}

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    body.classList.toggle("dark")
}