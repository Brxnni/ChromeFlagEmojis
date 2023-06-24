let sizeInput = document.getElementById("size");
let marginInput = document.getElementById("margin");
let styleInput = document.getElementById("style");

let previewImg = document.getElementById("preview");

async function readStorage(){
	let storage = await chrome.storage.sync.get();

	sizeInput.value = storage.size;
	marginInput.value = storage.margin;
	styleInput.value = storage.style;
}

function addStyleSelects(){
	for (let [shortName, fullName] of Object.entries(globalThis.styles)){
		let option = document.createElement("option");
		option.value = shortName;
		option.innerHTML = fullName;
		styleInput.appendChild(option);
	}
}

function updatePreview(){
	previewImg.style.setProperty("width", `${sizeInput.value}`, "important");
	previewImg.style.setProperty("margin", `${marginInput.value}`, "important");
	previewImg.setAttribute("src", `./../flags/${styleInput.value}/1f1e9-1f1ea.png`);
}

sizeInput.addEventListener("input", () => {
	chrome.storage.sync.set({ size: sizeInput.value });
	readStorage();
	updatePreview();
});

marginInput.addEventListener("input", () => {
	chrome.storage.sync.set({ margin: marginInput.value });
	readStorage();
	updatePreview();
});

styleInput.addEventListener("input", () => {
	chrome.storage.sync.set({ style: styleInput.value });
	readStorage();
	updatePreview();
});

(async function(){
	addStyleSelects();
	await readStorage();
	updatePreview();
})();
