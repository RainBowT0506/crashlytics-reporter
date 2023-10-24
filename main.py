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
    <thead role="rowgroup">
        <tr
            _ngcontent-ng-c1685953515=""
            role="row"
            mat-header-row=""
            class="mat-mdc-header-row mdc-data-table__header-row cdk-header-row fire-table-row ng-star-inserted"
        >
            <th
                _ngcontent-ng-c1685953515=""
                role="columnheader"
                mat-header-cell=""
                class="mat-mdc-header-cell mdc-data-table__header-cell cdk-header-cell cdk-column-issueCheckbox mat-column-issueCheckbox ng-star-inserted"
            >
                <mat-checkbox
                    _ngcontent-ng-c1685953515=""
                    firefocusmanageritem=""
                    class="mat-mdc-checkbox issue-checkbox all-checkbox mat-accent ng-star-inserted"
                    id="mat-mdc-checkbox-190"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-190-input"
                                tabindex="0"
                                aria-label="Toggle selection of all issues"
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
                            for="mat-mdc-checkbox-190-input"
                        ></label></div></mat-checkbox
                ><!---->
            </th>
            <th
                _ngcontent-ng-c1685953515=""
                role="columnheader"
                mat-header-cell=""
                class="mat-mdc-header-cell mdc-data-table__header-cell cdk-header-cell cdk-column-issue mat-column-issue ng-star-inserted"
            >
                <span _ngcontent-ng-c1685953515="">问题</span>
            </th>
            <th
                _ngcontent-ng-c1685953515=""
                role="columnheader"
                mat-header-cell=""
                class="mat-mdc-header-cell mdc-data-table__header-cell cdk-header-cell hide-at-mobile cdk-column-versions mat-column-versions ng-star-inserted"
            >
                版本
            </th>
            <th
                _ngcontent-ng-c1685953515=""
                role="columnheader"
                mat-header-cell=""
                aria-sort="descending"
                aria-label="事件计数"
                mat-sort-header=""
                class="mat-sort-header mat-mdc-header-cell mdc-data-table__header-cell cdk-header-cell hide-at-mobile ng-tns-c1267148319-52 cdk-column-eventCount mat-column-eventCount mat-sort-header-disabled ng-star-inserted"
            >
                <div
                    class="mat-sort-header-container mat-focus-indicator ng-tns-c1267148319-52 mat-sort-header-sorted"
                    aria-describedby="cdk-describedby-message-ng-1-8"
                    cdk-describedby-host="ng-1"
                >
                    <div class="mat-sort-header-content ng-tns-c1267148319-52">
                        事件
                    </div>
                    <div
                        class="mat-sort-header-arrow ng-trigger ng-trigger-arrowPosition ng-tns-c1267148319-52 ng-star-inserted"
                        style="transform: translateY(0px); opacity: 1"
                    >
                        <div
                            class="mat-sort-header-stem ng-tns-c1267148319-52"
                        ></div>
                        <div
                            class="mat-sort-header-indicator ng-tns-c1267148319-52 ng-trigger ng-trigger-indicator"
                            style="transform: translateY(10px)"
                        >
                            <div
                                class="mat-sort-header-pointer-left ng-tns-c1267148319-52 ng-trigger ng-trigger-leftPointer"
                                style="transform: rotate(45deg)"
                            ></div>
                            <div
                                class="mat-sort-header-pointer-right ng-tns-c1267148319-52 ng-trigger ng-trigger-rightPointer"
                                style="transform: rotate(-45deg)"
                            ></div>
                            <div
                                class="mat-sort-header-pointer-middle ng-tns-c1267148319-52"
                            ></div>
                        </div>
                    </div>
                    <!---->
                </div>
            </th>
            <th
                _ngcontent-ng-c1685953515=""
                role="columnheader"
                mat-header-cell=""
                mat-sort-header=""
                class="mat-sort-header mat-mdc-header-cell mdc-data-table__header-cell cdk-header-cell hide-at-mobile ng-tns-c1267148319-53 cdk-column-userCount mat-column-userCount ng-star-inserted"
                aria-sort="none"
            >
                <div
                    class="mat-sort-header-container mat-focus-indicator ng-tns-c1267148319-53"
                    aria-describedby="cdk-describedby-message-ng-1-9"
                    cdk-describedby-host="ng-1"
                    tabindex="0"
                    role="button"
                >
                    <div class="mat-sort-header-content ng-tns-c1267148319-53">
                        用户
                    </div>
                    <div
                        class="mat-sort-header-arrow ng-trigger ng-trigger-arrowPosition ng-tns-c1267148319-53 ng-star-inserted"
                        style="transform: translateY(-25%); opacity: 0"
                    >
                        <div
                            class="mat-sort-header-stem ng-tns-c1267148319-53"
                        ></div>
                        <div
                            class="mat-sort-header-indicator ng-tns-c1267148319-53 ng-trigger ng-trigger-indicator"
                            style="transform: translateY(10px)"
                        >
                            <div
                                class="mat-sort-header-pointer-left ng-tns-c1267148319-53 ng-trigger ng-trigger-leftPointer"
                                style="transform: rotate(45deg)"
                            ></div>
                            <div
                                class="mat-sort-header-pointer-right ng-tns-c1267148319-53 ng-trigger ng-trigger-rightPointer"
                                style="transform: rotate(-45deg)"
                            ></div>
                            <div
                                class="mat-sort-header-pointer-middle ng-tns-c1267148319-53"
                            ></div>
                        </div>
                    </div>
                    <!---->
                </div>
            </th>
            <!---->
        </tr>
        <!---->
    </thead>
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
                    id="mat-mdc-checkbox-201"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-201-input"
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
                            for="mat-mdc-checkbox-201-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                aria-describedby="fbc_26"
                                                aria-owns="fbc_26"
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
                                                aria-describedby="fbc_27"
                                                aria-owns="fbc_27"
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
                        aria-describedby="cdk-describedby-message-ng-1-75"
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
                    href="/u/0/project/citysupereshop-prd/crashlytics/app/android:com.citysuper.eshop/issues/2dc01aa4d2945ade101fee85ce9faffa?hl=zh-cn&amp;time=last-ninety-days&amp;types=crash&amp;versions=1.7.0%20(1118)"
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
                    id="mat-mdc-checkbox-202"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-202-input"
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
                            for="mat-mdc-checkbox-202-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                                >com.citysuper.eshop.components</span
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >NormalViewPager2Adapter.kt:35</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >ViewFragment.onViewCreated</span
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
                                    >java.lang.IndexOutOfBoundsException - Empty
                                    list doesn't contain element at index
                                    0.</span
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
                        <span _ngcontent-ng-c1685953515="">48 次崩溃</span
                        >&nbsp;
                        <span _ngcontent-ng-c1685953515="">32 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    48 </a
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
                    32 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-203"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-203-input"
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
                            for="mat-mdc-checkbox-203-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >MainActivity.kt:126</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >MainActivity.onCreate</span
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
                                    >java.lang.NoSuchMethodException -
                                    com.citysuper.eshop.components.InboxDetailViewFragment.&lt;init&gt;
                                    []</span
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
                        <span _ngcontent-ng-c1685953515="">42 次崩溃</span
                        >&nbsp;
                        <span _ngcontent-ng-c1685953515="">26 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    42 </a
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
                    26 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-204"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-204-input"
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
                            for="mat-mdc-checkbox-204-input"
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
                    href="/u/0/project/citysupereshop-prd/crashlytics/app/android:com.citysuper.eshop/issues/c8535f823e498742938943c06d38a312?hl=zh-cn&amp;time=last-ninety-days&amp;types=crash&amp;versions=1.7.0%20(1118)"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                                >com.citysuper.eshop.ui.fragment.cart.overview</span
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >OverviewFragment.kt:655</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >OverviewFragment.handleShopifyResult</span
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
                                    >java.lang.IllegalStateException - Can't
                                    access the Fragment View's LifecycleOwner
                                    when getView() is null i.e., before
                                    onCreateView() or after
                                    onDestroyView()</span
                                >
                            </div>
                            <!---->
                            <div
                                _ngcontent-ng-c129725039=""
                                class="sub-issue-count ng-star-inserted"
                            >
                                <mat-icon
                                    _ngcontent-ng-c129725039=""
                                    role="img"
                                    class="mat-icon notranslate sub-issue-count-icon material-icons mat-ligature-font mat-icon-no-color"
                                    aria-hidden="true"
                                    data-mat-icon-type="font"
                                    >arrow_split</mat-icon
                                >
                                <!---->
                                <span
                                    _ngcontent-ng-c129725039=""
                                    class="ng-star-inserted"
                                >
                                    2 </span
                                ><!---->
                                变体
                            </div>
                            <!---->
                        </div>
                        <!----></issue-caption-table-cell
                    ><!---->
                    <div
                        _ngcontent-ng-c1685953515=""
                        class="mobile-stats show-at-mobile"
                    >
                        <span _ngcontent-ng-c1685953515="">33 次崩溃</span
                        >&nbsp;
                        <span _ngcontent-ng-c1685953515="">22 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    33 </a
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
                    22 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-205"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-205-input"
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
                            for="mat-mdc-checkbox-205-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                        <!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedLibraryWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
                                            aria-describedby="cdk-describedby-message-ng-1-77"
                                            cdk-describedby-host="ng-1"
                                        >
                                            <mat-icon
                                                _ngcontent-ng-c3846189135=""
                                                role="img"
                                                class="mat-icon notranslate metadata-icons material-icons mat-ligature-font mat-icon-no-color"
                                                aria-hidden="true"
                                                data-mat-icon-type="font"
                                            >
                                                developer_guide </mat-icon
                                            ><span
                                                _ngcontent-ng-c3846189135=""
                                                class="copy-target"
                                                >com.citysuper.eshop</span
                                            >
                                        </div>
                                        <!----><!---->
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >DeliveryFragment.java:2</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><c9s-issue-tags
                                        _ngcontent-ng-c3846189135=""
                                        data-test-id="signals"
                                        _nghost-ng-c3492471496=""
                                        aria-label="有一个问题信号"
                                        class="ng-star-inserted"
                                        ><div
                                            _ngcontent-ng-c3492471496=""
                                            class="c9s-issue-tags ng-star-inserted"
                                        >
                                            <fire-chip
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
                                                aria-describedby="fbc_28"
                                                aria-owns="fbc_28"
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
                                    >com.citysuper.eshop.ui.fragment.cart.delivery.DeliveryFragment.updateDeliveryMethod</span
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
                                    >java.lang.NullPointerException - Attempt to
                                    invoke virtual method 'int
                                    com.google.android.material.tabs.TabLayout.getSelectedTabPosition()'
                                    on a null object reference</span
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
                        <span _ngcontent-ng-c1685953515="">31 次崩溃</span
                        >&nbsp;
                        <span _ngcontent-ng-c1685953515="">11 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-78"
                        cdk-describedby-host="ng-1"
                    >
                        1.5.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    31 </a
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
                    11 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-206"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-206-input"
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
                            for="mat-mdc-checkbox-206-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                                >com.citysuper.eshop.ui.fragment.cart.overview</span
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >OverviewFragment.java:265</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >OverviewFragment.applyDiscount</span
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
                                    >java.lang.IllegalStateException - Fragment
                                    OverviewFragment{89593df}
                                    (d63f3910-d400-42e9-bea5-29417f1fd52f) not
                                    attached to a context.</span
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
                        <span _ngcontent-ng-c1685953515="">12 次崩溃</span
                        >&nbsp;
                        <span _ngcontent-ng-c1685953515="">10 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    12 </a
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
                    10 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-207"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-207-input"
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
                            for="mat-mdc-checkbox-207-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >QrCodeActivity.java:96</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >QrCodeActivity$loadQRCodeData$1.invoke$lambda-2$lambda-0</span
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
                                    >java.lang.OutOfMemoryError</span
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
                        <span _ngcontent-ng-c1685953515="">9 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">1 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-79"
                        cdk-describedby-host="ng-1"
                    >
                        1.7.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    9 </a
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
                    1 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-208"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-208-input"
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
                            for="mat-mdc-checkbox-208-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                                >com.citysuper.eshop.extensions</span
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >TextExtensions.kt:42</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >TextExtensionsKt.findMatchResult</span
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
                                    >java.util.regex.PatternSyntaxException -
                                    Incorrectly nested parentheses in regexp
                                    pattern near index 30 CANDOLINI GRAPPA
                                    BIANCA (700mL</span
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
                        <span _ngcontent-ng-c1685953515="">8 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">6 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    8 </a
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
                    6 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-209"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-209-input"
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
                            for="mat-mdc-checkbox-209-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                                >com.citysuper.eshop.ui.fragment.cart.delivery</span
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >DeliveryFragment.kt:268</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >DeliveryFragment$onViewCreated$7$1$1.invoke</span
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
                                    >java.lang.IllegalStateException - Can't
                                    access the Fragment View's LifecycleOwner
                                    when getView() is null i.e., before
                                    onCreateView() or after
                                    onDestroyView()</span
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
                        <span _ngcontent-ng-c1685953515="">7 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">7 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    7 </a
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
                    7 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-210"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-210-input"
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
                            for="mat-mdc-checkbox-210-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                                >com.citysuper.eshop.ui.fragment.cart.overview</span
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >OverviewFragment.kt:623</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >OverviewFragment.loadingIconHandler</span
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
                                    >java.lang.IllegalStateException - Fragment
                                    OverviewFragment{3a4c2e}
                                    (a3c11cb9-6175-4424-8b6c-f206f960c378) not
                                    attached to an activity.</span
                                >
                            </div>
                            <!---->
                            <div
                                _ngcontent-ng-c129725039=""
                                class="sub-issue-count ng-star-inserted"
                            >
                                <mat-icon
                                    _ngcontent-ng-c129725039=""
                                    role="img"
                                    class="mat-icon notranslate sub-issue-count-icon material-icons mat-ligature-font mat-icon-no-color"
                                    aria-hidden="true"
                                    data-mat-icon-type="font"
                                    >arrow_split</mat-icon
                                >
                                <!---->
                                <span
                                    _ngcontent-ng-c129725039=""
                                    class="ng-star-inserted"
                                >
                                    2 </span
                                ><!---->
                                变体
                            </div>
                            <!---->
                        </div>
                        <!----></issue-caption-table-cell
                    ><!---->
                    <div
                        _ngcontent-ng-c1685953515=""
                        class="mobile-stats show-at-mobile"
                    >
                        <span _ngcontent-ng-c1685953515="">5 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">5 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    5 </a
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
                    5 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-211"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-211-input"
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
                            for="mat-mdc-checkbox-211-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                                >com.citysuper.eshop.dialog</span
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >AlertDialog.kt:47</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >AlertStatementDialog.&lt;init&gt;</span
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
                                    >java.lang.RuntimeException - Can't create
                                    handler inside thread Thread[OkHttp
                                    https://citysuper-mobile.myshopify.com/...,5,main]
                                    that has not called Looper.prepare()</span
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
                        <span _ngcontent-ng-c1685953515="">5 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">5 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    5 </a
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
                    5 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-212"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-212-input"
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
                            for="mat-mdc-checkbox-212-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >MainActivity.kt:639</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >MainActivity.onDestroy</span
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
                                    >java.lang.IllegalStateException - View
                                    androidx.fragment.app.FragmentContainerView{100e25b
                                    V.E...... ......ID 0,170-1080,1968 #7f0a03d8
                                    app:id/nav_host_container} does not have a
                                    NavController set</span
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
                        <span _ngcontent-ng-c1685953515="">3 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">3 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    3 </a
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
                    3 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-213"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-213-input"
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
                            for="mat-mdc-checkbox-213-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
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
                                                >com.citysuper.eshop.fragments</span
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
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
                                                >CollectionFragment.kt:435</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><c9s-issue-tags
                                        _ngcontent-ng-c3846189135=""
                                        data-test-id="signals"
                                        _nghost-ng-c3492471496=""
                                        aria-label="有一个问题信号"
                                        class="ng-star-inserted"
                                        ><div
                                            _ngcontent-ng-c3492471496=""
                                            class="c9s-issue-tags ng-star-inserted"
                                        >
                                            <fire-chip
                                                _ngcontent-ng-c3492471496=""
                                                tabindex="0"
                                                class="signal-chip fire-popover-trigger is-freshness is-size__dense is-hairline ng-star-inserted"
                                                _nghost-ng-c115418348=""
                                                style="
                                                    --__fire-chip-bg-color: var(
                                                        --theme-color-bg
                                                    );
                                                    --__fire-chip-color: var(
                                                        --theme-color-fg-secondary
                                                    );
                                                "
                                                aria-describedby="fbc_29"
                                                aria-owns="fbc_29"
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
                                                        >auto_awesome</mat-icon
                                                    >
                                                    新问题
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
                                    >CollectionFragment$onViewCreated$13$1.invoke</span
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
                                    >java.lang.IllegalStateException - Fragment
                                    CollectionFragment{e045fdb}
                                    (9cd4d61c-c029-4f7e-82e1-97a79e93f9b3) not
                                    associated with a fragment manager.</span
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
                        <span _ngcontent-ng-c1685953515="">3 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">2 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-79"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.7.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    3 </a
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
                    2 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-214"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-214-input"
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
                            for="mat-mdc-checkbox-214-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >com.citysuper.eshop.fragments</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >ProfileFragment.kt:211</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >ProfileFragment.callAPI</span
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
                                    >java.lang.IllegalStateException - Can't
                                    access the Fragment View's LifecycleOwner
                                    when getView() is null i.e., before
                                    onCreateView() or after
                                    onDestroyView()</span
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
                        <span _ngcontent-ng-c1685953515="">3 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">2 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-79"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.7.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    3 </a
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
                    2 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-215"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-215-input"
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
                            for="mat-mdc-checkbox-215-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >com.citysuper.eshop.dialog</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >LoadingDialog.kt:63</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >LoadingDialog.dismiss</span
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
                                    >java.lang.IllegalArgumentException -
                                    View=DecorView@48067a0[MainActivity] not
                                    attached to window manager</span
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
                        <span _ngcontent-ng-c1685953515="">3 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">2 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    3 </a
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
                    2 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-216"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-216-input"
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
                            for="mat-mdc-checkbox-216-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >CartActivity.kt:119</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >CartActivity.addFragment</span
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
                                    >java.lang.IllegalStateException - Can not
                                    perform this action after
                                    onSaveInstanceState</span
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
                        <span _ngcontent-ng-c1685953515="">3 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">3 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    3 </a
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
                    3 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-217"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-217-input"
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
                            for="mat-mdc-checkbox-217-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >com.citysuper.eshop.retrofit</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >OkHttpClient.kt:1104</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >RetrofitFactory$makeRetrofitService$$inlined$-addInterceptor$1.intercept</span
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
                                    >android.system.GaiException -
                                    android_getaddrinfo failed: EAI_NODATA (No
                                    address associated with hostname)</span
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
                        <span _ngcontent-ng-c1685953515="">2 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">1 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-79"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.7.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    2 </a
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
                    1 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-218"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-218-input"
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
                            for="mat-mdc-checkbox-218-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >com.citysuper.eshop.ui.fragment.cart.overview</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >OverviewFragment.kt:111</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >OverviewFragment.onCreateView</span
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
                                    >java.lang.IllegalStateException - Required
                                    value was null.</span
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
                        <span _ngcontent-ng-c1685953515="">2 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">2 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    2 </a
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
                    2 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-219"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-219-input"
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
                            for="mat-mdc-checkbox-219-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >com.citysuper.eshop.ui.fragment.cart.delivery</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >DeliveryFragment.kt:226</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >DeliveryFragment$onViewCreated$7$1.invoke</span
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
                                    >java.lang.IllegalStateException - Fragment
                                    DeliveryFragment{eeb7a44}
                                    (19ae760d-3304-475c-949a-b342dfcfc915) not
                                    attached to a context.</span
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
                        <span _ngcontent-ng-c1685953515="">2 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">1 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    2 </a
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
                    1 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-220"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-220-input"
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
                            for="mat-mdc-checkbox-220-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >com.citysuper.eshop.ui.fragment.cart.overview</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >OverviewFragment.kt:294</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >OverviewFragment.fetchCart</span
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
                                    >java.lang.IllegalStateException - Fragment
                                    OverviewFragment{b0e8816}
                                    (e5026b7a-abb9-442a-bc29-9ee9847f0a84) not
                                    attached to a context.</span
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
                        <span _ngcontent-ng-c1685953515="">2 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">2 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    2 </a
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
                    2 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-221"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-221-input"
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
                            for="mat-mdc-checkbox-221-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >com.citysuper.eshop.fragments.bottomsheet</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >AddToCartBottomSheetFragment.kt:201</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >AddToCartBottomSheetFragment$onViewCreated$6$1$1.invoke</span
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
                                    >java.lang.IllegalStateException - Can not
                                    perform this action after
                                    onSaveInstanceState</span
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
                        <span _ngcontent-ng-c1685953515="">2 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">2 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    2 </a
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
                    2 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-222"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-222-input"
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
                            for="mat-mdc-checkbox-222-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >androidx.profileinstaller</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >ProfileInstallReceiver.java:75</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >ProfileInstallReceiver.onReceive</span
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
                                    >java.lang.NullPointerException - Attempt to
                                    invoke virtual method 'java.lang.String
                                    android.os.Bundle.getString(java.lang.String)'
                                    on a null object reference</span
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
                        <span _ngcontent-ng-c1685953515="">1 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">1 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    1 </a
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
                    1 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-223"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-223-input"
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
                            for="mat-mdc-checkbox-223-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >MainActivity.java:886</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >MainActivity.navToSearchHistoryFragment</span
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
                                    >java.lang.NullPointerException - null
                                    cannot be cast to non-null type
                                    androidx.navigation.fragment.FragmentNavigator.Destination</span
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
                        <span _ngcontent-ng-c1685953515="">1 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">1 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-76"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.6.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    1 </a
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
                    1 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-224"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-224-input"
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
                            for="mat-mdc-checkbox-224-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                            aria-describedby="cdk-describedby-message-ng-1-73"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >com.citysuper.eshop.retrofit</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >OkHttpClient.kt:1104</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >RetrofitFactory$makeRetrofitService$$inlined$-addInterceptor$1.intercept</span
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
                                    >android.system.ErrnoException - isConnected
                                    failed: ECONNABORTED (Software caused
                                    connection abort)</span
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
                        <span _ngcontent-ng-c1685953515="">1 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">1 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-79"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.7.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    1 </a
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
                    1 </a
                ><!---->
            </td>
            <!---->
        </tr>
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
                    id="mat-mdc-checkbox-225"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-225-input"
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
                            for="mat-mdc-checkbox-225-input"
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
                                            aria-describedby="cdk-describedby-message-ng-1-72"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                        <!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedLibraryWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-77"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
                                        >
                                            <mat-icon
                                                _ngcontent-ng-c3846189135=""
                                                role="img"
                                                class="mat-icon notranslate metadata-icons material-icons mat-ligature-font mat-icon-no-color"
                                                aria-hidden="true"
                                                data-mat-icon-type="font"
                                            >
                                                developer_guide </mat-icon
                                            ><span
                                                _ngcontent-ng-c3846189135=""
                                                class="copy-target"
                                                >com.citysuper.eshop</span
                                            >
                                        </div>
                                        <!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
                                            aria-describedby="cdk-describedby-message-ng-1-74"
                                            cdk-describedby-host="ng-1"
                                            style="
                                                user-select: none;
                                                -webkit-user-drag: none;
                                                touch-action: none;
                                                -webkit-tap-highlight-color: transparent;
                                            "
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
                                                >NetworkErrorDialog.kt:5</span
                                            >
                                        </div>
                                        <!----><!---->
                                    </div>
                                    <!----><!---->
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
                                    >com.citysuper.eshop.dialog.NetworkErrorDialogKt.networkError</span
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
                                    >android.view.WindowManager$BadTokenException
                                    - Unable to add window -- token null is not
                                    valid; is your activity running?</span
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
                        <span _ngcontent-ng-c1685953515="">1 次崩溃</span>&nbsp;
                        <span _ngcontent-ng-c1685953515="">1 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-78"
                        cdk-describedby-host="ng-1"
                        style="
                            user-select: none;
                            -webkit-user-drag: none;
                            touch-action: none;
                            -webkit-tap-highlight-color: transparent;
                        "
                    >
                        1.5.0 – 1.7.0 </span
                    ><!----><!----></a
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
                    1 </a
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
                    1 </a
                ><!---->
            </td>
            <!---->
        </tr>
        <!----><!---->
    </tbody>
    <tfoot
        role="rowgroup"
        class="mat-mdc-table-sticky"
        style="display: none; bottom: 0px; z-index: 10"
    >
        <!---->
    </tfoot>
</table>
"""

# 使用lxml解析器解析HTML
soup = BeautifulSoup(html, 'lxml')

# 找到所有的<tr>标签
table = soup.find('table')
tbody = table.find('tbody')
rows = tbody.find_all('tr')


for index, row in enumerate(rows, start=1):
    title_text = ""
    version_text = ""

    title = row.find('div', {'class': 'title-wrapper'})

    event_cell = row.find_all('td')[3]
    event_text = event_cell.get_text(strip=True)

    version_cell = row.find_all('td')[2]

    if title is not None:
        title_text = title.get_text(strip=True)

    if version_cell:
        version_span_element = version_cell.find('span', class_='mat-mdc-tooltip-trigger')
        if version_span_element:
            version_text = version_span_element.get_text(strip=True)

            print(f"{index}. {title_text} {event_text} 影響版本 {version_text}")

    if index == 3:
        break
