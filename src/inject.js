function reloadImg(img){
	setTimeout((img) => {
		img.src = img.src;
		// Remove onerror so that it only reloads once
		// and doesn't waste resources
		img.onerror = () => {};
	}, 1000, img);
}
