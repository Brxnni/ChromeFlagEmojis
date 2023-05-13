// Add standard settings when none are there yet
chrome.runtime.onInstalled.addListener(() => {
	chrome.storage.sync.set({
		// These don't do anything yet
		size: "1em",
		margin: "0.1em",
		style: "twitter"
	})
});

// Is called when new tab is opened or switched to
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
	// Is tab fully loaded?
	if (changeInfo.status === "complete"){
		// Execute the content.js script here
	}
});
