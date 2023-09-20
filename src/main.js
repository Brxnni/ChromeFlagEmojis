// Convert Unicode to inline HTML of an <img>.
async function unicodeToImg(text){
	// Js uses UTF16 because it is stupid, so convert the chars to pairs UTF32
	let utf16CharPairs = text.match(/.{1,2}/g).map(globalThis.cfe_utf16ToUtf32Hex);
	let utf32Chars = utf16CharPairs.join("-");
	let flagName = globalThis.cfe_flagNames[utf32Chars];

	// If flag is not supported, return original text so nothing changes
	if (flagName === undefined) return text;

	let {style, size, margin} = storage;

	let imgSrc;
	let title;
	
	if (globalThis.cfe_supportedFlags[style].includes(utf32Chars)){
		let fileType = globalThis.cfe_fileTypes[style];
		imgSrc = chrome.runtime.getURL(`flags/${style}/${utf32Chars}.${fileType}`);
		title = `Flag of ${flagName}`;
	// If file is not supported by the selected style, use the `unknown` image variant
	} else {
		imgSrc = chrome.runtime.getURL(`flags/unknown/${style}.png`);
		let styleName = globalThis.cfe_styles[style];
		title = `Flag of ${flagName} (Not supported by ${styleName})`;
	}

	return `<img
		src="${imgSrc}"
		onerror="reloadImg(this)"
		title="${title}"
		alt="${text}"
		class="chromeext-emojiflags"
		style="
			height: ${size} !important;
			margin: ${margin} !important;
		"
	/>`.replaceAll(/[\t\n]+/g, " ");
	// Replace tabs and newlines that are caused by me making this more readable instead of having it be a one-liner
}

async function replaceNode(node){
	let matches = node.textContent.match(globalThis.cfe_regexGeneralFlag);
	if (matches){
		// Replace content
		let newText = await globalThis.cfe_replaceAllAsync(node.textContent, globalThis.cfe_regexGeneralFlag, unicodeToImg);
		// Without this, a text node would replace itself with its original content, causing a mutation,
		// Causing it to check the node again => infinite loop
		if (newText === node.textContent) return;
		// Replacing innerHTML of node won't work, so you have to make a wrapper element
		let div = document.createElement("div");
		div.innerHTML = newText;
		node.replaceWith(div);
	}
}

function replaceNodeTree(element){

	if (cfe_ignoreNode(element)) return;
	if (element.nodeType === Node.TEXT_NODE) replaceNode(element);

	for (let node of element.childNodes) {
		switch (node.nodeType) {
			case Node.ELEMENT_NODE || Node.DOCUMENT_NODE:
				replaceNodeTree(node);
				break;

			case Node.TEXT_NODE:
				replaceNode(node);
				break;
		}
	}
}

let storage;

(async function(){

	storage = await chrome.storage.sync.get();

	// This is false when viewing something thats not html
	if (document.body !== null){
		// Replace entire body to begin with (for static pages)
		replaceNodeTree(document.body);
	
		// If any node in the page ever changes, search everything in that node again
		let obv = new MutationObserver((mutations) => {
			mutations.forEach((mutation) => {
				if (
					mutation.type === "childList" ||
					mutation.type === "characterData"
				){
					mutation.addedNodes.forEach((node) => {
						replaceNodeTree(node);
					})
				}
			});
		});

		obv.observe(document.body, {
			childList: true,
			subtree: true
		})
	}

})();
