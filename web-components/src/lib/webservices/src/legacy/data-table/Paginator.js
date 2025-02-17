/*
 * Paginator Component
 *
 * This component is used to page through results.
 *
 */

import {
  createElement,
  customElementsMaybeDefine,
  parseElementProps,
} from "../lib/domLib.js";

export default class Paginator extends HTMLElement {
  static makeButton(text, page, start, disabled) {
    const button = createElement("button", {
      // Ensure that type=button to prevent form submission on click.
      type: "button",
      textContent: text,
      disabled: disabled,
    });
    button.setAttribute("page", page);
    button.setAttribute("start", start);
    return button;
  }

  async connectedCallback() {
    this.props = parseElementProps(this, [
      "numTotal",
      "pageSize",
      "currentPage",
    ]);
    const { numTotal, pageSize, currentPage } = this.props;
    const maxPage = Math.max(Math.ceil(numTotal / pageSize), 1);

    // Define the max number of page number button to display on each side
    // of the current page.
    const MAX_NUM_REACHABLE_PAGES = 1;

    // Determine whether we're going to show the first and last page buttons.
    const showFirstPageButton = currentPage > MAX_NUM_REACHABLE_PAGES + 1;
    const showLastPageButton = maxPage - currentPage > MAX_NUM_REACHABLE_PAGES;

    // Define a helper to calculate the 'start' value for a given page number.
    const pageToStart = (pageNum) => pageSize * (pageNum - 1);

    // Add the previous page button.
    this.appendChild(
      Paginator.makeButton("<", currentPage - 1, pageToStart(currentPage - 1), currentPage === 1)
    );

    // Define an Ellipsis element.
    const ellipsisElement = createElement("span", {
      classList: ["position-relative", "mr-1"],
      textContent: "…",
    });
    ellipsisElement.style.top = "0.4em";

    // Maybe add a first page button.
    if (showFirstPageButton) {
      this.appendChild(Paginator.makeButton("1", 1, pageToStart(1)));
      this.appendChild(ellipsisElement.cloneNode(true));
    }

    // Add the adjacent page buttons.
    let pageDelta = -MAX_NUM_REACHABLE_PAGES;
    while (pageDelta <= MAX_NUM_REACHABLE_PAGES) {
      const page = currentPage + pageDelta;
      if (
        page > 0 &&
        (page !== 1 || !showFirstPageButton) &&
        (page !== maxPage || !showLastPageButton) &&
        page <= maxPage
      ) {
        const isCurrentPage = page === currentPage;
        this.appendChild(Paginator.makeButton(page, page, pageToStart(page), isCurrentPage));
      }
      pageDelta += 1;
    }

    // Maybe add a last page button.
    if (showLastPageButton) {
      this.appendChild(ellipsisElement.cloneNode(true));
      this.appendChild(Paginator.makeButton(maxPage, maxPage, pageToStart(maxPage)));
    }

    // Add the next page button.
    this.appendChild(Paginator.makeButton(">", currentPage + 1, pageToStart(currentPage + 1), currentPage === maxPage));
  }
}

customElementsMaybeDefine("paginator-control", Paginator);
