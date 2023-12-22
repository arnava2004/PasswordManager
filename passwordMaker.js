const digits = [0,1,2,3,4,5,6,7,8,9];
const specialChars = ["!", "?", "@", "#", "$", "%", "^", "&", "*","-", "_", "/"];
const lowerLetters = [...Array(26)].map((_,i) => String.fromCharCode(i + 97));
const upperLetters = lowerLetters.map(letter => letter.toUpperCase());

const charAmountRange = document.getElementById("charAmountRange");
const charAmountNum = document.getElementById("charAmountNum");
const form = document.getElementById("passGeneratorForm");
const UppercaseCheck = document.getElementById("UppercaseCheck");
const NumbersCheck = document.getElementById("NumbersCheck");
const SymbolsCheck = document.getElementById("SymbolsCheck");
const passDisplay = document.getElementById("passDisplay");

const UPPERCASE_CHAR_CODES = arrayFromLowToHigh(65, 90)
const LOWERCASE_CHAR_CODES = arrayFromLowToHigh(97, 122)
const NUMBER_CHAR_CODES = arrayFromLowToHigh(48, 57)
const SYMBOL_CHAR_CODES = arrayFromLowToHigh(33, 47).concat(
  arrayFromLowToHigh(58, 64)
).concat(
  arrayFromLowToHigh(91, 96)
).concat(
  arrayFromLowToHigh(123, 126)
)

charAmountRange.addEventListener("input", syncLength);
charAmountNum.addEventListener("input", syncLength);
form.addEventListener("submit", e => {
    e.preventDefault();
    const charAmount = charAmountNum.value;
    const uppercase = UppercaseCheck.checked; 
    const numbers = NumbersCheck.checked;
    const symbols = SymbolsCheck.checked;
    const password = generatePassword(charAmount, uppercase, numbers, symbols);
    passDisplay.innerText = password;
})

function arrayFromLowToHigh(low, high) {
    const array = []
    for (let i = low; i <= high; i++) {
      array.push(i)
    }
    return array
}

function syncLength(e) {
    const value = e.target.value;
    charAmountRange.value = value;
    charAmountNum.value = value;
}
// Will make range input later, make it changeable
const passwordLength = 15

function generatePassword(characterAmount, includeUppercase, includeNumbers, includeSymbols) {
    let charCodes = LOWERCASE_CHAR_CODES
    if (includeUppercase) charCodes = charCodes.concat(UPPERCASE_CHAR_CODES)
    if (includeSymbols) charCodes = charCodes.concat(SYMBOL_CHAR_CODES)
    if (includeNumbers) charCodes = charCodes.concat(NUMBER_CHAR_CODES)
    
    const passwordCharacters = []
    for (let i = 0; i < characterAmount; i++) {
      const characterCode = charCodes[Math.floor(Math.random() * charCodes.length)]
      passwordCharacters.push(String.fromCharCode(characterCode))
    }
    return passwordCharacters.join('')
}

// Uncomment when range becomes input and password length is mutable
// passwordLength.addEventListener("change", () => { generatePassword();});



