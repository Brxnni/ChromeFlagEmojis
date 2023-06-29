// Add standard settings when none are there yet
chrome.runtime.onInstalled.addListener(async () => {
	let storage = await chrome.storage.sync.get();
	if (!storage.margin) chrome.storage.sync.set({ margin: "0 0 0.075em 0 0.075em" });
	if (!storage.size) chrome.storage.sync.set({ size: "1.2em" });
	if (!storage.style) chrome.storage.sync.set({ style: "twitter" });
});
