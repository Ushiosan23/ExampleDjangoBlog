class StickyMenu {
	
	/**
	 * This property check if document has a scroll event.
	 *
	 * @type {boolean}
	 */
	static documentAlreadyHasEvent = false;
	
	/**
	 * This property save all sticky menus.
	 *
	 * @type {Array}
	 * @private
	 */
	static __listAllNodeListen = [];
	
	/**
	 * Save delta screen offset y
	 *
	 * @type {number}
	 * @private
	 */
	static __deltaY = 0;
	
	/**
	 * Sticky constructor
	 *
	 * @param node {HTMLElement}
	 * @param showWhenUp {Boolean}
	 * @param paddingBody {Boolean}
	 */
	constructor(node, showWhenUp = false, paddingBody = false) {
		// Save element
		this.element = node;
		// Save showWhenUp property
		this.showWhenUp = showWhenUp;
		// Save padding body property
		this.paddingBody = paddingBody;
		// Offset node
		this.nodeOffset = offset(this.element);
		// Check document mouse wheel
		if (!StickyMenu.documentAlreadyHasEvent) {
			document.addEventListener('scroll', this.__onDocumentWheel, false);
			StickyMenu.documentAlreadyHasEvent = true;
		}
		// Save instance in all elements
		StickyMenu.__listAllNodeListen.push(this);
	}
	
	/**
	 * Create instance of sticky menu but not rerun nothing.
	 *
	 * @param node {HTMLElement}
	 * @param showWhenUp {Boolean}
	 * @param paddingBody {Boolean}
	 */
	static listen(node, showWhenUp = false, paddingBody = false) {
		if (node === null)
			throw new Error("Node cannot be null.");
		new StickyMenu(node, showWhenUp, paddingBody);
	}
	
	/**
	 * Handle scroll document event.
	 *
	 * @param ev {Event}
	 * @private
	 */
	__onDocumentWheel(ev) {
		let distance;
		
		if ((window.scrollY - StickyMenu.__deltaY) > 0) {
			distance = 100;
		} else {
			distance = -100;
		}
		
		StickyMenu.__deltaY = window.scrollY;
		StickyMenu.__listAllNodeListen.forEach(value => {
			value.__configureNode(window.scrollY, distance);
		});
	}
	
	/**
	 * Configure node depends of position.
	 *
	 * @param scrollY {Number}
	 * @param scrollDeltaY {Number}
	 * @private
	 */
	__configureNode(scrollY, scrollDeltaY) {
		if (scrollY > this.nodeOffset.top) {
			if (this.paddingBody) {
				let elementHeight = this.element.clientHeight;
				
				this.element.setData({sticky: ''});
				document.body.css({paddingTop: `${elementHeight}px`});
			}
		} else {
			this.element.removeData('sticky');
			document.body.css({paddingTop: null});
		}
	}
	
}