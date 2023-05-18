function utf16ToUtf32(utf16Chars){
	// Takes to characters in Utf16 and converts them to the hex representation in Utf32
	let highSurrogate = (utf16Chars.charCodeAt(0));
	let lowSurrogate = (utf16Chars.charCodeAt(1));

	// https://en.wikipedia.org/wiki/UTF-16
	let final = ((highSurrogate - 0xD800) * 0x400) + (lowSurrogate - 0xDC00) + 0x10000;
	return final;
}

// Convert Regional Indicator Chars to inline HTML of an <img>.
function riToImg(text, settings){

	let flagName = globalThis.flagNames[text];
	// Js uses UTF16 because it is stupid, so convert the 4 chars (2 per Regional Indicator) to 2 in UTF32
	let char1 = (utf16ToUtf32(text.slice(0, 2))).toString(16);
	let char2 = (utf16ToUtf32(text.slice(2, 4))).toString(16);

	let imgSrc;
	let {style, size, margin} = settings;
	imgSrc = `https://em-content.zobj.net/thumbs/120/${style}/${globalThis.urlNumbers[style]}/flag-${flagName.shortName}_${char1}-${char2}.png`;
	
	return `<img
		src="${imgSrc}"
		title="Flag of ${flagName.fullName}"
		alt="${text}"
		class="chromeext-emojiflags"
		style="
			height: ${size};
			margin: ${margin};
		"
	/>`.replaceAll(/[\t\n]+/g, " ");
	// Replace tabs and newlines that are caused by me making this more readable instead of having it be a one-liner

}

function replaceNode(node){
	let newText = node.textContent.replaceAll(RIRegex, (match) => riToImg(match, storage) );

	if (node.textContent !== newText){
		// Replacing innerHTML of node won't work, so you have to make a wrapper element
		let div = document.createElement("div");
		div.innerHTML = newText;
		node.replaceWith(div);
		div.outerHTML = div.innerHTML;
	}
}

function replaceRIsRecursively(element){
	if (element.nodeType === Node.TEXT_NODE) replaceNode(element);

	for (let node of element.childNodes) {
		switch (node.nodeType) {
			case Node.ELEMENT_NODE || Node.DOCUMENT_NODE:
				replaceRIsRecursively(node);
				break;

			case Node.TEXT_NODE:
				replaceNode(node);
				break;
		}
	}
}

const RIRegex = /[\uD83C][\uDDE6-\uDDFF][\uD83C][\uDDE6-\uDDFF]/g;
let storage;

(async function(){

	storage = await chrome.storage.sync.get();

	// This is false when viewing something thats not html
	if (document.body !== null){
		// Replace entire body to begin with (for static pages)
		replaceRIsRecursively(document.body);
	
		// If any node in the page ever changes, search everything in that node again
		let obv = new MutationObserver((mutations) => {
			mutations.forEach((mutation) => {
				if (
					mutation.type === "childList" ||
					mutation.type === "characterData"
				){
					mutation.addedNodes.forEach((node) => {
						replaceRIsRecursively(node);
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
