let allSpan;
let updateSpan;
let styleSpan;

let countryCodes = Object.keys(globalThis.flagNames).map(code => code.split("-").map(c => globalThis.utf32HexToUtf16(c)).join(""));

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
