// Add standard settings when none are there yet
chrome.runtime.onInstalled.addListener(() => {
	chrome.storage.sync.set({
		// These don't do anything yet
		size: "1.2em",
		margin: "0 0.2em 0 0.15em",
		style: "twitter"
	})
});
