let sizeInput = document.getElementById("size");
let marginInput = document.getElementById("margin");
let styleInput = document.getElementById("style");

async function readStorage(){
	let storage = await chrome.storage.sync.get();

	sizeInput.value = storage.size;
	marginInput.value = storage.margin;
	styleInput.value = storage.style;
}

sizeInput.addEventListener("input", () => {
	chrome.storage.sync.set({ size: sizeInput.value })
});

marginInput.addEventListener("input", () => {
	chrome.storage.sync.set({ margin: marginInput.value })
});

styleInput.addEventListener("input", () => {
	chrome.storage.sync.set({ style: styleInput.value })
});

readStorage();
