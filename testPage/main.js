let allSpan;
let updateSpan;
let styleSpan;

let countryCodes = Object.keys(globalThis.cfe_flagNames).map(code => code.split("-").map(c => globalThis.cfe_utf32HexToUtf16(c)).join(""));

function newRandomEmoji(){
	updateSpan.innerHTML = countryCodes[Math.floor(Math.random() * countryCodes.length)];
}

updateSpan = document.getElementById("update");
allSpan = document.getElementById("all");
styleSpan = document.getElementById("style");

allSpan.innerHTML = countryCodes.join(" ");
for (let [styleShortName, styleFullName] of Object.entries(globalThis.cfe_styles)){
	let url = `./../src/flags/${styleShortName}`;
	styleSpan.innerHTML += `${styleFullName}: `
	styleSpan.innerHTML += `<img class="chromeext-emojiflags" style="height: 1.5em !important;" src="${url}/1f1f2-1f1f3.png" title="${styleFullName}"/> `
	styleSpan.innerHTML += `<img class="chromeext-emojiflags" style="height: 1.5em !important;" src="${url}/unknown.png" title="${styleFullName} (Unknown variation)"/><br/>`
}

newRandomEmoji();
