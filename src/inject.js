function reloadImg(img){
	setTimeout((img) => {
		img.src = img.src;
		img.onerror = () => {};
	}, 1000, img)
}
