const flagCodeToName = {
	"🇦🇨":"ascension-island",
	"🇦🇩":"andorra",
	"🇦🇪":"united-arab-emirates",
	"🇦🇫":"afghanistan",
	"🇦🇬":"antigua-barbuda",
	"🇦🇮":"anguilla",
	"🇦🇱":"albania",
	"🇦🇲":"armenia",
	"🇦🇴":"angola",
	"🇦🇶":"antarctica",
	"🇦🇷":"argentina",
	"🇦🇸":"american-samoa",
	"🇦🇹":"austria",
	"🇦🇺":"australia",
	"🇦🇼":"aruba",
	"🇦🇽":"aland-islands",
	"🇦🇿":"azerbaijan",
	"🇧🇦":"bosnia-herzegovina",
	"🇧🇧":"barbados",
	"🇧🇩":"bangladesh",
	"🇧🇪":"belgium",
	"🇧🇫":"burkina-faso",
	"🇧🇬":"bulgaria",
	"🇧🇭":"bahrain",
	"🇧🇮":"burundi",
	"🇧🇯":"benin",
	"🇧🇱":"st-barthelemy",
	"🇧🇲":"bermuda",
	"🇧🇳":"brunei",
	"🇧🇴":"bolivia",
	"🇧🇶":"caribbean-netherlands",
	"🇧🇷":"brazil",
	"🇧🇸":"bahamas",
	"🇧🇹":"bhutan",
	"🇧🇻":"bouvet-island",
	"🇧🇼":"botswana",
	"🇧🇾":"belarus",
	"🇧🇿":"belize",
	"🇨🇦":"canada",
	"🇨🇨":"cocos-keeling-islands",
	"🇨🇩":"congo-kinshasa",
	"🇨🇫":"central-african-republic",
	"🇨🇬":"congo-brazzaville",
	"🇨🇭":"switzerland",
	"🇨🇮":"cote-divoire",
	"🇨🇰":"cook-islands",
	"🇨🇱":"chile",
	"🇨🇲":"cameroon",
	"🇨🇳":"china",
	"🇨🇴":"colombia",
	"🇨🇵":"clipperton-island",
	"🇨🇷":"costa-rica",
	"🇨🇺":"cuba",
	"🇨🇻":"cape-verde",
	"🇨🇼":"curacao",
	"🇨🇽":"christmas-island",
	"🇨🇾":"cyprus",
	"🇨🇿":"czechia",
	"🇩🇪":"germany",
	"🇩🇬":"diego-garcia",
	"🇩🇯":"djibouti",
	"🇩🇰":"denmark",
	"🇩🇲":"dominica",
	"🇩🇴":"dominican-republic",
	"🇩🇿":"algeria",
	"🇪🇦":"ceuta-melilla",
	"🇪🇨":"ecuador",
	"🇪🇪":"estonia",
	"🇪🇬":"egypt",
	"🇪🇭":"western-sahara",
	"🇪🇷":"eritrea",
	"🇪🇸":"spain",
	"🇪🇹":"ethiopia",
	"🇪🇺":"european-union",
	"🇫🇮":"finland",
	"🇫🇯":"fiji",
	"🇫🇰":"falkland-islands",
	"🇫🇲":"micronesia",
	"🇫🇴":"faroe-islands",
	"🇫🇷":"france",
	"🇬🇦":"gabon",
	"🇬🇧":"united-kingdom",
	"🇬🇩":"grenada",
	"🇬🇪":"georgia",
	"🇬🇫":"french-guiana",
	"🇬🇬":"guernsey",
	"🇬🇭":"ghana",
	"🇬🇮":"gibraltar",
	"🇬🇱":"greenland",
	"🇬🇲":"gambia",
	"🇬🇳":"guinea",
	"🇬🇵":"guadeloupe",
	"🇬🇶":"equatorial-guinea",
	"🇬🇷":"greece",
	"🇬🇸":"south-georgia-south-sandwich-islands",
	"🇬🇹":"guatemala",
	"🇬🇺":"guam",
	"🇬🇼":"guinea-bissau",
	"🇬🇾":"guyana",
	"🇭🇰":"hong-kong-sar-china",
	"🇭🇲":"heard-mcdonald-islands",
	"🇭🇳":"honduras",
	"🇭🇷":"croatia",
	"🇭🇹":"haiti",
	"🇭🇺":"hungary",
	"🇮🇨":"canary-islands",
	"🇮🇩":"indonesia",
	"🇮🇪":"ireland",
	"🇮🇱":"israel",
	"🇮🇲":"isle-of-man",
	"🇮🇳":"india",
	"🇮🇴":"british-indian-ocean-territory",
	"🇮🇶":"iraq",
	"🇮🇷":"iran",
	"🇮🇸":"iceland",
	"🇮🇹":"italy",
	"🇯🇪":"jersey",
	"🇯🇲":"jamaica",
	"🇯🇴":"jordan",
	"🇯🇵":"japan",
	"🇰🇪":"kenya",
	"🇰🇬":"kyrgyzstan",
	"🇰🇭":"cambodia",
	"🇰🇮":"kiribati",
	"🇰🇲":"comoros",
	"🇰🇳":"st-kitts-nevis",
	"🇰🇵":"north-korea",
	"🇰🇷":"south-korea",
	"🇰🇼":"kuwait",
	"🇰🇾":"cayman-islands",
	"🇰🇿":"kazakhstan",
	"🇱🇦":"laos",
	"🇱🇧":"lebanon",
	"🇱🇨":"st-lucia",
	"🇱🇮":"liechtenstein",
	"🇱🇰":"sri-lanka",
	"🇱🇷":"liberia",
	"🇱🇸":"lesotho",
	"🇱🇹":"lithuania",
	"🇱🇺":"luxembourg",
	"🇱🇻":"latvia",
	"🇱🇾":"libya",
	"🇲🇦":"morocco",
	"🇲🇨":"monaco",
	"🇲🇩":"moldova",
	"🇲🇪":"montenegro",
	"🇲🇫":"st-martin",
	"🇲🇬":"madagascar",
	"🇲🇭":"marshall-islands",
	"🇲🇰":"north-macedonia",
	"🇲🇱":"mali",
	"🇲🇲":"myanmar-burma",
	"🇲🇳":"mongolia",
	"🇲🇴":"macao-sar-china",
	"🇲🇵":"northern-mariana-islands",
	"🇲🇶":"martinique",
	"🇲🇷":"mauritania",
	"🇲🇸":"montserrat",
	"🇲🇹":"malta",
	"🇲🇺":"mauritius",
	"🇲🇻":"maldives",
	"🇲🇼":"malawi",
	"🇲🇽":"mexico",
	"🇲🇾":"malaysia",
	"🇲🇿":"mozambique",
	"🇳🇦":"namibia",
	"🇳🇨":"new-caledonia",
	"🇳🇪":"niger",
	"🇳🇫":"norfolk-island",
	"🇳🇬":"nigeria",
	"🇳🇮":"nicaragua",
	"🇳🇱":"netherlands",
	"🇳🇴":"norway",
	"🇳🇵":"nepal",
	"🇳🇷":"nauru",
	"🇳🇺":"niue",
	"🇳🇿":"new-zealand",
	"🇴🇲":"oman",
	"🇵🇦":"panama",
	"🇵🇪":"peru",
	"🇵🇫":"french-polynesia",
	"🇵🇬":"papua-new-guinea",
	"🇵🇭":"philippines",
	"🇵🇰":"pakistan",
	"🇵🇱":"poland",
	"🇵🇲":"st-pierre-miquelon",
	"🇵🇳":"pitcairn-islands",
	"🇵🇷":"puerto-rico",
	"🇵🇸":"palestinian-territories",
	"🇵🇹":"portugal",
	"🇵🇼":"palau",
	"🇵🇾":"paraguay",
	"🇶🇦":"qatar",
	"🇷🇪":"reunion",
	"🇷🇴":"romania",
	"🇷🇸":"serbia",
	"🇷🇺":"russia",
	"🇷🇼":"rwanda",
	"🇸🇦":"saudi-arabia",
	"🇸🇧":"solomon-islands",
	"🇸🇨":"seychelles",
	"🇸🇩":"sudan",
	"🇸🇪":"sweden",
	"🇸🇬":"singapore",
	"🇸🇭":"st-helena",
	"🇸🇮":"slovenia",
	"🇸🇯":"svalbard-jan-mayen",
	"🇸🇰":"slovakia",
	"🇸🇱":"sierra-leone",
	"🇸🇲":"san-marino",
	"🇸🇳":"senegal",
	"🇸🇴":"somalia",
	"🇸🇷":"suriname",
	"🇸🇸":"south-sudan",
	"🇸🇹":"sao-tome-principe",
	"🇸🇻":"el-salvador",
	"🇸🇽":"sint-maarten",
	"🇸🇾":"syria",
	"🇸🇿":"eswatini",
	"🇹🇦":"tristan-da-cunha",
	"🇹🇨":"turks-caicos-islands",
	"🇹🇩":"chad",
	"🇹🇫":"french-southern-territories",
	"🇹🇬":"togo",
	"🇹🇭":"thailand",
	"🇹🇯":"tajikistan",
	"🇹🇰":"tokelau",
	"🇹🇱":"timor-leste",
	"🇹🇲":"turkmenistan",
	"🇹🇳":"tunisia",
	"🇹🇴":"tonga",
	"🇹🇷":"turkey",
	"🇹🇹":"trinidad-tobago",
	"🇹🇻":"tuvalu",
	"🇹🇼":"taiwan",
	"🇹🇿":"tanzania",
	"🇺🇦":"ukraine",
	"🇺🇬":"uganda",
	"🇺🇲":"us-outlying-islands",
	"🇺🇳":"united-nations",
	"🇺🇸":"united-states",
	"🇺🇾":"uruguay",
	"🇺🇿":"uzbekistan",
	"🇻🇦":"vatican-city",
	"🇻🇨":"st-vincent-grenadines",
	"🇻🇪":"venezuela",
	"🇻🇬":"british-virgin-islands",
	"🇻🇮":"us-virgin-islands",
	"🇻🇳":"vietnam",
	"🇻🇺":"vanuatu",
	"🇼🇫":"wallis-futuna",
	"🇼🇸":"samoa",
	"🇽🇰":"kosovo",
	"🇾🇪":"yemen",
	"🇾🇹":"mayotte",
	"🇿🇦":"south-africa",
	"🇿🇲":"zambia",
	"🇿🇼":"zimbabwe"
}

const urlNums = {
	"apple": "354",
	"google": "350",
	"samsung": "349",
	"whatsapp": "352",
	"twitter": "322",
	"facebook": "355",
	"openmoji": "338"
}

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

	let flagName = flagCodeToName[text];
	// Js uses UTF16 because it is stupid, so convert the 4 chars (2 per Regional Indicator) to 2 in UTF32
	let char1 = (utf16ToUtf32(text.slice(0, 2))).toString(16);
	let char2 = (utf16ToUtf32(text.slice(2, 4))).toString(16);

	let imgSrc;
	let {style, size, margin} = settings;
	imgSrc = `https://em-content.zobj.net/thumbs/120/${style}/${urlNums[style]}/flag-${flagName}_${char1}-${char2}.png`;
	
	return `<img
		src="${imgSrc}"
		alt="flag of ${flagName}"
		style="
			height: ${size};
			margin: ${margin};
			vertical-align: bottom;
			-webkit-user-drag: none;
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
