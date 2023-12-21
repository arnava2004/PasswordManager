const digits = [0,1,2,3,4,5,6,7,8,9];
const specialChars = ["!", "?", "@", "#", "$", "%", "^", "&", "*","-", "_", "/"];
const lowerLetters = [...Array(26)].map((_,i) => String.fromCharCode(i + 97));
const upperLetters = lowerLetters.map(letter => letter.toUpperCase());


// Will make range input later, make it changeable
const passwordLength = 15

const generatePassword = () => {
    console.log("Password Generated")
}

// Uncomment when range becomes input and password length is mutable
// passwordLength.addEventListener("change", () => { generatePassword();});



