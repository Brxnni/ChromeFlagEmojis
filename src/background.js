// Add standard settings when none are there yet
chrome.runtime.onInstalled.addListener(() => {
	chrome.storage.sync.set({
		size: "1.2em",
		margin: "0 0.075em 0 0.075em",
		style: "twitter"
	});
});
