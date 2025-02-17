import { PropertyValues } from "lit";
import { customElement, state } from "lit/decorators.js";

import { AitDataTable } from "../../lib/webservices/src/aitDataTable/index";

import API from "../../lib/ait-data-table-api-adapter";
import Styles from "./styles";

import { ArchLoadingIndicator } from "../../archLoadingIndicator/index";
import { ArchHoverTooltip } from "../../archHoverTooltip/index";

@customElement("arch-data-table")
export class ArchDataTable<RowT> extends AitDataTable<RowT> {
  @state() columnNameHeaderTooltipMap: Record<string, string> = {};

  // Apply any ARCH-specific styles.
  static styles = [...AitDataTable.styles, ...Styles];

  constructor() {
    super();
    this.apiFactory = API;
    this.loadingMessage = new ArchLoadingIndicator();
    this.pageLength = 50;
  }

  addHeaderTooltip(headerName: string, text: string) {
    const headerTr = this.dataTable.querySelector(
      "thead > tr"
    ) as HTMLTableRowElement;
    const el = headerTr.querySelector(
      `th.${headerName} > button`
    ) as HTMLButtonElement;
    if (!el) {
      console.warn(`Could not add tooltip to header: ${headerName}`);
      return;
    }
    const tooltip = new ArchHoverTooltip();
    tooltip.text = text;
    tooltip.textContent = el.textContent;
    tooltip.style.display = "inline-block";
    tooltip.style.color = "#fff";
    el.replaceChildren(tooltip);
  }

  firstUpdated(_changedProperties: PropertyValues) {
    super.firstUpdated(_changedProperties);
    // Add hover tooltips after DataTable has been rendered.
    for (const [columnName, text] of Object.entries(
      this.columnNameHeaderTooltipMap
    )) {
      this.addHeaderTooltip(columnName, text);
    }
  }
}
