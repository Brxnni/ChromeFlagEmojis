function utf32HexToUtf16(hex32){
	hex32 = parseInt(hex32, 16);

	let highSurrogate = Math.floor((hex32 - 0x10000) / 0x400) + 0xD800;
	let lowSurrogate = ((hex32 - 0x10000) % 0x400) + 0xDC00;

	return String.fromCharCode(highSurrogate) + String.fromCharCode(lowSurrogate);
}

let allSpan;
let updateSpan;
let styleSpan;

let countryCodes = Object.keys(globalThis.flagNames).map(code => code.split("-").map(c => utf32HexToUtf16(c)).join(""));

let styles = [
	"apple",
	"google",
	"samsung",
	"whatsapp",
	"twitter",
	"facebook",
	"openmoji"
];
let urls = {};
for (let style of styles){
	urls[style] = `./../src/flags/${style}/1f1f2-1f1f3.png`;
}

function newRandomEmoji(){
	updateSpan.innerHTML = countryCodes[Math.floor(Math.random() * countryCodes.length)];
}

updateSpan = document.getElementById("update");
allSpan = document.getElementById("all");
styleSpan = document.getElementById("style");

allSpan.innerHTML = countryCodes.join(" ");
for (let [style, url] of Object.entries(urls)){
	styleSpan.innerHTML += `<img class="chromeext-emojiflags" src="${url}" title="${style}"/>`
}

newRandomEmoji();
