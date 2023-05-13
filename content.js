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

	// Js uses UTF16 because it is stupid, so convert the 4 chars (2 per Regional Indicator) to 2 in UTF32
	let c1 = utf16ToUtf32(text.slice(0, 2));
	let c2 = utf16ToUtf32(text.slice(2, 4));

	let src;
	let {style, size, margin} = settings;
	// Get Url for Twimg CDN
	if (
		style === "twitter" ||
		style === "google" ||
		style === "apple" ||
		style === "facebook"
	){
		// Just put the hex value of the chars in there
		// https://www.jsdelivr.com/package/npm/emoji-datasource-apple
		// 💖 Thanks to iamcal for collecting all these together into one nice cdn
		src = `https://projects.iamcal.com/emoji-data/img-${style}-64/${c1.toString(16)}-${c2.toString(16)}.png`
	}
	else if (style === "flat"){
		// Convert to latin characters (RI becomes -> "d" and "e")
		// "a" = 97, "🇦" = 127462, diff = 127365
		src = `https://flagcdn.com/${String.fromCharCode(c1 - 127365)}${String.fromCharCode(c2 - 127365)}.svg`;
	}

	// style="width: ${settings.size}; height: ${settings.size}"
	return `<img
		src="${src}"
		style="
			height: ${size};
			margin: ${margin};
			vertical-align: bottom;
			image-rendering: pixelated;
		"
	/>`.replaceAll(/[\t\n]+/g, " ");
	// Replace tabs and newlines that are caused by me making this more readable instead of having it be a one-liner

}

function replaceRIs(text){
	return text.replaceAll(RIRegex, (match) => {
		return riToImg(match, storage);
	})
}

function replaceNode(node){
	let newText = replaceRIs(node.textContent);

	if (node.textContent !== newText){
		// Replacing innerHTML of node won't work, so you have to make a wrapper element
		let div = document.createElement("div");
		div.innerHTML = newText;
		node.replaceWith(div);
		div.outerHTML = div.innerHTML;
	}
}

function replaceRIsRecursively(element){

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
					replaceNode(node);
					replaceRIsRecursively(node);
				})
			}
        });
    });

	obv.observe(document.body, {
		childList: true,
		subtree: true
	})

})();
