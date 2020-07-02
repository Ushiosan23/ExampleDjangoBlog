window.addEventListener('DOMContentLoaded', () => {
	
	/**
	 * Check natural properties image.
	 *
	 * @param img {HTMLImageElement}
	 * @returns {boolean}
	 */
	const checkImageNaturals = img => {
		return img.naturalWidth === undefined ||
			img.naturalWidth === 0 ||
			img.naturalHeight === undefined ||
			img.naturalHeight === 0;
	}
	
	/**
	 * Called when image is loaded.
	 *
	 * @param ev {Event}
	 */
	const configureImageAsync = ev => configure_image(ev.currentTarget);
	
	/**
	 * Configure image size.
	 *
	 * @param img {HTMLImageElement}
	 */
	const configure_image = img => {
		if (checkImageNaturals(img)) {
			img.addEventListener('load', configureImageAsync);
			return;
		}
		
		let width = img.naturalWidth,
			height = img.naturalHeight;
		
		
		// check width
		if (width > height) {
			img.css({height: `105%`});
		} else {
			img.css({width: `105%`});
		}
	}
	
	/**
	 * Configure card height.
	 *
	 * @param card {HTMLElement}
	 */
	const configure_card = card => {
		let img = card.$("img");
		
		card.css({height: `${card.clientWidth}px`});
		configure_image(img);
	};
	
	// Save cards
	let cards = $$(".card.photo_card");
	
	// Iterate all cards
	cards.forEach((card, index) => {
		let img_card = card.$(".card_img");
		configure_card(img_card);
		
		if ((index + 1) % 2 === 0)
			card.setData({'flip': ''});
	});
	
}, false);