let allSpan;
let updateSpan;
let styleTable;

let countryCodes = Object.keys(globalThis.cfe_flagNames).map(code => code.split("-").map(c => globalThis.cfe_utf32HexToUtf16(c)).join(""));

function newRandomEmoji(){
	updateSpan.innerHTML = countryCodes[Math.floor(Math.random() * countryCodes.length)];
}

updateSpan = document.getElementById("update");
allSpan = document.getElementById("all");
styleTable = document.getElementById("style");

allSpan.innerHTML = countryCodes.join(" ");

for (let [styleShortName, styleFullName] of Object.entries(globalThis.cfe_styles)){
	let url = `./../src`;
	let fileType = globalThis.cfe_fileTypes[styleShortName];

	let tr = document.createElement("tr");
	
	let tdName = document.createElement("td");
	tdName.innerHTML = styleFullName;
	let tdFlagRegular = document.createElement("td");
	tdFlagRegular.innerHTML = `<img class="chromeext-emojiflags" style="height: 1.5em !important;" src="${url}/flags/${styleShortName}/1f1f2-1f1f3.${fileType}" title="${styleFullName}"/>`;
	let tdFlagUnknown = document.createElement("td");
	tdFlagUnknown.innerHTML = `<img class="chromeext-emojiflags" style="height: 1.5em !important;" src="${url}/flags/unknown/${styleShortName}.png" title="${styleFullName} (Unknown variation)"/>`;

	tr.appendChild(tdName);
	tr.appendChild(tdFlagRegular);
	tr.appendChild(tdFlagUnknown);

	styleTable.appendChild(tr);

}

newRandomEmoji();
