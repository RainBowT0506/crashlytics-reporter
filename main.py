from bs4 import BeautifulSoup

# 你提供的HTML内容
html = """
<table
    _ngcontent-ng-c1685953515=""
    ngskiphydration=""
    mat-table=""
    aria-labelledby="issues-table-label"
    role="grid"
    matsort=""
    matsortstart="desc"
    matsortdirection="desc"
    matsortdisableclear="true"
    class="mat-mdc-table mdc-data-table__table cdk-table mat-sort c9s-issues-table captionsV2 fire-table"
>
    <tbody role="rowgroup" class="mdc-data-table__content">
        <tr
            _ngcontent-ng-c1685953515=""
            role="row"
            mat-row=""
            class="mat-mdc-row mdc-data-table__row cdk-row fire-table-row data-row ng-star-inserted"
        >
            <td
                _ngcontent-ng-c1685953515=""
                mat-cell=""
                class="mat-mdc-cell mdc-data-table__cell cdk-cell cdk-column-issueCheckbox mat-column-issueCheckbox ng-star-inserted"
                role="gridcell"
            >
                <mat-checkbox
                    _ngcontent-ng-c1685953515=""
                    firefocusmanageritem=""
                    class="mat-mdc-checkbox issue-checkbox mat-accent ng-star-inserted"
                    id="mat-mdc-checkbox-53"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-53-input"
                                tabindex="0"
                                aria-label="Toggle issue selection"
                            />
                            <div class="mdc-checkbox__ripple"></div>
                            <div class="mdc-checkbox__background">
                                <svg
                                    focusable="false"
                                    viewBox="0 0 24 24"
                                    aria-hidden="true"
                                    class="mdc-checkbox__checkmark"
                                >
                                    <path
                                        fill="none"
                                        d="M1.73,12.91 8.1,19.28 22.79,4.59"
                                        class="mdc-checkbox__checkmark-path"
                                    ></path>
                                </svg>
                                <div class="mdc-checkbox__mixedmark"></div>
                            </div>
                            <div
                                mat-ripple=""
                                class="mat-ripple mat-mdc-checkbox-ripple mat-mdc-focus-indicator"
                            ></div>
                        </div>
                        <label
                            class="mdc-label"
                            for="mat-mdc-checkbox-53-input"
                        ></label></div></mat-checkbox
                ><!---->
            </td>
            <td
                _ngcontent-ng-c1685953515=""
                mat-cell=""
                class="mat-mdc-cell mdc-data-table__cell cdk-cell issue-title cdk-column-issue mat-column-issue ng-star-inserted"
                role="gridcell"
            >
                <a
                    _ngcontent-ng-c1685953515=""
                    firefocusmanageritem=""
                    draggable="false"
                    class="fire-router-link-host link-wrapper"
                    href="#"
                    style="cursor: pointer"
                    ><issue-caption-table-cell
                        _ngcontent-ng-c1685953515=""
                        data-test-id="issue-caption-table-cell"
                        _nghost-ng-c129725039=""
                        ><div
                            _ngcontent-ng-c129725039=""
                            class="caption-table-cell ng-star-inserted"
                        >
                            <c9s-issue-caption-metadata-row
                                _ngcontent-ng-c129725039=""
                                data-test-id="metadataWrapper"
                                _nghost-ng-c3846189135=""
                                ><div
                                    _ngcontent-ng-c3846189135=""
                                    class="row-wrapper"
                                >
                                    <div
                                        _ngcontent-ng-c3846189135=""
                                        data-test-id="eventTypeWrapper"
                                        class="event-type-wrapper ng-star-inserted"
                                    >
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger event-type-tooltip-target"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
                                            aria-describedby="cdk-describedby-message-ng-1-14"
                                            cdk-describedby-host="ng-1"
                                        >
                                            <mat-icon
                                                _ngcontent-ng-c3846189135=""
                                                role="img"
                                                class="mat-icon notranslate 崩溃-icon material-icons mat-ligature-font mat-icon-no-color"
                                                aria-hidden="true"
                                                data-mat-icon-type="font"
                                            >
                                                cancel </mat-icon
                                            ><span
                                                _ngcontent-ng-c3846189135=""
                                                class="event-type-text"
                                            >
                                                崩溃
                                            </span>
                                        </div>
                                        <!----><fire-cdk-popover
                                            _ngcontent-ng-c3846189135=""
                                            _nghost-ng-c3591672751=""
                                            ><!----></fire-cdk-popover
                                        ><mat-divider
                                            _ngcontent-ng-c3846189135=""
                                            role="separator"
                                            class="mat-divider mat-divider-vertical ng-star-inserted"
                                            aria-orientation="vertical"
                                        ></mat-divider
                                        ><!---->
                                    </div>
                                    <!---->
                                    <div
                                        _ngcontent-ng-c3846189135=""
                                        data-test-id="captionDataWrapper"
                                        class="caption-metadata-wrapper ng-star-inserted"
                                    >
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedPackageWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
                                            aria-describedby="cdk-describedby-message-ng-1-15"
                                            cdk-describedby-host="ng-1"
                                        >
                                            <mat-icon
                                                _ngcontent-ng-c3846189135=""
                                                role="img"
                                                fontset="google-material-icons"
                                                class="mat-icon notranslate metadata-icons google-material-icons mat-icon-no-color"
                                                aria-hidden="true"
                                                data-mat-icon-type="font"
                                                data-mat-icon-namespace="google-material-icons"
                                            >
                                                sdk </mat-icon
                                            ><span
                                                _ngcontent-ng-c3846189135=""
                                                class="copy-target"
                                                >com.citysuper.eshop</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
                                            aria-describedby="cdk-describedby-message-ng-1-16"
                                            cdk-describedby-host="ng-1"
                                        >
                                            <mat-icon
                                                _ngcontent-ng-c3846189135=""
                                                role="img"
                                                fontset="google-material-icons"
                                                class="mat-icon notranslate metadata-icons google-material-icons mat-icon-no-color"
                                                aria-hidden="true"
                                                data-mat-icon-type="font"
                                                data-mat-icon-namespace="google-material-icons"
                                            >
                                                insert_drive_file </mat-icon
                                            ><span
                                                _ngcontent-ng-c3846189135=""
                                                class="copy-target"
                                                >SplashActivity.kt:231</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><c9s-issue-tags
                                        _ngcontent-ng-c3846189135=""
                                        data-test-id="signals"
                                        _nghost-ng-c3492471496=""
                                        aria-label="有多个问题信号"
                                        class="ng-star-inserted"
                                        ><div
                                            _ngcontent-ng-c3492471496=""
                                            class="c9s-issue-tags ng-star-inserted"
                                        >
                                            <fire-chip
                                                _ngcontent-ng-c3492471496=""
                                                tabindex="0"
                                                class="signal-chip fire-popover-trigger is-early is-size__dense is-hairline ng-star-inserted"
                                                _nghost-ng-c115418348=""
                                                style="
                                                    --__fire-chip-bg-color: var(
                                                        --theme-color-bg
                                                    );
                                                    --__fire-chip-color: var(
                                                        --theme-color-fg-secondary
                                                    );
                                                "
                                                aria-describedby="fbc_o"
                                                aria-owns="fbc_o"
                                                ><div
                                                    _ngcontent-ng-c115418348=""
                                                    data-fire-popup-overlay-trigger=""
                                                    class="chip-content"
                                                >
                                                    <mat-icon
                                                        _ngcontent-ng-c3492471496=""
                                                        role="img"
                                                        class="mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color"
                                                        aria-hidden="true"
                                                        data-mat-icon-type="font"
                                                        >bolt</mat-icon
                                                    >
                                                    早期 崩溃
                                                </div>
                                                <!----></fire-chip
                                            >
                                            <div
                                                class="cdk-visually-hidden"
                                                aria-hidden="true"
                                                tabindex="0"
                                                data-focusinliner="true"
                                            ></div>
                                            <!----><fire-cdk-popover
                                                _ngcontent-ng-c3492471496=""
                                                _nghost-ng-c3591672751=""
                                                class="ng-star-inserted"
                                                ><!----></fire-cdk-popover
                                            ><!----><fire-chip
                                                _ngcontent-ng-c3492471496=""
                                                tabindex="0"
                                                class="signal-chip fire-popover-trigger is-repetitive is-size__dense is-hairline ng-star-inserted"
                                                _nghost-ng-c115418348=""
                                                style="
                                                    --__fire-chip-bg-color: var(
                                                        --theme-color-bg
                                                    );
                                                    --__fire-chip-color: var(
                                                        --theme-color-fg-secondary
                                                    );
                                                "
                                                aria-describedby="fbc_p"
                                                aria-owns="fbc_p"
                                                ><div
                                                    _ngcontent-ng-c115418348=""
                                                    data-fire-popup-overlay-trigger=""
                                                    class="chip-content"
                                                >
                                                    <mat-icon
                                                        _ngcontent-ng-c3492471496=""
                                                        role="img"
                                                        class="mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color"
                                                        aria-hidden="true"
                                                        data-mat-icon-type="font"
                                                        >loop</mat-icon
                                                    >
                                                    重复 崩溃
                                                </div>
                                                <!----></fire-chip
                                            >
                                            <div
                                                class="cdk-visually-hidden"
                                                aria-hidden="true"
                                                tabindex="0"
                                                data-focusinliner="true"
                                            ></div>
                                            <!----><fire-cdk-popover
                                                _ngcontent-ng-c3492471496=""
                                                _nghost-ng-c3591672751=""
                                                class="ng-star-inserted"
                                                ><!----></fire-cdk-popover
                                            ><!----><!---->
                                        </div>
                                        <!----></c9s-issue-tags
                                    ><!---->
                                </div></c9s-issue-caption-metadata-row
                            >
                            <div
                                _ngcontent-ng-c129725039=""
                                data-test-id="titleWrapper"
                                class="title-wrapper"
                            >
                                <span
                                    _ngcontent-ng-c129725039=""
                                    class="copy-target"
                                    >SplashActivity.notifications</span
                                >
                            </div>
                            <div
                                _ngcontent-ng-c129725039=""
                                data-test-id="subtitleWrapper"
                                class="subtitle-wrapper ng-star-inserted"
                            >
                                <span
                                    _ngcontent-ng-c129725039=""
                                    class="copy-target"
                                    >java.lang.IllegalArgumentException - No
                                    suitable parent found from the given view.
                                    Please provide a valid view.</span
                                >
                            </div>
                            <!----><!---->
                        </div>
                        <!----></issue-caption-table-cell
                    ><!---->
                    <div
                        _ngcontent-ng-c1685953515=""
                        class="mobile-stats show-at-mobile"
                    >
                        <span _ngcontent-ng-c1685953515="">190 次崩溃</span
                        >&nbsp;
                        <span _ngcontent-ng-c1685953515="">16 个用户</span>
                    </div></a
                >
            </td>
            <td
                _ngcontent-ng-c1685953515=""
                mat-cell=""
                class="mat-mdc-cell mdc-data-table__cell cdk-cell hide-at-mobile cdk-column-versions mat-column-versions ng-star-inserted"
                role="gridcell"
            >
                <a
                    _ngcontent-ng-c1685953515=""
                    firefocusmanageritem=""
                    draggable="false"
                    class="fire-router-link-host link-wrapper"
                    href="#"
                    style="cursor: pointer"
                    ><!----><!----><span
                        _ngcontent-ng-c1685953515=""
                        class="mat-mdc-tooltip-trigger version-range"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                        aria-describedby="cdk-describedby-message-ng-1-35"
                        cdk-describedby-host="ng-1"
                    >
                        1.8.0 – 1.7.0 </span
                    ><!---->
                    <div
                        _ngcontent-ng-c1685953515=""
                        class="issue-notes-count ng-star-inserted"
                    >
                        1 个备注
                    </div>
                    <!----></a
                >
            </td>
            <td
                _ngcontent-ng-c1685953515=""
                mat-cell=""
                class="mat-mdc-cell mdc-data-table__cell cdk-cell events hide-at-mobile cdk-column-eventCount mat-column-eventCount ng-star-inserted"
                role="gridcell"
            >
                <a
                    _ngcontent-ng-c1685953515=""
                    firefocusmanageritem=""
                    class="fire-router-link-host link-wrapper ng-star-inserted"
                    href="#"
                    style="cursor: pointer"
                >
                    190 </a
                ><!---->
            </td>
            <td
                _ngcontent-ng-c1685953515=""
                mat-cell=""
                class="mat-mdc-cell mdc-data-table__cell cdk-cell users hide-at-mobile cdk-column-userCount mat-column-userCount ng-star-inserted"
                role="gridcell"
            >
                <a
                    _ngcontent-ng-c1685953515=""
                    firefocusmanageritem=""
                    class="fire-router-link-host link-wrapper ng-star-inserted"
                    href="#"
                    style="cursor: pointer"
                >
                    16 </a
                ><!---->
            </td>
            <!---->
        </tr>
    </tbody>
</table>
"""

# 使用lxml解析器解析HTML
soup = BeautifulSoup(html, 'lxml')

# 找到所有的<tr>标签
table = soup.find('table')
rows = table.find_all('tr')

# 遍历每个<tr>标签并提取内容
for row in rows:
    # cells = row.find_all('td')  # 如果你想提取<td>元素的值
    # specific_div = row.find('div', class_="title-wrapper")
    div_title_wrapper = row.find('div', {'class': 'title-wrapper'})
    if div_title_wrapper is not None:
        title_text = div_title_wrapper.get_text(strip=True)
        print(title_text)

