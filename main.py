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
                    id="mat-mdc-checkbox-6"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-6-input"
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
                            for="mat-mdc-checkbox-6-input"
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
                class="mat-sort-header mat-mdc-header-cell mdc-data-table__header-cell cdk-header-cell hide-at-mobile ng-tns-c1267148319-10 cdk-column-eventCount mat-column-eventCount mat-sort-header-disabled ng-star-inserted"
            >
                <div
                    class="mat-sort-header-container mat-focus-indicator ng-tns-c1267148319-10 mat-sort-header-sorted"
                    aria-describedby="cdk-describedby-message-ng-1-8"
                    cdk-describedby-host="ng-1"
                >
                    <div class="mat-sort-header-content ng-tns-c1267148319-10">
                        事件
                    </div>
                    <div
                        class="mat-sort-header-arrow ng-trigger ng-trigger-arrowPosition ng-tns-c1267148319-10 ng-star-inserted"
                        style="transform: translateY(0px); opacity: 1"
                    >
                        <div
                            class="mat-sort-header-stem ng-tns-c1267148319-10"
                        ></div>
                        <div
                            class="mat-sort-header-indicator ng-tns-c1267148319-10 ng-trigger ng-trigger-indicator"
                            style="transform: translateY(10px)"
                        >
                            <div
                                class="mat-sort-header-pointer-left ng-tns-c1267148319-10 ng-trigger ng-trigger-leftPointer"
                                style="transform: rotate(45deg)"
                            ></div>
                            <div
                                class="mat-sort-header-pointer-right ng-tns-c1267148319-10 ng-trigger ng-trigger-rightPointer"
                                style="transform: rotate(-45deg)"
                            ></div>
                            <div
                                class="mat-sort-header-pointer-middle ng-tns-c1267148319-10"
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
                class="mat-sort-header mat-mdc-header-cell mdc-data-table__header-cell cdk-header-cell hide-at-mobile ng-tns-c1267148319-11 cdk-column-userCount mat-column-userCount ng-star-inserted"
                aria-sort="none"
            >
                <div
                    class="mat-sort-header-container mat-focus-indicator ng-tns-c1267148319-11"
                    aria-describedby="cdk-describedby-message-ng-1-9"
                    cdk-describedby-host="ng-1"
                    tabindex="0"
                    role="button"
                >
                    <div class="mat-sort-header-content ng-tns-c1267148319-11">
                        用户
                    </div>
                    <div
                        class="mat-sort-header-arrow ng-trigger ng-trigger-arrowPosition ng-tns-c1267148319-11 ng-star-inserted"
                        style="transform: translateY(-25%); opacity: 0"
                    >
                        <div
                            class="mat-sort-header-stem ng-tns-c1267148319-11"
                        ></div>
                        <div
                            class="mat-sort-header-indicator ng-tns-c1267148319-11 ng-trigger ng-trigger-indicator"
                            style="transform: translateY(10px)"
                        >
                            <div
                                class="mat-sort-header-pointer-left ng-tns-c1267148319-11 ng-trigger ng-trigger-leftPointer"
                                style="transform: rotate(45deg)"
                            ></div>
                            <div
                                class="mat-sort-header-pointer-right ng-tns-c1267148319-11 ng-trigger ng-trigger-rightPointer"
                                style="transform: rotate(-45deg)"
                            ></div>
                            <div
                                class="mat-sort-header-pointer-middle ng-tns-c1267148319-11"
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
                    id="mat-mdc-checkbox-17"
                    ><div class="mdc-form-field">
                        <div class="mdc-checkbox">
                            <div class="mat-mdc-checkbox-touch-target"></div>
                            <input
                                type="checkbox"
                                class="mdc-checkbox__native-control"
                                id="mat-mdc-checkbox-17-input"
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
                            for="mat-mdc-checkbox-17-input"
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
                                                >com.citysuper.eshop.components</span
                                            >
                                        </div>
                                        <!----><!----><!---->
                                        <div
                                            _ngcontent-ng-c3846189135=""
                                            data-test-id="blamedFileWrapper"
                                            mattooltipposition="above"
                                            class="mat-mdc-tooltip-trigger metadata-wrapper ng-star-inserted"
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
                        <span _ngcontent-ng-c1685953515="">23 次崩溃</span
                        >&nbsp;
                        <span _ngcontent-ng-c1685953515="">19 个用户</span>
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
                        aria-describedby="cdk-describedby-message-ng-1-17"
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
                    href="/u/0/project/citysupereshop-prd/crashlytics/app/android:com.citysuper.eshop/issues/fbec9941a784336ca6b33309e6ef69c7?hl=zh-cn&amp;time=last-ninety-days&amp;versions=1.6.0%20(1116);1.6.0%20(1111);1.6.0%20(1110);1.6.0%20(1109)&amp;types=crash"
                    style="cursor: pointer"
                >
                    23 </a
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
                    19 </a
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
    cells = row.find_all('td')  # 如果你想提取<td>元素的值
    for cell in cells:
        # 提取单元格内容
        cell_text = cell.get_text(strip=True)
        print(cell_text)
